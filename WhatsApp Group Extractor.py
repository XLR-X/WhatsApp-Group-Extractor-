import time
import pyautogui
import os 
import pyperclip
import shutil

def filecheck():
    i = 0
    while os.path.isfile(str(i) + "output.txt") == True:
        i = i+1
    return str(i) + "output.txt"



def main():
    print("open whatsapp web with group located in 5 sec\n")
    time.sleep(5)
    namejap = ""
    g = os.getcwd()
    pyperclip.copy(g)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    loc = pyperclip.paste()
    pyautogui.write(loc + "\WhatsApp")
    pyautogui.press("tab")

    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")

    pyautogui.press("enter")
    pyautogui.press("enter")
    file0 = 'WhatsApp.html'
    while 1 == 1:
        if os.path.exists(file0) == True:
            try:
                b = str(open(file0, "r", encoding = 'cp850').readlines())
                leno = len(b)
                i = 0
                j = 12
                start = b.find('zzgSd _3e6xi')
                end = b.find('_2YPr_ i0jNr selectable-text copyable-text')
                new = b[start:end].replace(' aria-label="" class=', "")
                new = new.replace("zzgSd _3e6xi", "")
                new = new.replace("><span title=", "")
                new = new.replace('"', "")
                new = new.replace(', ', "\n")
                namaiwa = filecheck()
                namejap = namaiwa
                open(namaiwa, "w").write(new)
                break
            except:
                pass
        else:
            pass
    
    print("Done>>saved in " +namejap + "\n")




print("Initializing files\n")
print(">>>>>>>>>>>>>>>>>>>\n")
print("<<<<<<<<<<<<<<<<<<<\n")
print("<<<<<<<success>>>>>\n")
print("*****WHATS APP GROUP NUMBER BACKUP CREATOR*****")
print("CREATED BY XLR_8")
time.sleep(1)

while 1 == 1:
    take = input("ENTER 1 and hit enter to copy group numbers\nENTER 0 to EXIST\n>>>")
    if take == "1":
        main()
        os.remove("WhatsApp.html")
    elif take == "0":
        break

shutil.rmtree(os.getcwd() + "\WhatsApp_files")