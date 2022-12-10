import pyautogui as pyauto
def screenshot():
    image = pyauto.screenshot(region=(425,262,988,53))
    image.save('10Fast.png')
    
def writeTextToBox(text):
    for s in text:
        if(s == ' '):
            pyauto.press('space')
        else:
            pyauto.write(s)
    pyauto.press('space')
            