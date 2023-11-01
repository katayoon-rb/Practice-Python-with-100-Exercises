#Write a script that detects and prints out your monitor resolution

from screeninfo import get_monitors
print(get_monitors())

print("Width: %s,  Height: %s" % (get_monitors()[0].width, get_monitors()[0].height))
