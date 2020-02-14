#!/usr/bin/python3
from gpiozero import LED
from time import sleep
time_dot=0.1
time_dash=0.3
word_gap=0.7
char_gap=0.1
led=LED(4)   # physical pin 7
	
def dot():
	led.on()
	sleep(time_dot)
	led.off()
	sleep(char_gap)
def dash():
	led.on()
	sleep(time_dash)
	led.off()
	sleep(char_gap)
def a():
	dot();dash()
def b():
	dash();dot();dot();dot()
def c():
	dash();dot();dash();dot()
def d():
	dash();dot();dot()
def e():
	dot()
def f():
	dot();dot();dash();dot()
def g():
	dash();dash();dot()
def h():
	dot();dot();dot();dot()
def i():
	dot();dot()
def j():
	dot();dash();dash();dash()
def k():
	dash();dot();dash()
def l():
	dot();dash();dot();dot()
def m():
	dash();dash()
def n():
	dash();dot()
def o():
	dash();dash();dash()
def p():
	dot();dash();dash();dot()
def q():
	dash();dash();dot();dash()
def r():
	dot();dash();dot()
def s():
	dot();dot();dot()
def t():
	dash()
def u():
	dot();dot();dash()
def v():
	dot();dot();dot();dash()
def w():
	dot();dash();dash()
def x():
	dash();dot();dot();dash()
def y():
	dash();dot();dash();dash()
def z():
	dash();dash();dot();dot()
print ('Enter a sentence')
data=input()

funcList = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
for item in data :
	funcList[ord(item)-ord('a')]()
