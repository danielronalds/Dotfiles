#!/usr/bin/env python3

# Toggles floating mode for all new windows

from i3ipc import Connection, Event
import keyboard
import os

def SetFloating(i3, e):
	if floating:
		i3.command('floating enable')
	else:
		i3.command('floating disable')

def ToggleFloating():
	global floating
	floating = not floating	
	SendNotification()

def SendNotification():
	global floating
	if floating:
		message = "Floating enabled"
	else:
		message = "Floating disabled"	
	notification = "notify-send -t 1200 " + message
	os.system(notification)

floating = False 

i3 = Connection()
i3.on(Event.WINDOW_NEW, SetFloating)
keyboard.add_hotkey('ctrl+alt+f', lambda: ToggleFloating()) 
i3.main()
