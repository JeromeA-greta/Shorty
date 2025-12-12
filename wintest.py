# Fichier de test, s'il est présent dans le Github c'est que
# le gitignore n'a pas fait son taf ou que j'ai oublié de l'y ajouter

import os
from platformdirs import *
from win32com.client import Dispatch
nom = "truc" + ".lnk"
desktop = user_desktop_dir()
print(desktop)
path = os.path.join(desktop, nom)
print(path)
target = os.path.join(desktop, "rufus.exe")
print(target)
wDir = desktop
print(wDir)
icon = target
print(icon)

print(os.path.dirname(target))

# shell = Dispatch("WScript.Shell")
# raccourci = shell.CreateShortCut(path)
# raccourci.Targetpath = target
# raccourci.WorkingDirectory = wDir
# raccourci.IconLocation = icon
# raccourci.save()

# print(os.name)
# print(os.path.expanduser("~"))
# print(user_desktop_dir())
# if not os.path.isdir(os.path.expanduser("~")+"/shorty") :
#     print("Pas de dossier shorty")
#     os.mkdir(os.path.expanduser("~")+"/shorty")
# var1 = "1"
# var2 = "deux"
# print(var1)
# print(var2)
# if os.name == "nt" :
#     var1 = "un"
#     var2 = "2"
#     var3 = "Tr3"
# print(var1)
# print(var2)
# print(var3)