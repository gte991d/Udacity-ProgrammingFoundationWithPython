#Udacity - Programming Foundations with Python
#
#Assignment - Write a program that remind a friend to take a break every 2 hours by opening a
#webbrowser and playing a youtube song

import time
import webbrowser

total_break = 3
break_count = 0

print ("This program is started on "+time.ctime())
while (break_count < total_break):
    time.sleep(10) #time in seconds for testing
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    break_count = break_count + 1
