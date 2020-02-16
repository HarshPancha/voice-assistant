import speech_recognition as sr
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, Controller as KeyboardController
import the_H
import subprocess
from selenium import webdriver
from time import sleep

mouse = MouseController()
r = sr.Recognizer()
bro = ''
i = 0

def say(text):
    subprocess.call(['say', text])


while('close' not in bro and 'shut up' not in bro and 'shut down' not in bro):
    with sr.Microphone() as src:
        a = r.adjust_for_ambient_noise(src)   
        print("Say hey dude to start")
        while True:
            a = r.listen(src, phrase_time_limit = 3)
            try:
                t = r.recognize_google(a)
            except:
                t = ""
            if(format(t) == 'hey dude'):
                break

    if(format(t) == 'hey dude'):
        with sr.Microphone() as source:
            #print("Speak Anything :")
            audio = r.adjust_for_ambient_noise(source)
            say("Hey, what can I do for you")
            #print("ready")
            audio = r.listen(source , phrase_time_limit = 3)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                bro = format(text)
                if('tell me a joke' in bro):
                    say("Your Mama so fat when she got on a weighing machine she found her phone number")
                    i = 1
                if('scroll down' in bro):
                    mouse.scroll(0,-50)
                    bro = ''
                    i = 1
                if('scroll up' in bro):
                    mouse.scroll(0,50)
                    bro = ''
                    i = 1
                if('select' in bro):
                    mouse.press(Button.left)
                    bro = 'release'
                    i = 1
                    sleep(5)
                if('release' in bro):
                    mouse.release(Button.left)
                    bro = ''
                    i = 1
                if('1, 1' in bro):
                    mouse.position = (160,80)
                    bro = ''
                    i = 1
                if('1, 2' in bro):
                    mouse.position = (520,80)
                    bro = ''
                    i = 1
                if('1, 3' in bro):
                    mouse.position = (880,80)
                    bro = ''
                    i = 1
                if('1, 4' in bro):
                    mouse.position = (1240,80)
                    bro = ''
                    i = 1
                if('2, 1' in bro):
                    mouse.position = (160,240)
                    bro = ''
                    i = 1
                if('2, 2' in bro):
                    mouse.position = (520,240)
                    bro = ''
                    i = 1
                if('2, 3' in bro):
                    mouse.position = (880,240)
                    bro = ''
                    i = 1
                if('2, 4' in bro):
                    mouse.position = (1240,240)
                    bro = ''
                    i = 1
                if('3, 1' in bro):
                    mouse.position = (160,400)
                    bro = ''
                    i = 1
                if('3, 2' in bro):
                    mouse.position = (520,400)
                    bro = ''
                    i = 1
                if('3, 3' in bro):
                    mouse.position = (880,400)
                    bro = ''
                    i = 1
                if('3, 4' in bro):
                    mouse.position = (1240,400)
                    bro = ''
                    i = 1
                if('4, 1' in bro):
                    mouse.position = (160,560)
                    bro = ''
                    i = 1
                if('4, 2' in bro):
                    mouse.position = (520,560)
                    bro = ''
                    i = 1
                if('4, 3' in bro):
                    mouse.position = (880,560)
                    bro = ''
                    i = 1
                if('4, 4' in bro):
                    mouse.position = (1240,560)
                    bro = ''
                    i = 1
                if('5, 1' in bro):
                    mouse.position = (160,720)
                    bro = ''
                    i = 1
                if('5, 2' in bro):
                    mouse.position = (520,720)
                    bro = ''
                    i = 1
                if('5, 3' in bro):
                    mouse.position = (880,720)
                    bro = ''
                    i = 1
                if('5, 4' in bro):
                    mouse.position = (1240,720)
                    bro = ''
                    i = 1
                if(('left click') in bro or ('left-click') in bro):
                    mouse.click(Button.left,1)
                    bro = ''
                    i = 1
                if(('right click') in bro or ('right-click' in bro)):
                    mouse.click(Button.right,1)
                    bro = ''
                    i = 1
                if(('double click' in bro) or ('double-click' in bro)):
                    mouse.click(Button.left,2)
                    bro = ''
                    i = 1
                '''Additional mouse command'''
                if ('open file' in bro):
                    mouse.click(Button.left, 3)
                    bro = ''
                    i = 1
                ''' Keyboard command start here!!!!!!!!!!!!!!!!!!!'''
                if (('zoom in') in bro):
                    pyautogui.keyDown('cmd')
                    pyautogui.keyDown('+')
                    pyautogui.keyUp('+')
                    pyautogui.keyUp('cmd')
                    bro = ''
                    i = 1
                if (('zoom out') in bro):
                    pyautogui.keyDown('cmd')
                    pyautogui.keyDown('-')
                    pyautogui.keyUp('-')
                    pyautogui.keyUp('cmd')
                    bro = ''
                    i = 1
                if ('type' in bro):
                    audio2 = r.adjust_for_ambient_noise(source)        
                    print('Say what you would like to type')
                    audio2 = r.listen(source, phrase_time_limit = 2)
                    text2 = r.recognize_google(audio2)
                    print("You said : {}".format(text2))
                    bro2 = format(text2)
                    pyautogui.typewrite(bro2)
                    bro = ''
                    i = 1
                if ('enter' in bro):
                    pyautogui.keyDown('enter')
                    pyautogui.keyUp('enter')
                    bro = ''
                    i = 1
                if ('quit' in bro):
                    pyautogui.keyDown('cmd')
                    pyautogui.keyDown('w')
                    pyautogui.keyUp('w')
                    pyautogui.keyUp('cmd')
                    bro = ''
                    i = 1
                if('Instagram' in bro):
                    the_H.Instabot('theproject164' , 'project')
                    i = 1
                    bro = ""
                if('song' in bro):
                    the_H.youtube()
                    i = 1
                    bro = ""
                if('search for' in bro):
                    k = bro[11:]
                    p1 = the_H.youtube1()
                    p1.search(k)
                    i = 1
                    bro = ""
                if('close' in bro or 'shut up' in bro or 'shut down' in bro):
                    i = 1
                if(i == 0):
                    say("Not a valid command")
                else:
                    i = 0
            except:
                print("Sorry could not recognize what you said")
                say("Sorry could not recognize what you said")