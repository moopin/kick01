# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
from multiprocessing import Pool, Process
from googletrans import Translator

#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# ki = LINE()
# ki.log("Auth Token : " + str(ki.authToken))
# ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

# kk = LINE()
# kk.log("Auth Token : " + str(kk.authToken))
# kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

# kc = LINE()
# kc.log("Auth Token : " + str(kc.authToken))
# kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

# ke = LINE()
# ke.log("Auth Token : " + str(ke.authToken))
# ke.log("Timeline Token : " + str(ke.tl.channelAccessToken))


print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

# kiMID = ki.profile.mid
# kiProfile = ki.getProfile()
# kiSettings = ki.getSettings()

# kkMID = kk.profile.mid
# kkProfile = kk.getProfile()
# kkSettings = kk.getSettings()

# kcMID = kc.profile.mid
# kcProfile = kc.getProfile()
# kcSettings = kc.getSettings()

# keMID = kc.profile.mid
# keProfile = kc.getProfile()
# keSettings = kc.getSettings()


# oepoll = OEPoll(ke)
# oepoll = OEPoll(kc)
# oepoll = OEPoll(kk)
# oepoll = OEPoll(ki)
oepoll = OEPoll(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
lineMID = line.getProfile().mid
# kiMID = ki.getProfile().mid
# kkMID = kk.getProfile().mid
# kcMID = kc.getProfile().mid
# kcMID = ke.getProfile().mid
# bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["ucc3eaec7bee330c182fbdb2849f252a8",lineMID]
admin=['ucc3eaec7bee330c182fbdb2849f252a8',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
settings = {
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":5},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Nn": True,
    "Sd": True,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "welcome":"ตั้งข้อความคนเข้าด้วยคับพรี้ (｡◕‿◕｡)",
    "bye":"ตั้งข้อความคนออกด้วยคับพรี้ (｡◕‿◕｡)",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"บัญชีผู้ไช้นี้ ถูกป้องกันโดย VąŁķỳŗįè тєάм ңάĉќ ระบบได้บล็อคคุณ อัตโนมัติ (｡◕‿◕｡)",
    "comment":"AUTOLIKE В¥.VąŁķỳŗįè тєάм ңάĉќ",
    "Respontag":"ตั้งข้อความตอบแทคด้วยคับพรี้ (｡◕‿◕｡)",
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
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":True,
    "copy2":True,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
#dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","Kick","!kickall","nuke","บิน","Kick","กระเด็น","หวด","เซลกากจัง","เตะ",".","ปลิว"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
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
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))



def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[ŚẾL₣ВΌŦแท็ค {} คน]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ชื่อกลุ่ม{} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log(" Nut " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp =      "  ─┅═✥ŚẾL₣ВΌŦ LÍŇỀ✥═┅─ "+ "  \n" + \
                  "╔══════════════════ "+ "\n" + \
                  "╠⚛คำสั่ง➠ ชุดคำสั่งที่1 "+ "  \n" + \
                  "╠⚛คำสั่ง2➠ ชุดคำสั่งที่2 "+ "  \n" + \
                  "╠⚛คำสั่ง3➠ ชุดคำสั่งที่ 3 "+ "  \n" + \
                  "╠⚛เช็ค➠ เช็คการตั้งค่า "+ "  \n" + \
                  "╠⚛รีบอท➠ รีสตารท์บอท "+ "  \n" + \
                  "╠⚛บอทออน➠เช็คเวลาบอทออน "+ "  \n" + \
                  "╠⚛Sp/Speed➠เช็คความเร็ว "+ "  \n" + \
                  "╠⚛ข้อมูล➠ เช็คข้อมูลคุณ "+ "  \n" + \
                  "╠⚛Creator➠เช็คผส.บอท "+ "  \n" + \
                  "╠⚛Self off ➠ ปิดบอท "+" \n" +\
                  "╠⚛Me ➠ คอทแท็ค "+ "  \n" + \
                  "╠⚛Mid ➠midเรา "+ "  \n" + \
                  "╠⚛ชื่อ ➠ ชื่อเรา "+ "  \n" + \
                  "╠⚛ตัส ➠ ตัสเรา "+ "  \n" + \
                  "╠⚛รูป ➠รูปเรา "+ "  \n" + \
                  "╠⚛รูปปก ➠ ปกเรา "+ "  \n" + \
                  "╠⚛รูปวีดีโอ ➠วีดีโอเรา "+ "\n" + \
                  "╠⚛คท @ ➠ดึงคอนแท็ค "+ "  \n" + \
                  "╠⚛Mid @ ➠ดึงmid "+ "  \n" + \
                  "╠⚛Video @➠ดึงวีดีโอ "+ "\n" +\
                  "╠⚛ชื่อ @ ➠ดึงชื่อ "+ "  \n" + \
                  "╠⚛ตัส @ ➠ดึงตัส "+ "  \n" + \
                  "╠⚛รูป @ ➠ดึงรุป "+ "  \n" + \
                  "╠⚛ปก @ ➠ดึงรุปปก "+ "  \n" + \
                  "╠⚛ข้อมูล @ ➠เช็คข้อมูล "+ "  \n" + \
                  "╠⚛ชื่อ: (ใส่ชื่อ) ➠เปลี่ยนชื่อ "+ "  \n" + \
                  "╠⚛ตัส: (ใส่ตัส) ➠เปลี่ยนตัส "+ "  \n" + \
                  "╠⚛โพส ➠โพสไทม์ไลน์ "+ "  \n" + \
                  "╠⚛Copy @ /ก็อป➠ ก็อปปี้"+ "  \n" + \
                  "╠⚛คืนร่าง /.คืนร่าง➠ คืนร่าง "+ "  \n" + \
                  "╠⚛บล็อค ➠ เช็คจำนวนบล็อค "+ "  \n" + \
                  "╠⚛เพื่อน ➠ เช็จำนวนเพื่อน"+ "  \n" + \
                  "╠⚛จำนวนmid ➠midเพื่อน "+ "  \n" + \
                  "╠⚛กลุ่ม ➠ เช็คกลุ่มทั้งหมด "+ "  \n" + \
                  "╠⚛Zx ➠ ปฏิเสธิคำเชิญทุกกลุ่ม "+ "  \n" + \
                  "╠⚛แทค ➠ แทคทุกคน "+ "  \n" + \
                  "╠⚛เลียนแบบ @ ➠ พิมตาม "+ "  \n" + \
                  "╠⚛ยกเลิก @ ➠ ยกเลิกเลียนแบบ"+ "  \n" + \
                  "╠⚛Nutmic on/off ➠เลียนแบบ เปิด ปิด "+ "  \n" + \
                  "╠⚛เช็คเลียนแบบ ➠ เช็ครายชื่อ "+ "  \n" + \
                  "╠⚛หารูป (ตามด้วยชื่อรุป) "+ "  \n" + \
                  "╠⚛รูปการตูน (ตามด้วยชื่อรุป) "+ "  \n" + \
                  "╠⚛เพลง (ตามด้วยชื่อเพลง) "+ "  \n" + \
                  "╠⚛ยูทูป (ตามด้วยชื่อคลิป) "+ "  \n" + \
                  "╠⚛วีดีโอ (ตามด้วยชื่อ) "+ " \n" +\
                  "╠⚛หนัง (ตามด้วยชื่อหนัง) "+ "  \n" + \
                  "╠⚛เขียน (ตามด้วยคำ) "+ "  \n" + \
                  "╠⚛ภาพ (ตามด้วยคำ) "+ "  \n" + \
                  "╠⚛ค้นหาอินสตาแกรม "+ "  \n" + \
                  "╠⚛เวลา ➠ เช็คเวลา "+ "  \n" + \
                  "╠⚛ขอหื่น ➠ ลิ้งหนังโป๊ "+ "  \n" + \
                  "╠⚛พูด ➠ สั่งสิริพูด "+ "  \n" + \
                  "╠⚛Tr-th ➠ แปลภาษา "+ "  \n" + \
                  "╠⚛Dow (ข้อความ) เปลี่ยนไอดี "+ "  \n" + \
                  "╠⚛สปีด ➠ สปีดขำๆ "+ "  \n" + \
                  "╠⚛Zt"+ "  \n" + \
                  "╠⚛Zm"+ "  \n" + \
                  "╠⚛Zc"+ "  \n" + \
                  "╠⚛ประกาศ: "+ "  \n" + \
                  "╠⚛โทร ➠ เชิญโทร "+ "  \n" + \
                  "╠⚛ลบรัน /ลบรัน1 ➠ ลบรัน "+ "  \n" + \
                  "╠⚛ลบแชท ➠ ลบแชท "+ "  \n" + \
                  "╠⚛B on ➠ เปิดออโต้บล็อค "+ "  \n" + \
                  "╠⚛B off ➠ ปิดออโต้บล็อค "+ "  \n" + \
                  "╠⚛เปิดเข้า ➠ เข้ากลุ่มออโต้ "+ "  \n" + \
                  "╠⚛ปิดเข้า ➠ ปิดเข้ากลุ่มออโต้ "+ "  \n" + \
                  "╠⚛แชท on ➠ อ่านแชทออโต้ "+ "  \n" + \
                  "╠⚛แชท off ➠ ปิดอ่านแชทออโต้ "+ "  \n" + \
                  "╠⚛ติ้ก on ➠ เชคข้อมูลติ้ก "+ "  \n" + \
                  "╠⚛ติ้ก off ➠ ปิดเชคข้อมูลติ้ก "+ "  \n" + \
                  "╠⚛แทค on ➠ เปิดตอบคนแทค "+ "  \n" + \
                  "╠⚛แทค off ➠ ปิดตอบคนแทค "+ "  \n" + \
                  "╠⚛Tag2 on ➠ แสดงรูปคนแทค "+ "  \n" + \
                  "╠⚛Tag2 off ➠ ปิดแสดงรูปคนแทค "+ "  \n" + \
                  "╠⚛ตั้งแทค: (ตามด้วยข้อความ) "+ "  \n" + \
                  "╠⚛เปิดคนเข้า➠ เปิดข้อความคนเข้า "+ "  \n" + \
                  "╠⚛ปิดคนเข้า➠ ปิดข้อความคนเข้า "+ "  \n" + \
                  "╠⚛เปิดคนออก➠ข้อความคนออก "+ "  \n" + \
                  "╠⚛ปิดคนออก➠ ข้อความคนออก"+ " \n" +\
                  "╠⚛ตั้งเข้า: (ตามด้วยข้อความ) "+ "  \n" + \
                  "╠⚛ตั้งออก: (ตามด้วยข้อความ) "+ "  \n" + \
                  "╠⚛ข้อมูลกลุ่ม ➠เช็คข้อมูลกลุ่ม "+ "  \n" + \
                  "╠⚛เปิดลิ้ง ➠ เปิดลิ้งกลุ่ม "+ "  \n" + \
                  "╠⚛ปิดลิ้ง ➠ ปิดลิ้งกลุ่ม "+ "  \n" + \
                  "╠⚛ขอลิ้ง "+ "  \n" + \
                  "╠⚛ยกเลิก ➠ ลบค้างเชิญ "+ "  \n" + \
                  "╠⚛แอบ ➠ ดูคนแอบ "+ " \n" +\
                  "╠⚛ปิดแอบ ➠ เลิกจับคนแอบ "+ "\n " + \
                 "╠⚛ไวรัส ➠ ลงไวรัส "+ "  \n" + \
                  "╠⚛ทีมบอท ➠Admin "+ "  \n" + \
                  "╠⚛แอด ➠ เช็คแอดกลุ่ม "+ "  \n" + \
                  "╠⚛ไอดีกลุ่ม ➠ เช็คGid "+ "  \n" + \
                  "╠⚛ชื่อกลุ่ม ➠ ดึงชื่อกลุ่ม "+ "  \n" + \
                  "╠⚛รูปกลุ่ม ➠ดึงรุปกลุ่ม "+ "  \n" + \
                  "╠⚛รายชื่อ ➠รายชื่อสมาชิก "+ "  \n" + \
                  "╠⚛Vk @ ➠เตะ ดึงกลับ "+ "  \n" + \
                  "╠⚛เตะ @ ➠ เตะ "+ "  \n" + \
                  "╠⚛ฟัก @ ➠ เตะ "+ "  \n" + \
                  "╠⚛Ban @ ➠แบน "+ "  \n" + \
                  "╠⚛Unban @ ➠ ปลดแบน "+ "  \n" + \
                  "╠⚛Allban ➠ แบนทุกคน "+ "  \n" + \
                  "╠⚛เตะแบน ➠ เตะคนติดแบน "+ "  \n" + \
                  "╠⚛เช็คแบน ➠ เชคคนติดแบน "+ "  \n" + \
                  "╠⚛Spam on ➠ สแปม "+ "  \n" + \
                  "╠⚛Spam off ➠ สแปม "+ "  \n" + \
                  "╠⚛@ออก ➠ ออกจากกลุ่ม "+ "  \n" + \
                  "╠⚛Gcancel:         "+ "  \n" + \
                  "╠⚛ล้างแบน ➠ ล้างแบนทั้งหมด "+ "  \n" + \
                  "╠⚛มอง ➠ นับคนอ่าน "+ "  \n" + \
                  "╠⚛ไครอ่าน ➠ ดูคนอ่าน "+ "  \n" + \
                  "╠⚛เชิญ/เชิน ➠ เชิญ "+ "  \n" + \
                  "╠⚛เปิดป้องกัน / ปิดป้องกัน "+ "  \n" + \
                  "╠⚛กันลบ on / off "+ "  \n" + \
                  "╠⚛กันยก on / off "+ "  \n" + \
                  "╠⚛กันเชิญ on/off  "+ "  \n" + \
                  "╠⚛กันลิ้ง on/off "+ "  \n" + \
                  "╠⚛ป้องกัน on / off "+ "  \n" + \
                  "╠⚛กันเข้า on/ off "+ "  \n" + \
                  "╚═══В¥.VąŁķỳŗįè тєάм ңάĉќ "
    return myHelp


def helptexttospeech():
    helpTextToSpeech =   "╔══════════════┓" + "\n" + \
                      "╠❂➣ af : แอฟริกัน " + "\n " +\
                      "╠❂➣ sq : อัลเบเนีย" + "\n" + \
                      "╠❂➣ ar : อราบิค" + "\n" + \
                      "╠❂➣ hy : อาเมเนีย" + "\n" + \
                      "╠❂➣ bn : บังการี่" + "\n" + \
                      "╠❂➣ bs : บอสเนีย" + "\n" + \
                      "╠❂➣ bg : บังแกเรีย" + "\n" + \
                      "╠❂➣ zh-cn : จีน" + "\n" + \
                      "╠❂➣ zh-tw : ใต้หวัน" + "\n" + \
                      "╠❂➣ cs : เช็ก" + "\n" + \
                      "╠❂➣ nl : ดัช" + "\n" + \
                      "╠❂➣ en : อังกฤษ" + "\n" + \
                      "╠❂➣ et : เอสโตเนียน" + "\n" + \
                      "╠❂➣ el : กรีก" + "\n" + \
                      "╠❂➣ id : อินโดนีเซีย" + "\n" + \
                      "╠❂➣ ga : ไอริส" + "\n" + \
                      "╠❂➣ it : อิตาลี" + "\n" + \
                      "╠❂➣ ja : ญี่ปุ่น" + "\n" + \
                      "╠❂➣ kn : แคนาดา" + "\n" + \
                      "╠❂➣ la : ลาติน" + "\n" + \
                      "╠❂➣ lv : ลัตเวีย" + "\n" + \
                      "╠❂➣ ms : มาเลเซีย" + "\n" + \
                      "╠❂➣ mt : มอลเตส" + "\n" + \
                      "╠❂➣ mn : มองโกเลีย" + "\n" + \
                      "╠❂➣ my : พม่า" + "\n" + \
                      "╠❂➣ fa : เปอร์เซีย" + "\n" + \
                      "╠❂➣ pt : โปรตุเกศ" + "\n" + \
                      "╠❂➣ ro : โรมาเนีย" + "\n" + \
                      "╠❂➣ ru : รัสเซีย" + "\n" + \
                      "╠❂➣ th : ไทย" + "\n" + \
                      "╠❂➣ zu : ซูลู" + "\n" + \
                      "╰═В¥.VąŁķỳŗįè тєάм ңάĉќ" + "\n" +  \
                      "           "
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    "╔══════════════┓" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══════════════┛" + "\n" + "\n\n" + \
                       "BY NUT"
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'คำสั่ง':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'คำสั่ง2':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'คำสั่ง3':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "ŚẾL₣ВΌŦ\nŚΡЄЄÐ (｡◕‿◕｡)")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))	
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "ŚẾL₣ВΌŦ\nŚΡЄЄÐ (｡◕‿◕｡)")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))						
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "➠รีบอทเสร็จแล้ว")
                    line.sendMessage(to, "กรุณาล็อคอินใหม่อีกครั้ง (｡◕‿◕｡)")
                    restartBot()
                elif text.lower() == 'บอทออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ŚẾL₣ВΌŦ ÒŃLÍŇỀ\n(｡◕‿◕｡)\n {}".format(str(runtime)))
                elif text.lower() == 'ข้อมูล':
                    try:
                        arr = []
                        owner = "u0035a5a6c5ae9d30c9a0992ecbc39395"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "\nŚẾL₣ВΌŦ LÍŇỀ"
                        ret_ = "ŚẾL₣ВΌŦ LÍŇỀ\n(｡◕‿◕｡)"
                        ret_ += "\n╠😊ชื่อ ➠ {}".format(contact.displayName)
                        ret_ += "\n╠😊 จำนวนกลุ่ม ➠  {}".format(str(len(grouplist)))
                        ret_ += "\n╠😊จำนวนเพื่อน ➠  {}".format(str(len(contactlist)))
                        ret_ += "\n╠😊จำนวนบล็อค ➠  {}".format(str(len(blockedlist)))
                        ret_ += "\n╠😊 ข้อมูลบัญชีคุณ"
                        ret_ += "\n╠😊CREATOR ➠{}".format(creator.displayName)
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#========================
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = line.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    line.kickoutFromGroup(msg.to,[target])
                                    line.findAndAddContactsByMid(target)
                                    line. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
                elif "โทร" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"➠เชิญเข้าร่วมการโทรสำเร็จ (｡◕‿◕｡) ")	
                elif "ยกเลิก" == msg.text.lower():
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            line.cancelGroupInvitation(msg.to,[_mid])
                        line.sendMessage(to,"ยกเลิกค้างเชิญแล้ว (｡◕‿◕｡) " )           
#===========
                elif "สปีด" == msg.text.lower():
                    line.sendMessage(to,"「ความเร็ว...」\n███▒39%\n██████▒69%\n██████████▒99%\n0.0000000000000000 second")
                    line.sendMessage(to,"0.0000000000000000 second")  
                    line.sendMessage(to,"(｡◕‿◕｡)")
#==============================================================================#
                elif "creator" == msg.text.lower():
                    line.sendMessage(to,"CREATOR ŚẾL₣ВΌŦ\n(｡◕‿◕｡)")
                    line.sendContact(to, "u0035a5a6c5ae9d30c9a0992ecbc39395")
                elif "ไวรัส" == msg.text.lower():
                    line.sendMessage(to, "หยุด ขอให้อยู่ในความสงบ")
                    line.sendContact(to, "ud95860b8e3a6b3d2454cde75d9a5e3ec',")
                elif "ทีมบอท" == msg.text.lower():
                    msg.contentType = 13
                    line.sendMessage(to, "CREAROT & ADMIN \nŚẾL₣ВΌŦ (｡◕‿◕｡)")
                    line.sendContact(to, "u0035a5a6c5ae9d30c9a0992ecbc39395")
                    line.sendContact(to, "u9e0f538586963f09c59b75648081e9d5")
                    line.sendContact(to, "ubf4806077f2b20dd22fb3a7072eb0eb8")
                    line.sendContact(to, "ufec28f9f699a2cb6444e62e5397fe115")
                    line.sendContact(to, "ue1a44110ed4e82ba603010445f0ba585")
                    line.sendContact(to, "u6588c368db2307a41862b7385e00f4d8")                    
#==============================================================================#
                elif text.lower() == 'เช็ค':
                    try:
                        ret_ = "      ⚛️การตั้งค่าของคุณ (｡◕‿◕｡)"

                        if settings["autoAdd"] == True: ret_ += "\nออโต้บล็อค ➠ เปิด✔"
                        else: ret_ += "\nออโต้บล็อค ➠ ปิด❌"
                        if settings["detectMention"] == True: ret_ += "\nข้อความตอบแท็ค ➠ เปิด✔"
                        else: ret_ += "\nข้อความแท็ค ➠ ปิด❌"						
                        if settings["autoLeave"] == True: ret_ += "\ออกแชทรวมออโต้ ➠ เปิด✔"
                        else: ret_ += "\nออกแชทรวมออโต้ ➠ ปิด❌"
                        if settings["potoMention"] == True: ret_ += "\nแสดงรูปคนแทค ➠ เปิด✔"
                        else: ret_ += "\nแสดงรูปคนแทค ➠ ปิด❌"
                        if settings["kickMention"] == True: ret_ += "\nเตะคนแทค ➠ เปิด✔"
                        else: ret_ += "\nเตะคนแทค ➠ ปิด❌"
                        if RfuProtect["Protectjoin"] == True: ret_ += "\nป้องกันคนเข้ากลุ่ม ➠ เปิด✔"
                        else: ret_ += "\nป้องกันการเข้ารวม ➠ ปิด❌"	
                        if settings["autoRead"] == True: ret_ += "\nอ่านออโต้ ➠ เปิด✔"
                        else: ret_ += "\nอ่านออโต้ ➠ ปิด❌"				
                        if settings["checkSticker"] == True: ret_ += "\nเช็คสติ้กเกอร์ ➠ เปิด✔"
                        else: ret_ += "\nเช็คสติ้กเกอร์ ➠ ปิด❌"						
                        if RfuProtect["Protectguest"] == True: ret_ += "\nระบบป้องกัน ➠ เปิด✔"
                        else: ret_ += "\nระบบป้องกัน ➠ ปิด❌"		
                        if RfuProtect["inviteprotect"] == True: ret_ += "\nป้องกันการเชิญ ➠ เปิด✔"
                        else: ret_ += "\nป้องกันการเชิญ ➠ ปิด❌"
                        if RfuProtect["cancelprotect"] == True: ret_ += "\nป้องกันการยกเลิกเชิญ ➠ เปิด✔"
                        else: ret_ += "\nป้องกันการยกเลิกเชิญ ➠ ปิด❌"
                        if RfuProtect["protect"] == True: ret_ += "\nป้องกันการลบสมาชิก ➠ เปิด✔"
                        else: ret_ += "\nป้องกันการลบสมาชิก  ปิด❌"
                        if RfuProtect["linkprotect"] == True: ret_ += "\nป้องกันลิ้ง QR ➠ เปิด✔"
                        else: ret_ += "\nป้องกันลิ้ง QR ➠ ปิด❌"
                        if settings["autoCancel"]["on"] == True:ret_+="\nยกเลิกเชิญกลุ่มเมื่อมีสมาชิกต่ำกว่า  " + str(settings["autoCancel"]["members"]) + "➠ เปิด✔"
                        else: ret_ += "\nยกเลิกเชิญกลุ่ม  ➠ ปิด❌"
                        if settings["autoJoin"] == True: ret_ += "\nเข้ากลุ่มออโต้ ➠ เปิด✔ "
                        else: ret_ += "\nเข้ากลุ่มออโต้ ➠ ปิด❌"		
                        ret_ += "\n"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'b on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "เปิดออโต้บล็อค (｡◕‿◕｡)")
                elif text.lower() == 'b off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "ปิดออโต้บล็อค (｡◕‿◕｡)")
                elif text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "เข้ากลุ่มออโต้ (｡◕‿◕｡)")
                elif text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "ปิดเข้ากลุ่มออโต้ (｡◕‿◕｡)")			
                elif text.lower() == 'แชท on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "ออกแชทรวมออโต้ (｡◕‿◕｡)")
                elif text.lower() == 'แชท off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "ปิดออกแชทรวมออโต้ (｡◕‿◕｡)")
                elif text.lower() == 'อ่าน on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "เปิดอ่านแชทออโต้ (｡◕‿◕｡)")
                elif text.lower() == 'อ่าน off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "ปิดอ่านแชทออโต้ (｡◕‿◕｡)")
                elif text.lower() == 'ติ้ก on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "เปิดระบบเช็ค สติกเกอร์ (｡◕‿◕｡)")
                elif text.lower() == 'ติ้ก off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "ปิดระบบเช็ค สติกเกอร์ (｡◕‿◕｡)")                   
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'mid':
                    line.sendMessage(msg.to,"Mid (｡◕‿◕｡)\n " +  lineMID)
                elif text.lower() == 'ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"ชื่อ (｡◕‿◕｡) \n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"ข้อความตัส (｡◕‿◕｡) \n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'รูปวิดีโอ':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'รูปปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "(｡◕‿◕｡)  \n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "(｡◕‿◕｡)  \n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
#==========================================                            
                elif msg.text.lower().startswith("ข้อมูล "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, contact.displayName)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, contact.statusMessage)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ">"
                        for ls in lists:
                            ret_ += ls
                        line.sendMessage(msg.to, str(ret_))
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))                            
                elif msg.text.lower().startswith("video "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "ผิดพลาด (^人^)")
                        except:
                            line.sendMessage(msg.to, "สำเร็จ (｡◕‿◕｡)")
                            
                elif text.lower() == 'คืนร่าง':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "(^人^)")
                    except:
                        line.sendMessage(msg.to, "(｡◕‿◕｡)")
						
#==============================================                    
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,str(settings["eror"]))
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")
                elif msg.text.lower().startswith("เลียนแบบ "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"เลียนแบบแล้ว (｡◕‿◕｡)")
                            break
                        except:
                            line.sendMessage(msg.to,"ผิดพลาด (^人^)")
                            break
                elif msg.text.lower().startswith("ยกเลิก "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"ยกเลิกเลียนแบบแล้ว \n(｡◕‿◕｡)")
                            break
                        except:
                            line.sendMessage(msg.to,"ผิดพลาด (^人^)")
                            break
                elif text.lower() == 'เช็คเลียนแบบ':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"ไม่พบการเลียนแบบ (｡◕‿◕｡)")
                    else:
                        mc = "   รายชื่อ การเลียนแบบ"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n    ŚẾL₣ВΌŦ VąŁķỳŗįè \nтєάм ңάĉќ")
                    
                elif "nutmic " in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"เปิดการเลียนแบบ (｡◕‿◕｡)")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"ปิดการเลียนแบบ (｡◕‿◕｡)")
#==============================================================================#
                elif text.lower() == 'แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "คนนี้คือคนสร้างกลุ่มนี้\n(｡◕‿◕｡)")
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ไอดีกลุ่มนี้ " + gid.id + " \n(｡◕‿◕｡)")
                elif text.lower() == 'รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ชื่อกลุ่ม" + gid.name + " \n(｡◕‿◕｡)")
                elif text.lower() == 'ขอลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งQR ของกลุ่มนี้ \nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "ลิ้งเปิดอยู่ สั่งว่า ของลิ้ง \n(｡◕‿◕｡)")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งQRกลุ่มแล้ว (｡◕‿◕｡)")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ลิ้งQRปิดอยู่ (｡◕‿◕｡)")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งQR แล้ว (｡◕‿◕｡)")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "   ŚẾL₣ВΌŦ (｡◕‿◕｡)"
                    ret_ += "\nชื่อกลุ่ม ➠  {}".format(str(group.name))
                    ret_ += "\nไอดีกลุ่ม ➠  {}".format(group.id)
                    ret_ += "\nผู้สร้างกลุ่ม ➠  {}".format(str(gCreator))
                    ret_ += "\nจำนวนสมาชิก ➠ {}".format(str(len(group.members)))
                    ret_ += "\nจำนวนค้างเชิญ ➠ {}".format(gPending)
                    ret_ += "\nลิ้งQR ของกลุ่ม ➠ ".format(gQr)
                    ret_ += "\nВ¥.VąŁķỳŗįè тєάм ңάĉќ"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
#=======================================                                
                elif "โพส " in msg.text:
                    tl_text = msg.text.replace("โพส ","")
                    line.sendText(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                elif "ก็อป " in msg.text:
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            P = contact.pictureStatus
                            hun = line.getProfile()
                            hun.pictureStatus = P
                            line.updateProfile(hun)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif msg.text in [".คืนร่าง"]:
                    try:
                        #line.updateProfile.pictureStatus(backup.pictureStatus)
                        line.updateProfile.statusMessage(backup.statusMessage)
                        line.updateProfile.displayName(backup.displayName)
                        line.sendMessage(msg.to, "กลับร่างเดิมแล้ว")
                    except Exception as e:
                        line.sendText(msg.to, str (e))                    

                elif text.lower() == 'รายชื่อ':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "   จำนวน&รายชื่อ สมาชิก"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n↜ ↝ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n   ↠ จำนวน {}   คน ↞ ".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'กลุ่ม':
                        groups = line.groups
                        ret_ = "   จำนวนกลุ่มของคุณ"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n➠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n จำนวน {} กลุ่ม  ".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

#                elif text.lower() == '1กลุ่ม':
#                        groups = ki.groups
#                        ret_ = "   ⚔️ Š€£Բ ฿✪Ŧ β¥.Šαї ⚔️ "
#                        no = 0 + 1
#                        for gid in groups:
#                            group = ki.getGroup(gid)
#                            ret_ += "\n➢ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
#                            no += 1
#                        ret_ += "\n จำนวน {} กลุ่ม ".format(str(len(groups)))
#                        ki.sendMessage(to, str(ret_))
#
#                elif text.lower() == '2กลุ่ม':
#                        groups = kk.groups
#                        ret_ = "   ⚔️ Š€£Բ ฿✪Ŧ β¥.Šαї ⚔️ "
#                        no = 0 + 1
#                        for gid in groups:
#                            group = kk.getGroup(gid)
#                            ret_ += "\n➢ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
#                            no += 1
#                        ret_ += "\n  จำนวน {} กลุ่ม".format(str(len(groups)))
#                        kk.sendMessage(to, str(ret_))
#
#                elif text.lower() == '3กลุ่ม':
#                        groups = kc.groups
#                        ret_ = "╔══[ Group List ]"
#                        no = 0 + 1
#                        for gid in groups:
#                            group = kc.getGroup(gid)
#                            ret_ += "\n➢ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
#                            no += 1
#                        ret_ += "\n จำนวน {} กลุ่ม".format(str(len(groups)))
#                        kc.sendMessage(to, str(ret_))
						
					
#==============================================================================#
#==============================================================================#          
                elif text.lower() == 'แทค':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = line.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len(contact)
                                if jml <= 100:
                                    mentionMembers(to, contact)
                                elif jml > 100 and jml <= 200: 
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, jml):
                                        ct2 += [contact[b]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                elif jml > 200 and jml <= 300:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, jml):
                                        ct3 += [contact[c]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                elif jml > 300 and jml <= 400:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, jml):
                                        ct4 += [contact[d]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                elif jml > 400 and jml <= 500:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, 399):
                                        ct4 += [contact[d]]
                                    for e in range(400, jml):
                                        ct4 += [contact[e]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                    mentionMembers(to, ct5)
#===================================================================#              

                elif text.lower() == 'มอง':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา  [ " + timeNow.strftime('%H:%M:%S') + " ]"
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
                                line.sendMessage(msg.to,"กำลังนับคนอ่าน\n(｡◕‿◕｡)")
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
                            line.sendMessage(msg.to, "เริ่มนับคนอ่านแบบแทค\n(｡◕‿◕｡)\n" + readTime)
                            

                elif text.lower() == 'ไครอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา  [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"รายชื่อคนที่อ่าน \nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'รายชื่อคนที่อ่าน \n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\nเวลาที่อ่าน \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"สั่ง (มอง) แล้วสั่ง (ไครอ่าน) \n(^人^) ")

                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)


#=============================================#                    
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")    

#==============================================================================#
                elif "ประกาศกลุ่ม " in msg.text:
                    bc = msg.text.replace("ประกาศกลุ่ม ","")
                    gid = line.getGroupIdsJoined()
                    for i in gid:
                        line.sendText(i,"======[ข้อความประกาศกลุ่ม]======\n\n"+bc+"\n\n(｡◕‿◕｡)")
                    
                elif "ประกาศแชท " in msg.text:
                    bc = msg.text.replace("ประกาศแชท ","")
                    gid = line.getAllContactIds()
                    for i in gid:
                        line.sendText(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\n(｡◕‿◕｡)")
#                elif "Bcvoice " in msg.text:
#                    bctxt = msg.text.replace("Bcvoice ", "")
#                    bc = ("⚔️ Š€£Բ ฿✪Ŧ β¥.Šαї ⚔️ \nŦ€Āʍ ĦĀ¢₭€Ɖ ĊΦƉ€")
#                    cb = (bctxt + bc)
#                    tts = gTTS(cb, lang='id', slow=False)
#                    tts.save('tts.mp3')
#                    n = line.getGroupIdsJoined()
#                    for manusia in n:
#                        line.sendAudio(manusia, 'tts.mp3')
#
#                elif "Cbcvoice " in msg.text:
#                    bctxt = msg.text.replace("Cbcvoice ", "")
#                    bc = ("⚔️ Š€£Բ ฿✪Ŧ β¥.Šαї ⚔️ \nŦ€Āʍ ĦĀ¢₭€Ɖ ĊΦƉ€")
#                    cb = (bctxt + bc)
#                    tts = gTTS(cb, lang='id', slow=False)
#                    tts.save('tts.mp3')
#                    n = line.getAllContactIdsJoined()
 #                   for manusia in n:
#                        line.sendAudio(manusia, 'tts.mp3')
#
                elif "Dow " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Dow ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="เกินขีด จำกัด ข้อความ! โปรดคลิกลิงก์\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))
#=================================
                elif text.lower() == 'self off':
                    line.sendMessage(receiver, 'ŚẾL₣ВΌŦ Ό₣₣ \n(｡◕‿◕｡) ')
                    print ("Selfbot Off")
                    exit(1)   
#==============================================
                elif msg.text == "ขอหื่น":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")
                elif msg.text == ".ประกาศ":
                	line.sendMessage(msg.to,str)      
#========================================
                elif msg.text in ["zx"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)							
                        except:
                            pass        
#=======================================                        
                elif "google " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.google.com/search?q=", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.google.com/search?q={}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "หนัง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))
                        
                elif "เพลง " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "เพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))         
#=========================================
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)        

#                elif "ค้นหาหนัง" in msg.text:
#                    proses = msg.text.split(":")
#                    get = msg.text.replace(proses[0] + ":","")
#                    getfilm = get.split()
#                    title = getfilm[0]
#                    tahun = getfilm[1]
#                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
#                    start = time.time()
#                    data=r.text
#                    data=json.loads(data)
#                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
#                    hasil += "\n\n " +str(data["Plot"])
#                    hasil += "\n\nDirector : " +str(data["Director"])
#                    hasil += "\nActors   : " +str(data["Actors"])
#                    hasil += "\nRelease : " +str(data["Released"])
#                    hasil += "\nGenre    : " +str(data["Genre"])
#                    hasil += "\nRuntime   : " +str(data["Runtime"])
#                    path = data["Poster"]
#                    line.sendImageWithURL(msg.to, str(path))
#                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'เวลา':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 


                
                elif "ค้นหาอินสตาแกรม" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "   ŚẾL₣ВΌŦ LÍŇỀ"
                            ret_ += "\n ชื่อ   {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n ยูเซอเนม : {}".format(str(data["user"]["username"]))
                            ret_ += "\n ตัส  {}".format(str(data["user"]["biography"]))
                            ret_ += "\n ผู้ติดตาม   {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n ติดตาม   {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n การยืนยัน: แล้ว"
                            else:
                                ret_ += "\n การยืนยัน: ยังไม่ได้"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n Akun Pribadi : Iya"
                            else:
                                ret_ += "\n บัญชีส่วนบุคคล: ไม่"
                            ret_ += "\n Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "ไม่พบผู้ใช้")

                    line.sendMessage(to, str(ret_))
                elif "หารูป" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "รูปการตูน" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "ยูทูป" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "การค้นหามีรายละเอียดตามนี้"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n⋙ {} ]".format(str(data["title"]))
                            ret_ += "\n⋙ https://www.youtube.com{}".format(str(data["href"]) + "\n")
                        ret_ += "\n\n⋙ ที่พบ {}  คลิป".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["แอบ"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"เริ่มจับคนอ่าน (｡◕‿◕｡) ")
                elif msg.text in ["ปิดแอบ"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        #line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    #else:
                        line.sendMessage(msg.to, "เลิกจับคนแอบละ (｡◕‿◕｡)")



                elif text.lower() == 'เพื่อน':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="จำนวน&รายชื่อเพื่อน"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["บล็อค"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="รายการ บล็อค (^人^)"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["จำนวนmid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="ŚẾL₣ВΌŦ LÍŇỀ"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\nจำนวน  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)



#                elif msg.text.lower() == 'เชิญกุ':
#                	if msg.toType == 2:                
#                           ginfo = line.getGroup(receiver)
#                           try:
#                               gcmid = ginfo.creator.mid
#                           except:
#                               gcmid = "Error"
#                           if settings["lang"] == "JP":
#                               line.inviteIntoGroup(receiver,[gcmid])
#                               line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่ม")
#                           else:
#                               line.inviteIntoGroup(receiver,[gcmid])
#                               line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")

                elif msg.text in ["@ออก"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)
                            #ki.leaveGroup(receiver)
                            #kk.leaveGroup(receiver)
                            #kc.leaveGroup(receiver)
                            #ke.leaveGroup(receiver)							
                        except:
                            pass


                elif msg.text in ["แทค on"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"เปิดข้อความตอบคนแทค \n(｡◕‿◕｡)")
                
                elif msg.text in ["แทค off"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"ปิดข้อความตอบคนแทค \n(｡◕‿◕｡)")
                    
                elif msg.text in ["เตะแทค on"]:
                    settings["kickMention"] = True
                    line.sendMessage(msg.to,"เปิดระบบเตะคนแทค (｡◕‿◕｡)")
                
                elif msg.text in ["เตะแทค off"]:
                    settings["kickMention"] = False
                    line.sendMessage(msg.to,"ปิดระบบเตะคนแทค (｡◕‿◕｡)")      
#============================                    
#               elif msg.text in [".เปิดตรวจสอบ"]:
#                   settings["aip"] = True
#                    line.sendMessage(msg.to,"เปิดระบบตรวจสอบคำหยาบกับบอทบิน  ^ω^")
#                
#                elif msg.text in [".ปิดตรวจสอบ"]:
#                    settings["aip"] = False
#                    line.sendMessage(msg.to,"ปิดระบบตรวจสอบคำหยาบกับบอทบินแล้วʕ•ﻌ•ʔ")
#                    
#                elif msg.text in [".เปิดพูด"]:
#                    settings["api"] = True
#                    line.sendMessage(msg.to,"เปิดระบบApiข้อความ")
#                
#                elif msg.text in [".ปิดพูด"]:
#                    settings["api"] = False
#                    line.sendMessage(msg.to,"ปิดระบบApiข้อความแล้ว")              
#==========================================                    
                elif text.lower() == 'tag2 on':
                    settings['potoMention'] = True
                    line.sendMessage(msg.to,"เปิดแสดงรูปภาพคนแท็ค\n(｡◕‿◕｡)")
                elif text.lower() == 'tag2 off':
                    settings['potoMention'] = False
                    line.sendMessage(msg.to,"ปิดแสดงรูปภาพคนแท็ค \n(｡◕‿◕｡)")                    

                elif 'ตั้งแทค: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งแทค: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความเรืยบร้อย\n(｡◕‿◕｡)")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "ข้อความตอบแทคของคุณ\n\n{}".format(str(spl)))


                elif 'ตั้งออก: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งออก: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนออกเรียบร้อย\n(｡◕‿◕｡)")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "ข้อความทักคนออกของคุณ\n\n\n{}".format(str(spl)))

                elif 'ตั้งเข้า: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งเข้า: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งข้อความคนเข้าเรียบร้อยแล้ว\n(｡◕‿◕｡)")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "ข้อความทักคนเข้าของคุณ\n\n\n{}".format(str(spl)))

                elif msg.text.lower().startswith("ภาพ "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบกลุ่มเชิญทั้งหมดแล้ว\n(｡◕‿◕｡)")
                    line.sendMessage(to, "เวลาที่ใช้: %sวินาที" % (elapsed_time))						
						
                elif text.lower() == 'zt':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ม่มีคนใส่ร่องหนในกลุ่มนี้ (｡◕‿◕｡)")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'zm':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน (｡◕‿◕｡)")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'zc':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้ (｡◕‿◕｡)")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
                            
                elif 'ลบเชิญS' in msg.text.lower():
                   if msg.toType == 2:
                       X = line.getGroup(msg.to)
                       if X.invitee is not None:
                           gInviMids = [contact.mid for contact in X.invitee]
                           line.cancelGroupInvitation(msg.to, gInviMids)
                       else:
                           if settings["lang"] == "JP":
                               line.sendMessage(msg.to,"ไม่มีการเชิญ")
                           else:
                               line.sendMessage(msg.to,"ขออภัยไม่มี")
                   else:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"ไม่สามารถใช้นอกกลุ่มได้")
                       else:
                           line.sendMessage(msg.to,"ไม่ใช้งานน้อยกว่ากลุ่ม")

                elif 'ตั้งคนออก: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคนออก: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งคนออก")
                     else:
                          settings["Nn"] = spl
                          line.sendMessage(msg.to, "{}".format(str(spl)))
                elif 'ตั้งคนเข้า: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('ตั้งคนเข้า: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "ตั้งคนออก")
                     else:
                          settings["Sd"] = spl
                          line.sendMessage(msg.to, "{}".format(str(spl)))

                elif msg.text in ["เชิญ"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"ส่งคอนแทคเพื่อเชิญ\n(｡◕‿◕｡)")


                elif msg.text in ["ล้างแบน"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียบร้อย\n(｡◕‿◕｡)")
                    print ("Clear Ban")

                elif text.lower() == 'บักหำ':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)                        
                        group.preventedJoinByTicket = True
                        line.updateGroup(group)
                        print ("คลิ้กเข้า ")

                elif 'เตะ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("เตะคน")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"จำกัด")

                elif 'ฟัก' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("เตะคน1")
                           except:
                               line.sendMessage(msg.to,"จำกัด")                               

                elif '1 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.kickoutFromGroup(msg.to,[target])           
                               print ("คลิ้ก1เตะ")
                           except:
                               ki.sendMessage(msg.to,"จำกัด")                               

                elif '2 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.kickoutFromGroup(msg.to,[target])
                               print ("คลิ้ก2เตะ")
                           except:
                               kk.sendMessage(msg.to,"จำกัด")                              

                elif '3 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.kickoutFromGroup(msg.to,[target])
                               print ("คลิ้ก3เตะ")
                           except:
                               kc.sendMessage(msg.to,"จำกัด")                              


                elif 'เชิน' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "เชิญok")
                           except:
                               line.sendMessage(msg.to,"จำกัด การเชิญ")

                elif '1เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.inviteIntoGroup(msg.to,[target])
                               ki.sendMessage(receiver, "เชิญok")
                               print ("R1 invite User")
                           except:
                               ki.sendMessage(msg.to,"จำกัด การเชิญ")                               

                elif '2เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.inviteIntoGroup(msg.to,[target])
                               kk.sendMessage(receiver, "เชิญok")
                               ("R2 invite User")
                           except:
                               kk.sendMessage(msg.to,"จำกัด การเชิญ")                               

                elif '3เชิญ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.inviteIntoGroup(msg.to,[target])
                               kc.sendMessage(receiver, "เชิญ")
                               ("R3 invite User")
                           except:
                               kc.sendMessage(msg.to,"จำกัด การเชิญ")                               
                elif "ไอ้หำ" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("ไอ้หำ","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"ผิดพลาด")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line,ki,kk,kc,ke]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["เตะแบน"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"ไม่มีบัญชีดำ\n(｡◕‿◕｡)")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line,ki,kk,kc,ke]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"(^人^)")
                                     print ("ไล่เตะดำ")

                elif text.lower() == "ลบแชท":
                        if msg._from in Family:
                            try:
                                line.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)                                
                                line.sendMessage(msg.to,"ลบแชทเรียบร้อย \n (｡◕‿◕｡)")
                            except:
                                pass
                                print ("ลบแชท")

                elif text.lower() == "ออก1":
                    if msg._from in Family:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)                        
                        print ("Kicker Leave")

                elif text.lower() == "ออกแชทรวม":
                    if msg._from in Family:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)                            
                            print ("ออกแชท")

                elif "ชื่อ: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนชื่อแล้ว(｡◕‿◕｡)\n เปลี่ยนเป็น  " + string)
                        print ("Update Name")

                elif "ตัส: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"เปลี่ยนตัสแล้ว (｡◕‿◕｡)\n เปลี่ยนเป็น  " + string)
                        print ("Update Bio Succes")

                elif "คลิ้ก: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = ke.getProfile()                        
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        profile_D.displayName = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"คุณได้เปลี่ยนชื่อคลิ้กเกอร์ เป็น   " + string)
                        print ("Update Name All Kicker")

                elif "ตัสคลิ้ก: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = kc.getProfile()                        
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        profile_D.statusMessage = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Bio All Kicker to : " + string)
                        print ("Update Bio All Kicker")

                elif text.lower() == "บักหำมา":
                    if msg._from in Family:
                        profile = ki.getProfile()
                        text = profile.displayName + ""
                        ki.sendMessage(to, text)                                
                        profile = kk.getProfile()
                        text = profile.displayName + ""
                        kk.sendMessage(to, text)                                
                        profile = kc.getProfile()
                        text = profile.displayName + ""
                        kc.sendMessage(to, text)
                        profile = ke.getProfile()                        
                        text = profile.displayName + ""
                        ke.sendMessage(to, text)                        
                        print ("สั่งคลิ้กเข้า")

  

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'กันลบ on':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันลบ off':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันการลบสมาชิค \n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันยก on':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันการยกเลิกเชิญ\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันการยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันการยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันการยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันยก off':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญสมาชิก\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันเชิญ on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันเชิญ off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญสมาชิก\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันลิ้ง on':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันลิ้ง off':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'ป้องกัน on':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้อง (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")

                elif msg.text.lower() == 'ป้องกัน off':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน (｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน (｡◕‿◕｡)")

                elif msg.text.lower() == 'กันเข้า on':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'กันเข้า off':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้ากลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'เปิดป้องกัน':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"กำลังเปิดป้องกันทั้งหมด (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันทั้งหมดเรียบร้อยแล้ว\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลบสมาชิก\n(｡◕‿◕｡)")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลบสมาชิก \n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลบสมาชิก \n(｡◕‿◕｡)")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องลบสมาชิก\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลบสมาชิก\n(｡◕‿◕｡)")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้งกลุ่ม\n(｡◕‿◕｡)")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน (｡◕‿◕｡)")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายนอกเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายนอกเข้ากลุ่ม\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายนอกเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายนอกเข้ากลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'ปิดป้องกัน':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันทั้งหมดเรียบร้อยแล้ว\n(｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันทั้งหมดเรียบร้อยแล้ว\n(｡◕‿◕｡)")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญคนเข้ากลุ่ม (｡◕‿◕｡)")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญคนเข้ากลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ (｡◕‿◕｡)")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ (｡◕‿◕｡)")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลบสมาชิกกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลบสมาชิกกลุ่ม (｡◕‿◕｡)")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลบสมาชิกกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลบสมาชิกกลุ่ม (｡◕‿◕｡)")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้งกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้งกลุ่ม (｡◕‿◕｡)")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้งกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้งกลุ่ม (｡◕‿◕｡)")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม (｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม (｡◕‿◕｡)")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนนอกเข้ากลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนนอกเข้ากลุ่ม (｡◕‿◕｡)")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนนอกเข้ากลุ่ม (｡◕‿◕｡)")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนนอกเข้ากลุ่ม (｡◕‿◕｡)")
#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'เปิดคนเข้า':
                        if settings["Nn"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            settings["Nn"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                elif msg.text.lower() == 'ปิดคนเข้า':
                        if settings["Nn"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับคนเข้ากลุ่ม\n(｡◕‿◕｡)")
                        else:
                            settings["Nn"] = False
                            if settings["Nn"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับคนเข้ากลุ่ม\n(｡◕‿◕｡)")

                elif msg.text.lower() == 'เปิดคนออก':
                        if settings["Sd"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนออก\n(｡◕‿◕｡)")
                        else:
                            settings["Sd"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความคนออก\n(｡◕‿◕｡)")
                elif msg.text.lower() == 'ปิดคนออก':
                        if settings["Sd"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนออก\n(｡◕‿◕｡)")
                        else:
                            settings["Sd"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความคนออก\n(｡◕‿◕｡)")

                elif text.lower() == '1ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้ว (｡◕‿◕｡)")
                    line.sendMessage(to, "เวลาที่ใช้: %sวินาที" % (elapsed_time))								
								
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"ผิดพลาด !")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"แบนสมาชิกทั้งหมดแล้ว (｡◕‿◕｡)")
										   
                elif 'ban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"แบนผู้ไช้แล้ว (｡◕‿◕｡)")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"ผิดพลาด !")

                elif 'unban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"ยกเลิกแบน ผู้ไช้แล้ว (｡◕‿◕｡)")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"ผิดพลาด !")

                elif msg.text in ["เช็คแบน"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่มีผู้ไช้ที่ติดแบน (｡◕‿◕｡)") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ไช้ที่ติดแบน (｡◕‿◕｡)")
                        mc = "รายชื่อ (｡◕‿◕｡)\n"
                        for mi_d in settings["blacklist"]:
                            mc += "➠ " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "VąŁķỳŗįè тєάм ңάĉќ"
                    ret_ += "\nสติกเกอร์ ID : {}".format(stk_id)
                    ret_ += "\nสติกเกอร์ PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\nสติกเกอร์ VERSION : {}".format(stk_ver)
                    ret_ += "\nสติกเกอร์ URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n    ŚẾL₣ВΌŦ LÍŇỀ"
                    line.sendMessage(to, str(ret_))
                    
#=========================================                                          
#            if msg.text in ["Speed","speed","Sp","sp"]:
#            	line.sendMessage(to,"ไวจัดเลยลูกพี่😁\nเดอะฟาสมาเอง🚗")
#            if msg.text in ["Me","me","คท"]:
 #           	line.sendMessage(to, "เชคทำไมกลัวบอทหลุดรึ😁")
#            if msg.text in ["."]:
#            	line.sendMessage(to,"SELFBOT ➠กำลังทำงาน ✔ ")
#            if msg.text in ["กำ","กำนะ"]:
#            	line.sendMessage(to,"กำหี😁\nกำนม😁")
#            if msg.text in ["ออนป่าว"]:
#            	line.sendMessage(to,"บอทออน")
#            if msg.text in ["เจ้"]:
#            	line.sendMessage(to, "เจ้ดูดม้า😁\nส่งคลิป😁\nติดกันชา\n55555555")
#            if msg.text in ["555","5555","55555"]:
#            	line.sendMessage(to,"ขำขนาดนี้ไปขี้เถอะ😂 ")
#            if msg.text in ["งิ","งิงิ"]:
#            	line.sendMessage(to,"งิไร มึงรุ้จักไอต่ายป่ะ😁")
            #if msg.text in ["ตอบรับผส","ตอบรับผส."]:
            	#nadya.sendMessage(to,"Hi Creator 😁™ωู้ざန้ד७❸➣❍ざูຮℓמՁஞণ")
            #if msg.text in ["ตั้งค่า"]:
            #	nadya.sendMessage(to,"เช็ค")
                #nadya.sendMessage(to,"เช็ค2")                    
              
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = kk.reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  line.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kiMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = kc.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kkMID:
              if op.param2 not in Family:
                try:
                  G = kc.getGroup(op.param1)
                  G = ki.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kcMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kc.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in keMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ke.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
#==============================================================================#
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kkMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kcMID:
                    if op.param2 in kkMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in keMID:
                    if op.param2 in kcMID:
                        G = ke.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = ke.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ke.updateGroup(G)
                        settings["blacklist"][op.param2] = True
            except:
                pass
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                                    
#============================                  
        if op.type == 17:
            if op.param2 in settings["blacklist"] == {}:
                line.kickoutFromGroup(op.param1,[op.param2])
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
                line.sendText(op.param1,"ผู้ไช้คนนี้อยู่ในแบนลิส (｡◕‿◕｡)"+tm)                                    

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"เปลี่ยนรูปภาพเรียบร้อยแล้ว")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki.sendChatChecked(to, msg_id)
                    kk.sendChatChecked(to, msg_id)
                    kc.sendChatChecked(to, msg_id)
                    ke.sendChatChecked(to, msg_id)					
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                        
#============================================                                     
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                        if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break                        

                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["\n " + cName ]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          line.sendMessage(to,str(settings["Respontag"]))
                                          #sendMessageWithMention(to, contact.mid)
                                          line.sendMessage(msg.to, None, contentMetadata={"STKID":"16463699","STKPKGID":"1431756","STKVER":"10"}, contentType=7)
                                          break




        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sd"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendMessage(op.param1,str(settings["welcome"]))
             line.sendImageWithURL(op.param1,image)
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Nn"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendImageWithURL(op.param1,image)
             line.sendMessage(op.param1,str(settings["bye"]) + "\n\n" + line.getContact(op.param2).displayName)
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n" + Name
                            pref=['แอบทมาย ออกมาควยกันมา (｡◕‿◕｡)  ']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n " + Name + "\n"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ VK SELFBOT] ")
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
#============================================                
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
