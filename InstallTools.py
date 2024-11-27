# InstallTools.py

import platform
import os
import glob


OS = platform.system()
if OS == "Darwin": 				# Mac
	x = 1

elif OS == "Linux":
	x = 2

elif OS == "Windows":			
	x = 3
	