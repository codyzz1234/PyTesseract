import pyautogui as pyauto
def screenshot():
    image = pyauto.screenshot(region=(425,262,988,53))
    image.save('10Fast.png')
    
def writeTextToBox(text):
    textWrite = ""
    for s in range(0,len(text)):
        if(text[s] == ' ' or s == len(text) - 1):
            pyauto.write(textWrite)
            pyauto.press('space')
            textWrite = ""
            continue
        else:
            textWrite = textWrite + text[s]
    pyauto.press('space')
            