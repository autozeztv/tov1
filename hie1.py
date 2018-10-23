# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

nadya = LINE()
#nadya = LINE("TOKEN KAMU")
#nadya = LINE("Email","Password")
nadya.log("Auth Token : " + str(nadya.authToken))
channelToken = nadya.getChannelResult()
nadya.log("Channel Token : " + str(channelToken))

nadyaMID = nadya.profile.mid
nadyaProfile = nadya.getProfile()
lineSettings = nadya.getSettings()
oepoll = OEPoll(nadya)
Rfu = [nadya]
RfuBot=[nadyaMID]
supperadmin=['ue9781edcd4eecd9abfd6e50fc3ea95b1',nadyaMID]
admin=['ue9781edcd4eecd9abfd6e50fc3ea95b1','u9cff30bb3b8bd344356702e0340ce793',nadyaMID]
Family=["ue9781edcd4eecd9abfd6e50fc3ea95b1","u9cff30bb3b8bd344356702e0340ce793",nadyaMID]
RfuFamily = RfuBot + Family
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)

wait = {
   'acommentOn':False,
   'bcommentOn':False,
   'AutoJoin':False,
   'autoLeave':False,
   'AutoAdd':False,
   'AutoRead':False,
   "server":"VPS",
   "userAgent": [
       "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
       "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
       "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
       "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
       "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
       "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
       "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
       "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
       "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
   ],
   "mimic": {
       "copy": False,
       "status": False,
       "target": {}
   }
}

RfuProtect = {
    "AutoAdd":False,
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = nadyaProfile.displayName
myProfile["statusMessage"] = nadyaProfile.statusMessage
myProfile["pictureStatus"] = nadyaProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    nadya.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        nadya.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def mentionMembers2(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = '╔════════════\n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '║ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╚════════════'
        if result:
            if result.endswith('\n'): result = result[:-1]
            nadya.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''
myMid = nadya.profile.mid

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            nadya.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def helpmessage():
    helpMessage =  "คำสั่งทั้งหมดพิม . ข้างหน้าคำสั่งแทน -" + "\n" + \
                  " " + "\n" + \
                  "คำสั่ง" + "\n" + \
                  "คำสั่ง2" + "\n" + \
                  " " + "\n" + \
                  "-สปีด" + "\n" + \
                  "-เชคค่า" + "\n" + \
                  "-ข้อมูล" + "\n" + \
                  "-เทส" + "\n" + \
                  "-รีบอท" + "\n" + \
                  "-ออน" + "\n" + \
                  "-พูด(ข้อความ)" + "\n" + \
                  "-ชื่อ: (ชื่อ)" + "\n" + \
                  "-ตัส: (ตัส)" + "\n" + \
                  "-ข้อมูล" + "\n" + \
                  "-โทร (จำนวนการเชิญ)" + "\n" + \
                  "-เชคแอด" + "\n" + \
                  "-สแปม「On/Off」(เลข)(ข้อความ)" + "\n" + \
                  "-ยกแชท(จำนวน)" + "\n" + \
                  "-คท" + "\n" + \
                  "-มิด" + "\n" + \
                  "-ชื่อ" + "\n" + \
                  "-ตัส" + "\n" + \
                  "-รูป" + "\n" + \
                  "-ปก" + "\n" + \
                  "-คท @" + "\n" + \
                  "-มิด @" + "\n" + \
                  "-ชื่อ @" + "\n" + \
                  "-ตัส @" + "\n" + \
                  "-ดิส @" + "\n" + \
                  "-เตะ @" + "\n" + \
                  "-เด้ง @" + "\n" + \
                  "-!แทค" + "\n" + \
                  "-!มิด" "\n" + \
                  "-!คท" + "\n" + \
                  "-แทค" + "\n" + \
                  "-ชื่อกลุ่ม" + "\n" + \
                  "-ไอดีกลุ่ม" + "\n" + \
                  "-รูปกลุ่ม" + "\n" + \
                  "-กลุ่มทั้งหมด" + "\n" + \
                  "-ข้อมูลกลุ่ม" + "\n" + \
                  "-สมาชิก" + "\n" + \
                  "-ลิ้งกลุ่ม" + "\n" + \
                  "-เพิ่มพิมตาม" + "\n" + \
                  "-ลบพิมตาม" + "\n" + \
                  "-อ่าน" + "\n" + \
                  "-ยกเลิก" + "\n" + \
                  "-เปลี่ยนรูป" + "\n" + \
                  "-ประกาศ: (ข้อความ)" + "\n" + \
                  " " + "\n" + \
                  "*คำสั่งเฉพาะบัญชีเท่านั้น*"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "คำสั่งทั้งหมดพิม \ ข้างหน้าคำสั่งแทน -" + "\n" +\
                         " " + "\n" \
                         "-หาคนอ่าน 「On/Off/Reset」" + "\n" + \
                         "-ลิ้ง 「On/Off」" + "\n" + \
                         "-พิมตาม 「On/Off」" + "\n" + \
                         "-เข้ากลุ่ม「On/Off」" + "\n" + \
                         "-อ่านออโต้「On/Off」" + "\n" + \
                         "-ออโต้บล็อค 「On/Off」" + "\n" + \
                         "-ออกกลุ่ม 「On/Off」" + "\n" + \
                         "-ตอนรับ 「On/Off」" + "\n" + \
                         "-ตอนรับออก 「On/Off」" + "\n" + \
                         " " + "\n" + \
                         "-ตั้งออก:" + "\n" + \
                         "-ตั้งเข้า:" + "\n" + \
                         "-เชคออก" + "\n" + \
                         "-เชคเข้า" + "\n" + \
                         " " + "\n " \
                         "**คำสั่งเฉพาะบัญขีเท่านั้น**"
    return helpTextToSpeech
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTOBLOCK")
            if settings["autoAdd"] == True:
            	nadya.blockContact(op.param1)
                #nadya.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(nadya.getContact(op.param1).displayName)))

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = nadya.getGroup(op.param1)
            if settings["autoJoin"] == True:
                nadya.acceptGroupInvitation(op.param1)

        if op.type == 15:
            if wait["bcommentOn"] and "bcomment" in wait:
            	nadya.sendMessage(op.param1, None, contentMetadata={"STKID":"20071427","STKPKGID":"1585840","STKVER":"1"}, contentType=7)
                nadya.sendMessage(op.param1,nadya.getContact(op.param2).displayName + "\n\n" + str(wait["bcomment"]))
           
        if op.type == 17:
            if wait["acommentOn"] and "acomment" in wait:
                cnt = nadya. getContact(op.param2)
                nadya.sendMessage(op.param1,cnt.displayName + "\n\n" + str(wait["acomment"]))

        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                nadya.leaveRoom(op.param1)

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
  
#==============================================================================#
                elif text.lower() == 'คำสั่ง':
                    helpMessage = helpmessage()
                    nadya.sendReplyMessage(msg.id, msg.to, str(helpMessage))
                elif text.lower() == 'คำสั่ง2':
                    helpTextToSpeech = helptexttospeech()
                    nadya.sendReplyMessage(msg.id, msg.to, str(helpTextToSpeech))
#==============================================================================#
                elif "google " in msg.text.lower():
                    spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        nadya.sendReplyMessage(msg.id, msg.to, "กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        nadya.sendReplyMessage(msg.id, msg.to, msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        nadya.sendReplyMessage(msg.id, msg.to, str(text))
                                    else:
                                        nadya.sendReplyMessage(msg.id, msg.to, msg.from_,str(text))
                                except Exception as e:
                                    print(e)

                elif "youtube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "ผมการค้นหาจาก YouTube\n\n"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n{}".format(str(data["title"]))
                            ret_ += "\nhttps://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\nจำนวนที่พบ {}".format(len(datas))
                        nadya.sendReplyMessage(msg.id, msg.to, "กำลังรับข้อมูล กรุณารอสักครู่..")
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))

                elif ".ประกาศ:" in msg.text:
                      bctxt = text.replace(".ประกาศ:","")
                      n = nadya.getGroupIdsJoined()
                      for manusia in n:
                          nadya.sendMessage(manusia,(bctxt))
                elif ".สแปม " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace(".สแปม "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               nadya.sendReplyMessage(msg.id, msg.to, teks)
                        else:
                           nadya.sendReplyMessage(msg.id, msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            nadya.sendReplyMessage(msg.id, msg.to, tulisan)
                        else:
                            nadya.sendReplyMessage(msg.id, msg.to, "Out Of Range!")
                elif ".โทร" in msg.text.lower():
                     if msg.toType == 2:
                            sep = text.split(" ")
                            strnum = text.replace(sep[0] + " ","")
                            num = int(strnum)
                            nadya.sendReplyMessage(msg.id, msg.to, "เชิญเข้าร่วมการโทร(。-`ω´-)")
                            for var in range(0,num):
                                group = nadya.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                nadya.acquireGroupCallRoute(to)
                                nadya.inviteIntoGroupCall(to, contactIds=members)
                elif ".ทีมงาน" == msg.text.lower():
                    msg.contentType = 13
                    nadya.sendReplyMessage(msg.id, msg.to, "「 BOT TEAM 」 • H0ck")
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':'ue9781edcd4eecd9abfd6e50fc3ea95b1'}, contentType=13) 
                elif ".เทส" == msg.text.lower():
                    nadya.sendReplyMessage(msg.id, msg.to, "LOADING:▒...0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "█▒... 10.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "██▒... 20.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "███▒... 30.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "████▒... 40.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "█████▒... 50.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "██████▒... 60.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "███████▒... 70.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "████████▒... 80.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "█████████▒... 90.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "███████████..100.0%")
                    nadya.sendReplyMessage(msg.id, msg.to, "บอทปกติดี(。-`ω´-)")

                elif ".ชื่อ: " in text.lower():
                    if msg._from in admin:
                           proses = text.split(": ")
                           string = text.replace(proses[0] + ": ","")
                           profile_A = nadya.getProfile()
                           profile_A.displayName = string
                           nadya.updateProfile(profile_A)
                           nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนชื่อเป็น(。-`ω´-) " + string)
                elif ".ตัส: " in msg.text.lower():
                	if msg._from in admin:
                           proses = text.split(": ")
                           string = text.replace(proses[0] + ": ","")
                           profile_A = nadya.getProfile()
                           profile_A.statusMessage = string
                           nadya.updateProfile(profile_A)
                           nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนตัสเสร็จสิ้น(。-`ω´-)  " + string)

                elif msg.text.lower().startswith(".ยกแชท "):
                    args = msg.text.replace(".ยกแชท ","")
                    mes = 0
                    try:
                       mes = int(args[1])
                    except:
                       mes = 1
                    M = nadya.getRecentMessagesV2(to, 101)
                    MId = []
                    for ind,i in enumerate(M):
                       if ind == 0:
                           pass
                       else:
                           if i._from == alcohol.profile.mid:
                               MId.append(i.id)
                               if len(MId) == mes:
                                   break
                    def unsMes(msg_id):
                     nadya.unsendMessage(msg_id)
                    for i in MId:
                     thread1 = threading.Thread(target=unsMes, args=(i,))
                     thread1.start()
                     thread1.join()
                    nadya.sendReplyMessage(msg.id, msg.to, 'ยกเลิก {} ข้อความเรียบร้อยแล้ว(。-`ω´-)'.format(len(MId)))

                elif msg.text in ["/token"]:
                  if msg._from in admin:
                      nadya.sendReplyMessage(msg.id, msg.to, nadya.authToken)

                elif "/mic " in msg.text:
                  if msg._from in admin:
                      mmid = msg.text.replace("/mic ","")
                      nadya.sendReplyMessage(msg.id, msg.to, text=None, contentMetadata={'mid': mmid}, contentType=13)

                elif text.lower() == 'ของขวัญ1':
                  nadya.sendGift(msg.to,'608','sticker')
							
                elif text.lower() == 'ของขวัญ2':
                  nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'PRDID': '88efc1ed-744d-4704-a77a-bb79077f5d22','PRDTYPE': 'THEME','MSGTPL': '100'}, contentType = 9)

                elif ".ยกเลิก" == msg.text.lower():
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            nadya.cancelGroupInvitation(msg.to,[_mid])
                        nadya.sendReplyMessage(msg.id, msg.to, "ยกเลิกค้างเชิญเสร็จสิ้น(。-`ω´-)")
                elif text.lower() == '.ลบรัน':
                    gid = nadya.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        nadya.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    nadya.sendReplyMessage(msg.id, msg.to, "กำลังดำเนินการ(。-`ω´-)")
                    nadya.sendReplyMessage(msg.id, msg.to, "เวลาที่ใช้: %sวินาที(。-`ω´-)" % (elapsed_time))
                elif msg.text in [".speed",".sp",".สปีด",".Speed",".Sp"]:
                    start = time.time()
                    nadya.sendReplyMessage(msg.id, msg.to, "การตอบสนองของบอท(。-`ω´-)")
                    elapsed_time = time.time() - start
                    nadya.sendReplyMessage(msg.id, msg.to, "[ %s Seconds ]\n[ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == '.รีบอท':
                    nadya.sendReplyMessage(msg.id, msg.to, "กำลังรีบอท กรุณารอสักครู่.....(。-`ω´-)")
                    time.sleep(5)
                    nadya.sendReplyMessage(msg.id, msg.to, "รีบอทสำเร็จแล้ว\n✍️  ᴛ⃢​ᴇ⃢​ᴀ⃢​ᴍ⃢   🔝ͲᎻᎬᖴ͙͛Ꮮ͙͛ᗩ͙͛ᔑ͙͛Ꮋ͙  ̾⚡")
                    restartBot()
                elif text.lower() == '.ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendReplyMessage(msg.id, msg.to, "ระยะเวลาการทำงานของบอท(。-`ω´-)\n{}".format(str(runtime)))
                elif text.lower() == '.ข้อมูล':
                    try:
                        arr = []
                        owner = "ude3230559bf63a55b9c28aa20ea194e3"
                        creator = nadya.getContact(owner)
                        contact = nadya.getContact(nadyaMID)
                        grouplist = nadya.getGroupIdsJoined()
                        contactlist = nadya.getAllContactIds()
                        blockedlist = nadya.getBlockedContactIds()
                        ret_ = "╔══[ ข้อมูลไอดีคุณ ]"
                        ret_ += "\n╠ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n╠ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n╚══[ ข้อมูลไอดีคุณ ]"
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                    except Exception as e:
                        nadya.sendReplyMessage(msg.id, msg.to, str(e))
#==============================================================================#
                elif text.lower() == '.เชคค่า':
                    try:
                        ret_ = "╔════════════"
                        if settings["autoAdd"] == True: ret_ += "\n║ ระบบออโต้บล็อค ✔"
                        else: ret_ += "\n║ ระบบออโต้บล็อค ✘"
                        if settings["autoJoin"] == True: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✔"
                        else: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✘"
                        if settings["autoLeave"] == True: ret_ += "\n║ ระบบออกกลุ่มออโต้  ✔"
                        else: ret_ += "\n║ ระบบออกกลุ่มออโต้ ✘"
                        if settings["autoRead"] == True: ret_ += "\n║ ระบบอ่านข้อความออโต้  ✔"
                        else: ret_ += "\n║ ระบบอ่านข้อความออโต้ ✘"
                        if wait["acommentOn"] == True: ret_ += "\n║ ระบบตอนรับคนเข้ากลุ่ม ✔"
                        else: ret_ += "\n║ ระบบตอนรับคนเข้ากลุ่ม ✘"
                        if wait["bcommentOn"] == True: ret_ += "\n║ ระบบตอนรับคนออกกลุ่ม ✔"
                        else: ret_ += "\n║ ระบบตอนรับคนออกกลุ่ม ✘"
                        ret_ += "\n╚════════════"
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                    except Exception as e:
                        nadya.sendReplyMessage(msg.id, msg.to, str(e))
                elif text.lower() == '/ออโต้บล็อค on':
                    settings["autoAdd"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบออโต้บล็อค(。-`ω´-)")
                elif text.lower() == '/ออโต้บล็อค off':
                    settings["autoAdd"] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบออโต้บล็อค(。-`ω´-)")
                elif text.lower() == '/เข้ากลุ่ม on':
                    settings["autoJoin"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")
                elif text.lower() == '/เข้ากลุ่ม off':
                    settings["autoJoin"] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")
                elif text.lower() == '/ออกกลุ่ม on':
                    settings["autoLeave"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบออกกลุ่มออโต้(。-`ω´-)")
                elif text.lower() == '/ออกกลุ่ม off':
                    settings["autoLeave"] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบออกกลุ่มออโต้(。-`ω´-)")
                elif text.lower() == '/อ่านออโต้ on':
                    settings["autoRead"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบอ่านออโต้(。-`ω´-)")
                elif text.lower() == '/อ่านออโต้ off':
                    settings["autoRead"] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบอ่านออโต้(。-`ω´-)")
#==============================================================================#
                elif msg.text.lower() ==  '/ตอนรับ on':
                    wait['acommentOn'] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบตอนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")
                elif msg.text.lower() ==  '/ตอนรับ off':
                    wait['acommentOn'] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบตอนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")
                elif msg.text.lower() == '/ตอนรับออก on':
                    wait["bcommentOn"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบตอนรับสมาชิกออกกลุ่ม(。-`ω´-)")
                elif msg.text.lower() == '/ตอนรับออก off':
                    wait['bcommentOn'] = False
                    nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบตอนรับสมาชิกออกกลุ่ม(。-`ω´-)")
#==============================================================================#
                elif "/ตั้งเข้า:" in msg.text.lower():
                    c = msg.text.replace("/ตั้งเข้า:","")
                    if c in [""," ","\n",None]:
                        nadya.sendReplyMessage(msg.id, msg.to, "เกิดข้อผิดพลาด(。-`ω´-)")
                    else:
                        wait["acomment"] = c
                        nadya.sendReplyMessage(msg.id, msg.to, "ตั้งค่าข้อความตอนรับเสร็จสิ้น(。-`ω´-)")

                elif "/ตั้งออก:" in msg.text.lower():
                    c = msg.text.replace("/ตั้งออก:","")
                    if c in [""," ","\n",None]:
                        nadya.sendReplyMessage(msg.id, msg.to, "เกิดข้อผิดพลาด(。-`ω´-)")
                    else:
                        wait["bcomment"] = c
                        nadya.sendReplyMessage(msg.id, msg.to, "ตั้งค่าข้อความตอนรับออกเสร็จสิ้น(。-`ω´-)")
#==============================================================================#
                elif msg.text in ["/เชคเข้า"]:
                	nadya.sendReplyMessage(msg.id, msg.to, "เช็คข้อความตอนรับล่าสุด(。-`ω´-)" + "\n\n➤" + str(wait["acomment"]))
                elif msg.text in ["/เชคออก"]:
                	nadya.sendReplyMessage(msg.id, msg.to, "เช็คข้อความตอนรับออกล่าสุด(。-`ω´-)" + "\n\n➤" + str(wait["bcomment"]))
#==============================================================================#
                elif text.lower() == ".เปลี่ยนรูป":
                    settings["changePictureProfile"] = True
                    nadya.sendReplyMessage(msg.id, msg.to, "ส่งรูปมา(。-`ω´-)")
                elif text.lower() == '!แทค':
                    gs = nadya.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 NAME 」\n• NoName")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        nadya.sendMessage(to, mc)

                elif text.lower() == '!มิด':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 NAME 」\n• NoName")
                    else:
                        mc = "「 ID 」\n• "
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        nadya.sendReplyMessage(msg.id, msg.to, mc)

                elif text.lower() == '!คท':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 NAME 」\n• NoName")
                    else:
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':mi_d}, contentType=13)

                elif text.lower() == '.คท':
                    sendMessageWithMention(to, nadyaMID)
                    nadya.sendContact(to, nadyaMID)
                elif text.lower() == '.มิด':
                    nadya.sendReplyMessage(msg.id, msg.to, "「 MY ID 」\n•" + nadyaMID)
                elif text.lower() == '.ชื่อ':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 MY NAME 」\n•" + me.displayName)
                elif text.lower() == '.ตัส':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 MY STATUS 」\n•" + me.statusMessage)
                elif text.lower() == '.ดิส':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '.ดิสวีดีโอ':
                    me = nadya.getContact(nadyaMID)
                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == '.ดิสปก':
                    me = nadya.getContact(nadyaMID)
                    cover = nadya.getProfileCoverURL(nadyaMID)    
                    nadya.sendImageWithURL(msg.to, cover)

                elif msg.text.lower().startswith(".คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':mi_d}, contentType=13)

                elif msg.text.lower().startswith(".มิด "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "「 ID 」\n•"
                        for ls in lists:
                            ret_ += ls
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))

                elif msg.text.lower().startswith(".ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendReplyMessage(msg.id, msg.to, "「 NAME 」\n•" ,contact.displayName)

                elif msg.text.lower().startswith(".ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            nadya.sendReplyMessage(msg.id, msg.to, "「 STATUS 」\n•" ,contact.statusMessage)
                       
                elif msg.text.lower().startswith(".ดิส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + nadya.getContact(ls).pictureStatus
                            nadya.sendImageWithURL(msg.to, str(path))
                             
                elif msg.text.lower().startswith(".ปก "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                             if mention["M"] not in lists:
                                 lists.append(mention["M"])
                        for ls in lists:
                            cover = nadya.getProfileCoverURL(ls)
                            nadya.sendImageWithURL(to, str(cover))
                            
                elif msg.text.lower().startswith(".ข้อมูล "):
                    if nadya != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                me = nadya.getContact(ls)
                                path = nadya.getProfileCoverURL(ls)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    nadya.sendReplyMessage(msg.id, msg.to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    nadya.sendMentionFooter(to, '「 YOU SELF 」\n•', sender, "https://line.me/ti/p/~hietocih", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~hietocih', 'type': 'mt', 'subText': "「 BOT TEAM 」 • H1ck", 'a-installUrl': 'https://line.me/ti/p/~hietocih', 'a-installUrl': ' https://line.me/ti/p/~hietocih', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~hietocih', 'i-linkUri': 'https://line.me/ti/p/~hietocih', 'id': 'mt000000000a6b79f9', 'text': '「 BOT TEAM 」 • H1ck', 'linkUri': 'https://line.me/ti/p/~hietocih'}, contentType=19)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU ID 」\n•" +  ls)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU NAME 」\n•" +  me.displayName)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU STATUS 」\n•\n" +  me.statusMessage)
                                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    nadya.sendImageWithURL(to, str(path))
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    nadya.sendReplyMessage(msg.id, msg.to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    nadya.sendMentionFooter(to, '「 YOU SELF 」\n•', sender, "https://line.me/ti/p/~hietocih", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~hietocih', 'type': 'mt', 'subText': "「 BOT TEAM 」 • H1ck", 'a-installUrl': 'https://line.me/ti/p/~hietocih', 'a-installUrl': ' https://line.me/ti/p/~hietocih', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~hietocih', 'i-linkUri': 'https://line.me/ti/p/~hietocih', 'id': 'mt000000000a6b79f9', 'text': '「 BOT TEAM 」 • H1ck', 'linkUri': 'https://line.me/ti/p/~hietocih'}, contentType=19)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU ID 」\n•" +  ls)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU NAME 」\n•" +  me.displayName)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 YOU STATUS 」\n•\n" +  me.statusMessage)
                                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    nadya.sendImageWithURL(to, str(path))
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
#==============================================================================#
                elif ".เด้ง " in msg.text:
                        vkick0 = msg.text.replace(".เด้ง ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = nadya.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    nadya.kickoutFromGroup(msg.to,[target])
                                    nadya.findAndAddContactsByMid(target)
                                    nadya. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text.lower().startswith(".เตะ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            nadya.kickoutFromGroup(msg.to,[target])
                        except:
                            nadya.sendReplyMessage(msg.id, msg.to, "Error")
                elif msg.text.lower().startswith(".พิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            nadya.sendReplyMessage(msg.id, msg.to, "เพิ่มพิมตามเรียบร้อย(。-`ω´-)")
                            break
                        except:
                            nadya.sendReplyMessage(msg.id, msg.to, "เพิ่มพิมตามล้มเหลว(。-`ω´-)")
                            break
                elif msg.text.lower().startswith(".ลบพิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            nadya.sendReplyMessage(msg.id, msg.to, "ลบพิมตามเรียบร้อย(。-`ω´-)")
                            break
                        except:
                            nadya.sendReplyMessage(msg.id, msg.to, "ลบพิมตามล้มเหลว(。-`ω´-)")
                            break
                elif text.lower() == '.รายชื่อคนพิมตาม':
                    if settings["mimic"]["target"] == {}:
                        nadya.sendReplyMessage(msg.id, msg.to, "ไม่มีการเพิ่มก่อนหน้านี้(。-`ω´-)")
                    else:
                        mc = "╔══[ รายชื่อคนพิมตาม ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+nadya.getContact(mi_d).displayName
                        nadya.sendReplyMessage(msg.id, msg.to, mc + "\n╚══[ 🔝ƬΣΛM✍️ŦЂềƒÎάŠħ⚡]")
                    
                elif "/พิมตาม" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบพิมตามเรียบร้อย(。-`ω´-)")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบพิมตามเรียบร้อย(。-`ω´-)")
#==============================================================================#
                elif text.lower() == '.เชคแอด':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':GS}, contentType=13)
                elif text.lower() == '.ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ID Group 」\n•" + gid.id)
                elif text.lower() == '.รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                elif text.lower() == '.ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 Name Group 」\n•" + gid.name)
                elif text.lower() == '.รายชื่อสมาชิก':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "รายชื่อสมชิกกลุ่ม"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n จำนวนสมาชิก {} คน(。-`ω´-) ".format(str(len(group.members)))
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                elif text.lower() == '.รายชื่อกลุ่ม':
                  if msg._from in admin:
                      groups = nadya.groups
                      ret_ = "รายชื่อกลุ่ม"
                      no = 0 + 1
                      for gid in groups:
                          group = nadya.getGroup(gid)
                          ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                          no += 1
                      ret_ += "\n จำนวนกลุ่ม {} กลุ่ม(。-`ω´-)".format(str(len(groups)))
                      nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                      
                elif text.lower() == '.ข้อมูลกลุ่ม':
                    group = nadya.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้าง"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ลิ้งถูกปิดอยู่.."
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(nadya.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลกลุ่ม ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีกลุ่ม:{}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ สมาชิกกลุ่ม : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ กลุ่มตั๋ว:{}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                    nadya.sendImageWithURL(to, path)

               elif text.lower() == '.ลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendReplyMessage(msg.id, msg.to, "「 Group 」\n• https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendReplyMessage(msg.id, msg.to, "กรุณาเปิดลิ้งกลุ่มก่อนลงคำสั่งนี้ด้วยครับ(。-`ω´-)".format(str(settings["keyCommand"])))

                elif text.lower() == '/ลิ้ง on':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มเปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendReplyMessage(msg.id, msg.to, "เปิดลิ้งกลุ่มเรียบร้อย(。-`ω´-)")

                elif text.lower() == '/ลิ้ง off':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มปิดเรียบร้อย(。-`ω´-)")

#==============================================================================#          
                elif msg.text in ["Tag","tagall","แทค","แทก","Tagall","tag"]:
                    members = []
                    if msg.toType == 1:
                        room = nadya.getCompactRoom(to)
                        members = [mem.mid for mem in room.contacts]
                    elif msg.toType == 2:
                          group = nadya.getCompactGroup(to)
                          members = [mem.mid for mem in group.members]
                    else:
                          return nadya.sendReplyMessage(msg.id, msg.to, '「 TAG 」 • ERROR')
                    if members:
                          mentionMembers2(to, members)
                          
                elif text.lower() == '/เปิดอ่าน on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                nadya.sendReplyMessage(msg.id, msg.to, "เปิดหาคนซุ่ม(。-`ω´-)")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            nadya.sendReplyMessage(msg.id, msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == '/เปิดอ่าน off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        nadya.sendReplyMessage(msg.id, msg.to, "ปิดหาคนซุ่ม(。-`ω´-)")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        nadya.sendReplyMessage(msg.id, msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == '/เปิดอ่าน reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        nadya.sendReplyMessage(msg.id, msg.to, "Reset reading point:\n" + readTime)
                    else:
                        nadya.sendReplyMessage(msg.id, msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == '.อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            nadya.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = nadya.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            nadya.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        nadya.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
            elif msg.text.lower().startswith(".พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    nadya.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
            elif msg.contentType == 1:
              if settings["changePictureProfile"] == True:
                  path = nadya.downloadObjectMsg(msg_id)
                  settings["changePictureProfile"] = False
                  nadya.updateProfilePicture(path)
                  nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนโปรไฟล์สำเร็จแล้ว(。-`ω´-)")

#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != nadya.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                
                if settings["autoRead"] == True:
                    nadya.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        nadya.sendMessage(msg.to,text)

#==============================================================================#
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
