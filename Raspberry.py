from num2words import num2words
from subprocess import call
import serial
from gtts import gTTS
import pygame
import lcd1
import time
ser = serial.Serial('/dev/ttyACM0',9600)
def vow():
    read_serial=ser.readline()
    s = str(read_serial)
    print(s)
    if s[2:7]=='00001':
        return "अ"
    if s[2:7]=='00010':
        return "आ"
    if s[2:7]=='00011':
        return "इ"
    if s[2:7]=='00100':
        return "ई"
    if s[2:7]=='00101':
        return "उ"
    if s[2:7]=='00110':
        return "ऊ"
    if s[2:7]=='00111':
        return "ऋ"
    if s[2:7]=='01000':
        return "ए"
    if s[2:7]=='01001':
        return "ऐ"
    if s[2:7]=='01010':
        return "ओ"
    if s[2:7]=='01011':
        return "औ"
    if s[2:7]=='01100':
        return "अं"
    if s[2:7]=='01101':
        return "अः"
def num():
    read_serial=ser.readline()
    s = str(read_serial)
    print(s)
    if s[2:7]=='00001':
        return "0"
    if s[2:7]=='00010':
        return "1"
    if s[2:7]=='00011':
        return "2"
    if s[2:7]=='00100':
        return "3"
    if s[2:7]=='00101':
        return "4"
    if s[2:7]=='00110':
        return "5"
    if s[2:7]=='00111':
        return "6"
    if s[2:7]=='01000':
        return "7"
    if s[2:7]=='01001':
        return "8"
    if s[2:7]=='01010':
        return "9"
    
def mat():
    read_serial=ser.readline()
    s = str(read_serial)
    print(s)
    if s[2:7]=='00001':
        return "ा"
    if s[2:7]=='00010':
        return "ी"
    if s[2:7]=='00011':
        return "ि"
    if s[2:7]=='00100':
        return "ु"
    if s[2:7]=='00101':
        return "ू"
    if s[2:7]=='00110':
        return "ो"
    if s[2:7]=='00111':
        return "ौ"
    if s[2:7]=='01000':
        return "े"
    if s[2:7]=='01001':
        return "ै"
    if s[2:7]=='01010':
        return "ॅ"

def prin(abc):
    tts=gTTS(text=abc, lang='en')
    tts.save("hello0.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("hello0.mp3")
    pygame.mixer.music.play()
    lcd1.lcd_init()
        #lcd1.lcd_byte(lcd1.LCD_LINE_1)
    lcd1.lcd_byte(lcd1.LCD_LINE_1, lcd1.LCD_CMD)
    lcd1.lcd_string( abc ,2)
        
def eng():
    s = str()
    x=' '
    a= str()
    while True:
        read_serial=ser.readline()
        s = str(read_serial)
        print(s)
#    while s[2:7] != '11111':
        if s[2:7] != '11111':    
            if s[2:7] =='00000':
                x="a"
                prin(x) 
            if s[2:7]=='00001':
                x="b"
                print("Hello1")
                prin(x)           
            if s[2:7]=='00010':
                x="c"
                print("Hello2")
                prin(x)
            if s[2:7]=='00011':
                x="d"
                print("Hello3")
                prin(x)
            if s[2:7]=='00100':
                x="e"
                print("Hello4")
                prin(x)
            if s[2:7]=='00101':
                x="f"
                print("Hello5")
                prin(x)
            if s[2:7]=='00110':
                x="g"
                print("Hello6")
                prin(x)
            if s[2:7]=='00111':
                x="h"
                print("Hello7")
                prin(x)
            if s[2:7]=='01000':
                x="i"
                print("Hello8")
                prin(x)
            if s[2:7]=='01001':
                x="j"
                print("Hello9")
                prin(x)
            if s[2:7]=='01010':
                x="k"
                print("Hello10")
                prin(x)
            if s[2:7]=='01011':
                x="l"
                print("Hello11")
                prin(x)
            if s[2:7]=='01100':
                x="m"
                print("Hello12")
                prin(x)
            if s[2:7]=='01101':
                x="n"
                print("Hello13")
                prin(x)
            if s[2:7]=='01110':
                x="o"
                print("Hello14")
                prin(x)
            if s[2:7]=='01111':
                x="p"
                print("Hello15")
                prin(x)
            if s[2:7]=='10000':
                x="q"
                print("Hello16")
                prin(x)
            if s[2:7]=='10001':
                x="r"
                print("Hello17")
                prin(x)
            if s[2:7]=='10010':
                x="s"
                print("Hello18")
                prin(x)
            if s[2:7]=='10011':
                x="t"
                print("Hello19")
                prin(x)
            if s[2:7]=='10100':
                x="u"
                print("Hello20")
                prin(x)
            if s[2:7]=='10101':
                x="v"
                print("Hello21")
                prin(x)
            if s[2:7]=='10110':
                x="w"
                print("Hello22")
                prin(x)
            if s[2:7]=='10111':
                x="x"
                print("Hello23")
                prin(x)
            if s[2:7]=='11000':
                x="y"
                print("Hello24")
                prin(x)
            if s[2:7]=='11001':
                x="z"
                print("Hello25")
                prin(x)
            if s[2:7]=='11010':
                x=num()
                print("Hello26")
                prin(x)
            if s[2:7]=='11011':
                x="1"
                print("Hello27")
                prin(x)
            if s[2:7]=='11100':
                x=" "
                print("Hello28")
                prin(x)
            if s[2:7]=='11101':
                x="Fan on"
                prin(x)
            if s[2:7]=='11110':
                prin("OFF")
                break
            a=a+x
            print(a)
#        elif s[2:7]=='11110':
##            x="OFF"
##            prin(x)
#            break
        else:
            tts=gTTS(text=a, lang='en')
            tts.save("hello0.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("hello0.mp3")
            pygame.mixer.music.play()
        
            lcd1.lcd_init()
        #lcd1.lcd_byte(lcd1.LCD_LINE_1)+
            lcd1.lcd_byte(lcd1.LCD_LINE_1, lcd1.LCD_CMD)
            lcd1.lcd_string( a ,2)
            time.sleep(15)
            x=' '
            a=' '

def hin():
    s = str()
    x='0'
    a= str()
    while True:
        read_serial=ser.readline()
        s = str(read_serial)
        print(s)
#    while s[2:7] != '11111':
        if s[2:7] != '11111':    
                                   if s[2:7] =='00000':
                                       x="क"
                                       print("Hello0")
                                       prin(x)
                                   if s[2:7]=='00001':
                                       x="ख"
                                       print("Hello1")
                                       prin(x)
                                   if s[2:7]=='00010':
                                       x="ग"
                                       print("Hello2")
                                       prin(x)
                                   if s[2:7]=='00011':
                                       x="घ"
                                       print("Hello3")
                                       prin(x)
                                   if s[2:7]=='00100':
                                       x="च"
                                       print("Hello4")
                                       prin(x)
                                   if s[2:7]=='00101':
                                       x="छ"
                                       print("Hello5")
                                       prin(x)
                                   if s[2:7]=='00110':
                                       x="ज"
                                       print("Hello6")
                                       prin(x)
                                   if s[2:7]=='00111':
                                       x="झ"
                                       print("Hello7")
                                       prin(x)
                                   if s[2:7]=='01000':
                                       x="ट"
                                       print("Hello8")
                                       prin(x)
#                                   if s[2:7]=='01001':
#                                       x="ठ"
#                                       print("Hello9")
#                                       prin(x)
                                   if s[2:7]=='01001':
                                       x="ड"
                                       print("Hello10")
                                       prin(x)
                                   if s[2:7]=='01010':
                                       x="ढ"
                                       print("Hello11")
                                       prin(x)
                                   if s[2:7]=='01011':
                                       x="त"
                                       print("Hello12")
                                       prin(x)
                                   if s[2:7]=='01100':
                                       x="थ"
                                       print("Hello13")
                                       prin(x)
                                   if s[2:7]=='01101':
                                       x="द"
                                       print("Hello14")
                                       prin(x)
                                   if s[2:7]=='01110':
                                       x="ध"
                                       print("Hello15")
                                       prin(x)
                                   if s[2:7]=='01111':
                                        x="न"
                                        print("Hello16")
                                        prin(x)
                                   if s[2:7]=='10000':
                                        x="प"
                                        print("Hello17")
                                        prin(x)
                                   if s[2:7]=='10001':
                                        x="ब"
                                        print("Hello18")
                                        prin(x)
                                   if s[2:7]=='10010':
                                        x="भ"
                                        print("Hello19")
                                        prin(x)
                                   if s[2:7]=='10011':
                                        x="म"
                                        print("Hello20")
                                        prin(x)
                                   if s[2:7]=='10100':
                                        x="य"
                                        print("Hello21")
                                        prin(x)
                                   if s[2:7]=='10101':
                                        x="र"
                                        print("Hello22")
                                        prin(x)
                                   if s[2:7]=='10110':
                                        x="ल"
                                        print("Hello23")
                                        prin(x)
                                   if s[2:7]=='10111':
                                        x="व"
                                        print("Hello24")
                                        prin(x)
                                   if s[2:7]=='11000':
                                        x="स"
                                        print("Hello25")
                                        prin(x)
                                   if s[2:7]=='11001':
                                        x="  "
                                        print("Hello26")
                                        prin(x)
                                   if s[2:7] =='11010':
                                        x=vow()
                                        print("Hello27")
                                        prin(x)
                                   if s[2:7]=='11011':
                                        x=mat()
                                        print("Hello28")
                                        prin(x)
                                   if s[2:7]=='11100':
                                        x=num()
                                        print("Hello29")
                                        prin(x)
                                   if s[2:7]=='11101':
                                        x=conse()
                                        print("Hello3")
                                        prin(x)
                                   a=a+x
                                   print(a)
        elif s[2:7]=='11110':
            z="OFF"
            prin(z)
            break                       
        else:
            tts=gTTS(text=a, lang='hi')
            tts.save("hello0.mp3")
            pygame.mixer.init()
            pygame.mixer.music.load("hello0.mp3")
            pygame.mixer.music.play()
        
            lcd1.lcd_init()
        #lcd1.lcd_byte(lcd1.LCD_LINE_1)
            lcd1.lcd_byte(lcd1.LCD_LINE_1, lcd1.LCD_CMD)
            lcd1.lcd_string( a ,2)
            time.sleep(6)
            x=' '
            a=' '

read_serial=ser.readline()
t = str(read_serial)
print(t[2:3])
if t[2:3]== "0" :
    y="ENGLISH"
    prin(y)
    eng()
else:
    y="HINDI"
    prin(y)
    hin()
