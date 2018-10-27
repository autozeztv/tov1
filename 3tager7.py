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
supperadmin=["ue9781edcd4eecd9abfd6e50fc3ea95b1",nadyaMID]
admin=["ue9781edcd4eecd9abfd6e50fc3ea95b1","u740dc5b30c38810eadb7251ecd3b40b6","uad73a8119f2accea9e8f39e39291ac9a","uf70dcd1cf3349a7f3d8d05e99a5fb081",nadyaMID]
Family=["ue9781edcd4eecd9abfd6e50fc3ea95b1","u740dc5b30c38810eadb7251ecd3b40b6","uad73a8119f2accea9e8f39e39291ac9a","uf70dcd1cf3349a7f3d8d05e99a5fb081",nadyaMID]
RfuFamily = RfuBot + Family
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
myMid = nadya.profile.mid
read = json.load(readOpen)
settings = json.load(settingsOpen)
msg_dict = {}
msg_image={}
msg_video={}
msg_sticker={}
unsendchat = {}
temp_flood = {}
wbanlist = []
wblacklist = []
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
pson = {"kw":{}}

settings = {
    "autoRead": True,
    "unsend": True,
    "acommentOn": False,
    "Wc": False,
    "bcommentOn": False,
    "autoLeave": False,
    "autoJoin": True,
    "autoAdd": True,
    "autoBlock": False,
    "autoJoinTicket": True, 
    "server":"VPS",
    "acomment":"「 ตอนรับเข้า 」\n•สวัสดี",
    "bcomment":"「 ตอนรับออก 」\n•บาย",
    "JoinMessage":"「 ข้อความเข้ากลุ่ม 」\n• 􀨁􀄕ขวา􏿿ขอบคุณที่เชิญสามาชิกเข้ากลุ่ม\n􀠁􀄭hi􏿿สามารถเล่น selfbot-tag ได้ 􀄃􀉕ตกลง􏿿\n􀔃􀅭มอง􏿿โดยพิม help เพื่อใช้คำสั่ง􀜅􀄔หล่อ􏿿",
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
    "addPesan": "@",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " @",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "52002736",
                "STKPKGID": "11537",
                "STKVER": "1"
            },
            "leaveSticker": {
                "STKID": "51626516",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "51626501",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "readerSticker": {
                "STKID": "13188540",
                "STKPKGID": "1327110",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "51626504",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "52002734",
                "STKPKGID": "11537",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
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

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nadya.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        nadya.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

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

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    nadya.sendMessage(to, '', contentMetadata, 7)
    
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
    helpMessage =  "╔═══════════════" + "\n" + \
                  "║สปีด➥เช็คความเร็วบอท" + "\n" \
                  "║เชคค่า➥เช็คการตั้งค่าบอท" + "\n" \
                  "║เชคแอด➥เช็คคนสร้างกลุ่ม" + "\n" \
                  "║ชื่อกลุ่ม➥แสดงชื่อกลุ่ม" + "\n" \
                  "║รูปกลุ่ม➥แสดงรูปกลุ่ม" + "\n" \
                  "║ไอดีกลุ่ม➥เช็คไอดีกลุ่ม" + "\n" \
                  "║รายชื่อสมาชิก➥ชื่อสมาชิกกลุ่ม" + "\n" \
                  "║ทีมงาน➥คนทำบอทและพัฒนา" + "\n" \
                  "║คท➥ ส่งคท " + "\n" \
                  "║มิด➥ ส่งมิด " + "\n" \
                  "║ชื่อ➥ ส่งชื่อ " + "\n" \
                  "║ตัส➥ ส่งตัส " + "\n" \
                  "║รูป➥ ส่งรูป " + "\n" \
                  "║ข้อมูล @➥จะส่งข้อมูลคนที่แท็ก" + "\n" \
                  "║!แทค➥แท็กคนใส่ชื่อร่องหน" + "\n" \
                  "║!มิด➥หามิดคนใส่ชื่อร่องหน" + "\n" \
                  "║!คท➥ส่งคอนแท็กคนใส่ร่องหน" + "\n" \
                  "║เปิดอ่าน➥เปิดหาคนซุ่ม" + "\n" \
                  "║อ่าน➥แสดงชื่อคนซุ่ม" + "\n" \
                  "║กูเกิล (ข้อความ)➥ค้นหาต่างๆ" + "\n" \
                  "║ยูทูป (ข้อความ)➥ค้นหาต่างๆ" + "\n" \
                  "║ขอลิ้งกลุ่ม➥ขอลิ้งกลุ่มนี้" + "\n" \
                  "║ลิ้งกลุ่ม เปิด/ปิด➥เปิดปิดลิ้งกลุ่ม" + "\n" \
                  "║ของขวัญ1-2➥ ส่งของขวัญ" + "\n" \
                  "╚═══════════════"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   ".ข้างหน้าแทน-ทั้งหมด" + "\n " \
                         " " + "\n" \
                         "-เตะ @" + "\n" + \
                         "-ออก" + "\n" \
                         "-ยกเลิก" + "\n" + \
                         "-ลบรัน" + "\n" + \
                         "-โทร(เลข)" + "\n" + \
                         "-ชื่อ:(ชื่อ)" + "\n" + \
                         "-ตัส:(ตัส)" + "\n" + \
                         "-ชื่อกลุ่ม:(ชื่อ)" + "\n" + \
                         "-เปลี่ยนรูป" + "\n" + \
                         "-รายชื่อกลุ่ม" + "\n" + \
                         "-/mic (มิด)" + "\n" + \
                         "-/token" + "\n" + \
                         " " + "\n" + \
                         "-opad @" + "\n" + \
                         "-deopad @" + "\n" + \
                         "-oplistad @" + "\n" + \
                         "-opsu @" + "\n" + \
                         "-deopsu @" + "\n" + \
                         "-oplistsu @" + "\n" + \
                         " " + "\n" + \
                         "-ยกเลิก on\off" + "\n" + \
                         "-เข้ากลุ่ม on\off" + "\n" + \
                         "-ออกกลุ่ม on\off" + "\n" + \
                         "-ตอนรับเข้า on\off" + "\n" + \
                         "-ตอนรับออก on\off" + "\n" + \
                         "-ตั้งเข้า:" + "\n" + \
                         "-ตั้งออก:" + "\n" + \
                         "-ตั้งเข้ากลุ่ม:" + "\n" + \
                         "-เชคเข้า" + "\n" + \
                         "-เชคออก" + "\n" + \
                         "-เชคเข้ากลุ่ม" + "\n" + \
                         " "+ "\n" + \
                         "**คำสั่งเฉพาะแอดมิน**"
    return helpTextToSpeech
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTOBLOCK") 
            if settings ['autoBlock'] == True:
                nadya.blockContact(op.param1)
                      
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTOADD")
            if settings["autoAdd"] == True:
                nadya.sendMessage(op.param1, "สวัสดีครับ {} ขอบคุณที่แอดเข้ามานะครับ(。-`ω´-)".format(str(nadya.getContact(op.param1).displayName)))

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE INTO GROUP")
            if settings["autoJoin"] and nadyaMID in op.param3:
                nadya.acceptGroupInvitation(op.param1)
                nadya.sendMention(op.param1, settings["JoinMessage"], [op.param2])

        if op.type == 15:
            if settings["bcommentOn"] and "bcomment" in settings:
                h = nadya.getContact(op.param2)
                nadya.sendMessage(op.param1,nadya.getContact(op.param2).displayName + "\n\n" + settings["bcomment"])
                nadya.sendContact(op.param1, op.param2)
                nadya.sendMessageMusic(op.param1, op.param2) 
                nadya.sendMessage(op.param1,"「 ไอดี 」\n•" +  op.param2)
                nadya.sendMessage(op.param1,"「 ชื่อ 」\n•" + nadya.getContact(op.param2).displayName)
                nadya.sendMessage(op.param1,"「 ตัส 」\n•\n" + nadya.getContact(op.param2).statusMessage)
                nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + nadya.getContact(op.param2).pictureStatus)
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["Wc"] == True:
                group = nadya.getGroup(op.param1)
                contact = nadya.getContact(op.param2)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 17:
            if settings["acommentOn"] and "acomment" in settings:
                cnt = nadya. getContact(op.param2)
                h = nadya.getContact(op.param2)
                nadya.sendMessage(op.param1,cnt.displayName + "\n\n" + settings["acomment"])
                nadya.sendContact(op.param1, op.param2)
                nadya.sendMessageMusic(op.param1, op.param2)
                nadya.sendMessage(op.param1,"「 ไอดี 」\n•" +  op.param2)
                nadya.sendMessage(op.param1,"「 ชื่อ 」\n•" + nadya.getContact(op.param2).displayName)
                nadya.sendMessage(op.param1,"「 ตัส 」\n•\n" + nadya.getContact(op.param2).statusMessage)
                nadya.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + nadya.getContact(op.param2).pictureStatus)

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
                if "/ti/g/" in msg.text.lower():
                     if settings["autoJoinTicket"] == True:
                         link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                         links = link_re.findall(text)
                         n_links = []
                         for l in links:
                             if l not in n_links:
                                 n_links.append(l)
                         for ticket_id in n_links:
                             group = nadya.findGroupByTicket(ticket_id)
                             nadya.acceptGroupInvitationByTicket(group.id,ticket_id)
                             nadya.sendReplyMessage(msg.id, msg.to, "「 NameGroup 」\n•  %s " % str(group.name))
        if op.type == 26:
            msg = op.message
            if msg.text is None:
                return
            try:
                if pson["kw"][msg.text]:
                    nadya.sendMessage(msg.to,str(pson["kw"][str(msg.text)]))
            except Exception as Error:
                pass
#==============================================================================#
                if msg.text in ["คำสั่ง","Help","help","/Help","/help"]:
                    helpMessage = helpmessage()
                    nadya.sendReplyMessage(msg.id, msg.to, str(helpMessage))
                if msg.text in [".คำสั่ง2","คำสั่ง2","Help2","help2","/Help2","/help2"]:
                  if msg._from in admin:
                         helpTextToSpeech = helptexttospeech()
                         nadya.sendReplyMessage(msg.id, msg.to, str(helpTextToSpeech))
#==============================================================================#

                if ".ชื่อ: " in msg.text:
                 if msg._from in supperadmin:
                     spl = re.split(".ชื่อ: ",msg.text,flags=re.IGNORECASE)
                     if spl[0] == "":
                        prof = nadya.getProfile()
                        prof.displayName = spl[1]
                        nadya.updateProfile(prof)
                        nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนชื่อสำเร็จแล้ว(。-`ω´-)")

                if ".ตัส: " in msg.text:
                 if msg._from in supperadmin:
                     spl = re.split(".ตัส: ",msg.text,flags=re.IGNORECASE)
                     if spl[0] == "":
                        prof = nadya.getProfile()
                        prof.statusMessage = spl[1]
                        nadya.updateProfile(prof)
                        nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนตัสสำเร็จแล้ว(。-`ω´-)")

                if ".ชื่อกลุ่ม: " in msg.text:
                  if msg._from in supperadmin:
                      if msg.toType == 2:
                          X = nadya.getGroup(msg.to)
                          X.name = msg.text.replace(".ชื่อกลุ่ม: ","")
                          nadya.updateGroup(X)
                      else:
                          nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อกลุ่ม 」\n• เกิดข้อผิดพลาด")

                if text.lower() == ".เปลี่ยนรูป":
                  if msg._from in supperadmin:
                      settings["changePictureProfile"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "ส่งรูปมา(。-`ω´-)")

#==============================================================================#
                if msg.text.lower().startswith(".เตะ "):
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                  for target in targets:
                        try:
                            nadya.kickoutFromGroup(msg.to,[target])
                            nadya.sendReplyMessage(msg.id, msg.to, "「 เตะ 」\n• เสร็จสิ้น")
                        except:
                            nadya.sendReplyMessage(msg.id, msg.to, "「 เตะ 」\n• เกิดข้อผิดพลาด")
                if text.lower() == 'เชคค่า':
                    try:
                        ret_ = "╔════════════"
                        if settings["autoJoin"] == True: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✔"
                        else: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✘"
                        if settings["autoRead"] == True: ret_ += "\n║ ระบบเข้าอ่านออโต้ ✔"
                        else: ret_ += "\n║ ระบบเข้าอ่านออโต้ ✘"
                        if settings["autoLeave"] == True: ret_ += "\n║ ระบบออกกลุ่มออโต้  ✔"
                        else: ret_ += "\n║ ระบบออกกลุ่มออโต้ ✘"
                        if settings["acommentOn"] == True: ret_ += "\n║ ระบบตอนรับคนเข้ากลุ่ม ✔"
                        else: ret_ += "\n║ ระบบตอนรับคนเข้ากลุ่ม ✘"
                        if settings["bcommentOn"] == True: ret_ += "\n║ ระบบตอนรับคนออกกลุ่ม ✔"
                        else: ret_ += "\n║ ระบบตอนรับคนออกกลุ่ม ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\n║ ระบบเข้ากลุ่มผ่านลิ้ง ✔"
                        else: ret_ += "\n║ ระบบเข้ากลุ่มผ่านลิ้ง ✘"
                        if settings["unsend"] == True: ret_ += "\n║ ระบบเช็คยกเลิกข้อความ ✔"
                        else: ret_ += "\n║ ระบบเช็คยกเลิกข้อความ ✘"
                        ret_ += "\n╚════════════"
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                    except Exception as e:
                        nadya.sendReplyMessage(msg.id, msg.to, str(e))

                if ".ยกเลิก" == msg.text.lower():
                  if msg._from in admin:
                         if msg.toType == 2:
                             group = nadya.getGroup(msg.to)
                             gMembMids = [contact.mid for contact in group.invitee]
                         for _mid in gMembMids:
                             nadya.cancelGroupInvitation(msg.to,[_mid])
                             nadya.sendReplyMessage(msg.id, msg.to,  "「 ยกเลิกค้างเชิญ 」\n• เสร็จสิ้น")
#==============================================================================# 
                if "ยูทูป" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "ผมการค้นหาจาก ยูทูป\n\n"
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

                if "กูเกิล " in msg.text.lower():
                    spl = re.split("กูเกิล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        nadya.sendReplyMessage(msg.id, msg.to, "กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        nadya.sendReplyMessage(msg.id, msg.to, msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก กูเกิล:\n\n"
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

                if "google " in msg.text.lower():
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

                if "youtube" in msg.text.lower():
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
                            
#==============================================================================#

                if text.lower() == '.ลบรัน':
                  if msg._from in admin:
                      gid = nadya.getGroupIdsInvited()
                      start = time.time()
                      for i in gid:
                          nadya.rejectGroupInvitation(i)
                      elapsed_time = time.time() - start
                      nadya.sendReplyMessage(msg.id, msg.to, "「 กำลังลบค้างเชิญ 」")
                      nadya.sendReplyMessage(msg.id, msg.to, "• ใช้เวลาไป: %s วินาที" % (elapsed_time))

                if msg.text in [".เตะหมด"]:
                  if msg._from in supperadmin:
                    if msg.toType == 2:
                        group = nadya.getGroup(msg.to)                    
                        groupname = "ไม่มีสามาชิกในห้องแชท"
                        if len(groupname) <= 50:
                            group1 = nadya.getGroup(to)
                            group1.name = groupname
                            name = [contact.displayName for contact in group.members]
                        for i in name:
                            nadya.sendMessage(msg.to, "ฮิโตชิ ลบ " + i + " ออกจากกลุ่ม")
                        nadya.sendMessage(msg.to, "ฮิโตชิ ลบคุณออกจากกลุ่ม")
                        nadya.updateGroup(group1)

                if ".โทร" in msg.text.lower():
                  if msg._from in admin:
                      if msg.toType == 2:
                          sep = text.split(" ")
                          strnum = text.replace(sep[0] + " ","")
                          num = int(strnum)
                          nadya.sendReplyMessage(msg.id, msg.to, "「 สแปมคอล 」\n• เสร็จสิ้น")
                      for var in range(0,num):
                          group = nadya.getGroup(to)
                          members = [mem.mid for mem in group.members]
                          nadya.acquireGroupCallRoute(to)
                          nadya.inviteIntoGroupCall(to, contactIds=members)

                if text.lower() == '.ออก':
                  if msg._from in admin:
                      if msg.toType == 2:
                          ginfo = nadya.getGroup(to)
                          try:
                              nadya.sendReplyMessage(msg.id, msg.to, "「 ออกกลุ่ม 」\n• เสร็จสิ้น ")
                              nadya.leaveGroup(to)
                          except:
                             pass

                if "ทีมงาน" == msg.text.lower():
                    msg.contentType = 13
                    nadya.sendReplyMessage(msg.id, msg.to, "「 BOT TEAM 」 • H0ck ")
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':'ue9781edcd4eecd9abfd6e50fc3ea95b1'}, contentType=13) 
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':'uad73a8119f2accea9e8f39e39291ac9a'}, contentType=13) 
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':'u740dc5b30c38810eadb7251ecd3b40b6'}, contentType=13)
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':'uf70dcd1cf3349a7f3d8d05e99a5fb081'}, contentType=13)
                    
                if msg.text in ["Speed","speed","Sp","sp",".Sp",".sp",".Speed",".speed","\Sp","\sp","\speed","\Speed","สปีด"]:
                    start = time.time()
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ความเร็ว 」")
                    elapsed_time = time.time() - start
                    nadya.sendReplyMessage(msg.id, msg.to, "[ %s วินาที ]\n[ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")

                if msg.text in ["ออน",".ออน","\ออน",".uptime",".Uptime"]:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ออนไลน์ 」\n•{}".format(str(runtime)))

                if msg.text in ["คท",".คท","Me","me",".Me",".me"]:
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':sender}, contentType=13)
                    nadya.sendMentionFooter(to, '「 ผู้ใช้งาน 」\n•', sender, "https://line.me/ti/p/~hietocih", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~hietocih', 'type': 'mt', 'subText': "「 BOT TEAM 」 • H1ck", 'a-installUrl': 'https://line.me/ti/p/~hietocih', 'a-installUrl': ' https://line.me/ti/p/~hietocih', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~hietocih', 'i-linkUri': 'https://line.me/ti/p/~hietocih', 'id': 'mt000000000a6b79f9', 'text': '「 BOT TEAM 」 • H1ck', 'linkUri': 'https://line.me/ti/p/~hietocih'}, contentType=19)

                if msg.text in ["ไอดี","Mid","mid","MID","มิด"]:
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ไอดี 」\n•" +  sender)

                if msg.text in ["ชื่อ","เนม"]:
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อ 」\n•" + nadya.getContact(sender).displayName)

                if msg.text in ["ตัส","สถานะ"]:
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ตัส 」\n•\n" + nadya.getContact(sender).statusMessage)

                if msg.text in ["รูป","ดิส","โปรไฟล์"]:
                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + nadya.getContact(sender).pictureStatus)

                if msg.text in ["/token"]:
                  if msg._from in admin:
                      nadya.sendReplyMessage(msg.id, msg.to, nadya.authToken)

                if "/mic " in msg.text:
                  if msg._from in admin:
                      mmid = msg.text.replace("/mic ","")
                      nadya.sendReplyMessage(msg.id, msg.to, text=None, contentMetadata={'mid': mmid}, contentType=13)

                if text.lower() == 'ของขวัญ1':
                  nadya.sendGift(msg.to,'608','sticker')
							
                if text.lower() == 'ของขวัญ2':
                  nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'PRDID': '88efc1ed-744d-4704-a77a-bb79077f5d22','PRDTYPE': 'THEME','MSGTPL': '100'}, contentType = 9)
                  
                if msg.text in ["Tag","tagall","แทค","แทก","Tagall","tag"]:
                    members = []
                    if msg.toType == 1:
                        room = nadya.getCompactRoom(to)
                        members = [mem.mid for mem in room.contacts]
                    elif msg.toType == 2:
                          group = nadya.getCompactGroup(to)
                          members = [mem.mid for mem in group.members]
                    else:
                          return nadya.sendReplyMessage(msg.id, msg.to, '「 แทค 」\n• เกิดข้อผิดพลาด')
                    if members:
                          mentionMembers2(to, members)
#==============================================================================#
                if text.lower().startswith('.opad '):
                  if msg._from in supperadmin:
                      MENTION = eval(msg.contentMetadata['MENTION'])
                      inkey = MENTION['MENTIONEES'][0]['M']
                      admin.append(str(inkey))
                      nadya.sendReplyMessage(msg_id,to, "เพิ่มสิทธิ์เรียบร้อยแล้ว(。-`ω´-)")
                if text.lower().startswith('.deopad '):
                  if msg._from in supperadmin:
                      MENTION = eval(msg.contentMetadata['MENTION'])
                      inkey = MENTION['MENTIONEES'][0]['M']
                      admin.remove(str(inkey))
                      nadya.sendReplyMessage(msg_id,to, "ลบสิทธิ์เรียบร้อยแล้ว(。-`ω´-)")
                if text.lower() == '.oplistad':
                  if msg._from in supperadmin:
                    if admin == []:
                        nadya.sendReplyMessage(msg_id,to, "ไม่มีอำนาจ(。-`ω´-)")
                    else:
                        nadya.sendReplyMessage(msg_id,to, "ต่อไปนี้เป็นผู้ตรวจสอบ(。-`ω´-)")
                        mc = ""
                        for mi_d in admin:
                            mc += "┏━━━━━━━━━━━┓\n" + "↠" + nadya.getContact(mi_d).displayName + "\n┗━━━━━━━━━━━┛\n"
                        nadya.sendReplyMessage(msg_id,to, mc)
                        
                if text.lower().startswith('.opsu '):
                  if msg._from in supperadmin:
                      MENTION = eval(msg.contentMetadata['MENTION'])
                      inkey = MENTION['MENTIONEES'][0]['M']
                      supperadmin.append(str(inkey))
                      nadya.sendReplyMessage(msg_id,to, "เพิ่มสิทธิ์เรียบร้อยแล้ว(。-`ω´-)")
                if text.lower().startswith('.deopsu '):
                  if msg._from in supperadmin:
                      MENTION = eval(msg.contentMetadata['MENTION'])
                      inkey = MENTION['MENTIONEES'][0]['M']
                      supperadmin.remove(str(inkey))
                      nadya.sendReplyMessage(msg_id,to, "ลบสิทธิ์เรียบร้อยแล้ว(。-`ω´-)")
                if text.lower() == '.oplistsu':
                  if msg._from in supperadmin:
                    if supperadmin == []:
                        nadya.sendReplyMessage(msg_id,to, "ไม่มีอำนาจ(。-`ω´-)")
                    else:
                        nadya.sendReplyMessage(msg_id,to, "ต่อไปนี้เป็นผู้ตรวจสอบ(。-`ω´-)")
                        mc = ""
                        for mi_d in supperadmin:
                            mc += "┏━━━━━━━━━━━┓\n" + "↠" + nadya.getContact(mi_d).displayName + "\n┗━━━━━━━━━━━┛\n"
                        nadya.sendReplyMessage(msg_id,to, mc)
#==============================================================================#

                if msg.text.lower().startswith("ข้อมูล "):
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
                                    nadya.sendMentionFooter(to, '「 ผู้ใช้งาน 」\n•', sender, "https://line.me/ti/p/~hietocih", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~hietocih', 'type': 'mt', 'subText': "「 BOT TEAM 」 • H1ck", 'a-installUrl': 'https://line.me/ti/p/~hietocih', 'a-installUrl': ' https://line.me/ti/p/~hietocih', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~hietocih', 'i-linkUri': 'https://line.me/ti/p/~hietocih', 'id': 'mt000000000a6b79f9', 'text': '「 BOT TEAM 」 • H1ck', 'linkUri': 'https://line.me/ti/p/~hietocih'}, contentType=19)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ไอดี 」\n•" +  ls)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อ 」\n•" +  me.displayName)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ตัส 」\n•\n" +  me.statusMessage)
                                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    nadya.sendImageWithURL(to, str(path))
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    nadya.sendReplyMessage(msg.id, msg.to, text=None, contentMetadata={'mid': ls}, contentType=13)
                                    nadya.sendMentionFooter(to, '「 ผู้ใช้งาน 」\n•', sender, "https://line.me/ti/p/~hietocih", "http://dl.profile.line-cdn.net/"+nadya.getContact(sender).pictureStatus, nadya.getContact(sender).displayName);nadya.sendMessage(to, nadya.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+nadya.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~hietocih', 'type': 'mt', 'subText': "「 BOT TEAM 」 • H1ck", 'a-installUrl': 'https://line.me/ti/p/~hietocih', 'a-installUrl': ' https://line.me/ti/p/~hietocih', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~hietocih', 'i-linkUri': 'https://line.me/ti/p/~hietocih', 'id': 'mt000000000a6b79f9', 'text': '「 BOT TEAM 」 • H1ck', 'linkUri': 'https://line.me/ti/p/~hietocih'}, contentType=19)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ไอดี 」\n•" +  ls)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อ 」\n•" +  me.displayName)
                                    nadya.sendReplyMessage(msg.id, msg.to, "「 ตัส 」\n•\n" +  me.statusMessage)
                                    nadya.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    nadya.sendImageWithURL(to, str(path))
                                    nadya.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")

                if text.lower() == '!แทค':
                    gs = nadya.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อล่องหน 」\n• ไม่มีชื่อนี้ในกลุ่ม")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        nadya.sendMessage(to, mc)

                if text.lower() == '!มิด':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อล่องหน 」\n• ไม่มีชื่อนี้ในกลุ่ม")
                    else:
                        mc = "「 ไอดี 」\n• "
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        nadya.sendReplyMessage(msg.id, msg.to, mc)

                if text.lower() == '!คท':
                    gs = nadya.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อล่องหน 」\n• ไม่มีชื่อนี้ในกลุ่ม")
                    else:
                        for ls in lists:
                            contact = nadya.getContact(ls)
                            mi_d = contact.mid
                            nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':mi_d}, contentType=13)

                if text.lower() == 'ขอลิ้งกลุ่ม':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = nadya.reissueGroupTicket(to)
                            nadya.sendReplyMessage(msg.id, msg.to, "「 ลิ้งกลุ่ม 」\n• https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            nadya.sendReplyMessage(msg.id, msg.to, "กรุณาเปิดลิ้งกลุ่มก่อนลงคำสั่งนี้ด้วยครับ(。-`ω´-)".format(str(settings["keyCommand"])))

                if text.lower() == 'ลิ้งกลุ่ม เปิด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มเปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = False
                            nadya.updateGroup(group)
                            nadya.sendReplyMessage(msg.id, msg.to, "เปิดลิ้งกลุ่มเรียบร้อย(。-`ω´-)")

                if text.lower() == 'ลิ้งกลุ่ม ปิด':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = True
                            nadya.updateGroup(group)
                            nadya.sendReplyMessage(msg.id, msg.to, "ลิ้งกลุ่มปิดเรียบร้อย(。-`ω´-)")

#==============================================================================#
                if text.lower() == 'เชคแอด':
                    group = nadya.getGroup(to)
                    GS = group.creator.mid
                    nadya.sendReplyMessage(msg_id,to, None, contentMetadata={'mid':GS}, contentType=13)
                if text.lower() == 'ไอดีกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ไอดีกลุ่ม 」\n•" + gid.id)
                if text.lower() == 'รูปกลุ่ม':
                    group = nadya.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    nadya.sendImageWithURL(to, path)
                if text.lower() == 'ชื่อกลุ่ม':
                    gid = nadya.getGroup(to)
                    nadya.sendReplyMessage(msg.id, msg.to, "「 ชื่อกลุ่ม 」\n•" + gid.name)
                if text.lower() == 'รายชื่อสมาชิก':
                    if msg.toType == 2:
                        group = nadya.getGroup(to)
                        ret_ = "รายชื่อสมชิกกลุ่ม"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n จำนวนสมาชิก {} คน(。-`ω´-) ".format(str(len(group.members)))
                        nadya.sendReplyMessage(msg.id, msg.to, str(ret_))
                if text.lower() == '.รายชื่อกลุ่ม':
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
#=================THEFLASH====================================================#

                if msg.text.lower() == ".ตั้งติ๊กเข้า":
                 if msg._from in admin:
                    settings["messageSticker"]["addStatus"] = True
                    settings["messageSticker"]["addName"] = "welcomeSticker"
                    nadya.sendReplyMessage(msg.id, msg.to, "ส่งสติกเกอรที่จะตั้งลงมา")
                if msg.text.lower() == ".ลบติ๊กเข้า":
                 if msg._from in admin:
                    settings["messageSticker"]["listSticker"]["welcomeSticker"] = None
                    nadya.sendReplyMessage(msg.id, msg.to, "ลบสติกเกอรคนเข้าแล้ว")

                if text.lower() == '.อ่านออโต้ on':
                  if msg._from in admin:
                      settings["autoRead"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดโหมดอ่านอัตโนมัติ(。-`ω´-)")
                if text.lower() == '.อ่านออโต้ off':
                  if msg._from in admin:
                      settings["autoRead"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดโหมดอ่านอัตโนมัติ(。-`ω´-)")

                if text.lower() == '.ยกเลิก on':
                  if msg._from in admin:
                      settings["unsend"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดเช็คยกเลิกข้อความ(。-`ω´-)")
                if text.lower() == '.ยกเลิก off':
                  if msg._from in admin:
                      settings["unsend"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดเช็คยกเลิกข้อความ(。-`ω´-)") 

                if text.lower() == '.มุด on':
                  if msg._from in admin: 
                      settings["autoJoinTicket"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบมุดลิ้ง(。-`ω´-)")
                if text.lower() == '.มุด off':
                  if msg._from in admin:
                      settings["autoJoinTicket"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบมุดลิ้ง(。-`ω´-)")

                if text.lower() == '.ออโต้บล็อค on':
                  if msg._from in admin:
                      settings["autoBlock"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบออโต้บล็อค(。-`ω´-)")
                if text.lower() == '.ออโต้บล็อค off':
                  if msg._from in admin:
                      settings["autoBlock"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบออโต้บล็อค(。-`ω´-)")

                if text.lower() == '.แอดออโต้ on':
                  if msg._from in admin:
                      settings["autoAdd"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบแอดออโต้(。-`ω´-)")
                if text.lower() == '.แอดออโต้ off':
                  if msg._from in admin:
                      settings["autoAdd"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบแอดออโต้(。-`ω´-)")

                if text.lower() == '.เชคติ้ก on':
                  if msg._from in admin:
                      settings["checkSticker"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบเช็คสติ้กเกอร์(。-`ω´-)")
                if text.lower() == '.เชคติ้ก off':
                  if msg._from in admin:
                      settings["checkSticker"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบเช็คสติ้กเกอร์(。-`ω´-)")

                if text.lower() == '.เข้ากลุ่ม on':
                  if msg._from in admin:
                      settings["autoJoin"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")
                if text.lower() == '.เข้ากลุ่ม off':
                  if msg._from in admin:
                      settings["autoJoin"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")

                if text.lower() == '.ออกกลุ่ม on':
                  if msg._from in admin:
                      settings["autoLeave"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบออกกลุ่มออโต้(。-`ω´-)")
                if text.lower() == '.ออกกลุ่ม off':
                  if msg._from in admin:
                      settings["autoLeave"] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบออกกลุ่มออโต้(。-`ω´-)")

                if msg.text.lower() ==  '.ตอนรับเข้า on':
                  if msg._from in admin:
                      settings['acommentOn'] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบตอนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")
                if msg.text.lower() ==  '.ตอนรับเข้า off':
                  if msg._from in admin:
                      settings['acommentOn'] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบตอนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")

                if msg.text.lower() == '.ตอนรับออก on':
                  if msg._from in admin:
                      settings["bcommentOn"] = True
                      nadya.sendReplyMessage(msg.id, msg.to, "เปิดระบบตอนรับสมาชิกออกกลุ่ม(。-`ω´-)")
                if msg.text.lower() == '.ตอนรับออก off':
                  if msg._from in admin:
                      settings['bcommentOn'] = False
                      nadya.sendReplyMessage(msg.id, msg.to, "ปิดระบบตอนรับสมาชิกออกกลุ่ม(。-`ω´-)")

                if ".ตั้งเข้า:" in msg.text.lower():
                  if msg._from in admin:
                      c = msg.text.replace(".ตั้งเข้า:","")
                      if c in [""," ","\n",None]:
                         nadya.sendReplyMessage(msg.id, msg.to, "เกิดข้อผิดพลาด(。-`ω´-)")
                      else:
                         settings["acomment"] = c
                         nadya.sendReplyMessage(msg.id, msg.to, "ตั้งค่าข้อความตอนรับเสร็จสิ้น(。-`ω´-)")

                if ".ตั้งออก:" in msg.text.lower():
                  if msg._from in admin:
                      c = msg.text.replace(".ตั้งออก:","")
                      if c in [""," ","\n",None]:
                          nadya.sendReplyMessage(msg.id, msg.to, "เกิดข้อผิดพลาด(。-`ω´-)")
                      else:
                         settings["bcomment"] = c
                         nadya.sendReplyMessage(msg.id, msg.to, "ตั้งค่าข้อความตอนรับออกเสร็จสิ้น(。-`ω´-)")

                if ".ตั้งเข้ากลุ่ม:" in msg.text.lower():
                  if msg._from in admin:
                      c = msg.text.replace(".ตั้งเข้ากลุ่ม:","")
                      if c in [""," ","\n",None]:
                         nadya.sendReplyMessage(msg.id, msg.to, "เกิดข้อผิดพลาด(。-`ω´-)")
                      else:
                         settings["JoinMessage"] = c
                         nadya.sendReplyMessage(msg.id, msg.to, "ตั้งค่าข้อความเข้ากลุ่มเสร็จสิ้น(。-`ω´-)")

                if msg.text in [".เชคเข้า"]:
                  if msg._from in admin:
                    nadya.sendReplyMessage(msg.id, msg.to, "เช็คข้อความตอนรับล่าสุด(。-`ω´-)" + "\n\n➤" + settings["acomment"])
                if msg.text in [".เชคออก"]:
                  if msg._from in admin:
                    nadya.sendReplyMessage(msg.id, msg.to, "เช็คข้อความตอนรับออกล่าสุด(。-`ω´-)" + "\n\n➤" + settings["bcomment"])
                if msg.text in [".เชคเข้ากลุ่ม"]:
                  if msg._from in admin:
                    nadya.sendReplyMessage(msg.id, msg.to, "เช็คข้อความเข้ากลุ่มล่าสุด(。-`ω´-)" + "\n\n➤" + settings["JoinMessage"])
#=================THEFLASH====================================================#
#==============================================================================#
                if msg.text.lower().startswith("พูด "):
                       sep = text.split(" ")
                       say = text.replace(sep[0] + " ","")
                       lang = 'th'
                       tts = gTTS(text=say, lang=lang)
                       tts.save("hasil.mp3")
                       nadya.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
                if text.lower() == 'เปิดอ่าน':
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
                if text.lower() == 'อ่าน':
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
                        nadya.sendMessage(receiver,"ก่อนจะพิมคำสั่งนี้กรุณา (เปิดอ่าน) ก่อนลงคำสั่งนี้(。-`ω´-)")
                       
            if msg.contentType == 1:
                if settings["changePictureProfile"] == True:
                    path = nadya.downloadObjectMsg(msg_id)
                    settings["changePictureProfile"] = False
                    nadya.updateProfilePicture(path)
                    nadya.sendReplyMessage(msg.id, msg.to, "เปลี่ยนโปรไฟล์สำเร็จแล้ว(。-`ω´-)")
                
            if msg.contentType == 7:
                if settings["messageSticker"]["addStatus"] == True:
                    name = settings["messageSticker"]["addName"]
                    if name != None and name in settings["messageSticker"]["listSticker"]:
                        settings["messageSticker"]["listSticker"][name] = {
                            "STKID": msg.contentMetadata["STKID"],
                            "STKVER": msg.contentMetadata["STKVER"],
                            "STKPKGID": msg.contentMetadata["STKPKGID"]
                        }
                        nadya.sendMessage(to, "เพิ่มสำเร็จแล้ว" + name)
                    settings["messageSticker"]["addStatus"] = False
                    settings["messageSticker"]["addName"] = None
                if settings["addSticker"]["status"] == True:
                    stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                    stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                    stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                    f = codecs.open('sticker.json','w','utf-8')
                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                    nadya.sendMessage(to, "เพิ่มสติ้กเกอร์เสร็จสิ้นแล้ว {}".format(str(settings["addSticker"]["name"])))
                    settings["addSticker"]["status"] = False
                    settings["addSticker"]["name"] = ""

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if settings["unsend"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"lokasi":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14:
                    if settings["unsend"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = nadya.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)

        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
              
               if pson["kw"][str(msg.text)]:
             #      user = nadya.Contact(msg._from)
                   nadya.sendMessage(msg.to,pson["kw"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != nadya.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.text is None:
                    return
                if msg.text.lower() == ".เชคapi":
                  if msg._from in admin:
                      lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                      for i in pson["kw"]:
                          lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(pson["kw"][i])+"\n"
                      nadya.sendMessage(msg.to,lisk)
                if msg.text.startswith(".ล้างapi "):
                  if msg._from in admin:
                      try:
                          delcmd = msg.text.split(" ")
                          getx = msg.text.replace(delcmd[0] + " ","")
                          del pson["kw"][getx]
                          nadya.sendMessage(msg.to, "คำตอบโต้ " + str(getx) + " ล้างแล้ว")
                          f=codecs.open('sb.json','w','utf-8')
                          json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                      except Exception as Error:
                          print(Error)
                if msg.text.startswith(".ตั้งapi "):
                  if msg._from in admin:
                      try:
                          delcmd = msg.text.split(" ")
                          get = msg.text.replace(delcmd[0]+" ","").split(":")
                          kw = get[0]
                          ans = get[1]
                          pson["kw"][kw] = ans
                          f=codecs.open('sb.json','w','utf-8')
                          json.dump(pson, f, sort_keys=True, indent=4, ensure_ascii=False)
                          nadya.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: " +str(ans))
                      except Exception as Error:
                          print(Error)

        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsend"] == True:
                at = op.param1
                msg_id = op.param2
                if msg_id in msg_dict:
                    ah = time.time()
                    ikkeh = nadya.getContact(msg_dict[msg_id]["from"])
                    if "text" in msg_dict[msg_id]:
                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                        waktumsg = format_timespan(waktumsg)
                        rat_ = "\nสปีด : {}".format(waktumsg)
                        rat_ += "\nข้อความ : {}".format(msg_dict[msg_id]["text"])
                        sendMention(at, ikkeh.mid, "╭────────────\n├ ตรวจพบข้อความยกเลิก\n╰────────────\n\nชื่อ :", str(rat_))
                        del msg_dict[msg_id]
                    else:
                        if "image" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nสปีด : {}".format(waktumsg)
                            rat_ += "\nรูป : "
                            nadya.sendMessage(at, "╭────────────\n├ ตรวจพบรูปภาพยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                            nadya.sendImage(at, msg_dict[msg_id]["image"])
                            del msg_dict[msg_id]
                        else:
                            if "video" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nสปีด : {}".format(waktumsg)
                                rat_ += "\nวีดีโอ : "
                                nadya.sendMessage(at, "╭────────────\n├ ตรวจพบวิดีโอยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                nadya.sendVideo(at, msg_dict[msg_id]["video"])
                                del msg_dict[msg_id]
                            else:
                                if "audio" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nสปีด : {}".format(waktumsg)
                                    rat_ += "\nเสียง : "
                                    nadya.sendMessage(at, "** พบการยกเลิกข้อความ **\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                    nadya.sendAudio(at, msg_dict[msg_id]["audio"])
                                    del msg_dict[msg_id]
                                else:
                                    if "sticker" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nสปีด : {}".format(waktumsg)
                                        rat_ += "\nสติ๊กเกอร์ :"
                                        nadya.sendMessage(at, "╭────────────\n├ ตรวจพบสติ้กเกอร์ยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                        nadya.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "mid" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nสปีด : {}".format(waktumsg)
                                            rat_ += "\nคอนแทค : "
                                            nadya.sendMessage(at, "╭────────────\n├ ตรวจพบข้อมูลผู้ติดต่อยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                            nadya.sendContact(at, msg_dict[msg_id]["mid"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "lokasi" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nสปีด : {}".format(waktumsg)
                                                rat_ += "\nตำแหน่ง :"
                                                nadya.sendMessage(at, "╭────────────\n├ ตรวจพบตำแหน่งยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                                nadya.sendLocation(at, msg_dict[msg_id]["lokasi"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "file" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nสปีด : {}".format(waktumsg)
                                                    rat_ += "\nไฟล์ : "
                                                    nadya.sendMessage(at, "╭────────────\n├ ตรวจพบไฟล์ยกเลิก\n╰────────────\n\nชื่อ : {}".format(str(ikkeh.displayName) + str(rat_)))
                                                    nadya.sendFile(at, msg_dict[msg_id]["file"])
                                                    del msg_dict[msg_id]
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
