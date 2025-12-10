from tkinter import *
from tkinter import filedialog as fd
from pathlib import Path
from PIL import Image, ImageTk
from platformdirs import *
import stat
import os
import time

# Fonctions<

def selFichier() : # Sélection du fichier
    nomFichier = fd.askopenfilename(#initialdir = '/home/'+user+'/bin/',
                                    initialdir = os.path.expanduser("~")+"/bin/",
                                    title = 'Fichier...',
                                    filetypes = (('AppImage', '*.AppImage'),
                                                 ('Script .sh', '*.sh'),
                                                 ('Tous types', '*')))
    chxExec.configure(text = nomFichier)

def selIcon() : # Sélection de l'image, qui sera traitée pour que sa taille soit 48x48
    global pathIcon
    global chxIcon
    nomIcon = fd.askopenfilename(initialdir = os.path.expanduser("~")+'/.icons/',
                                 title = 'Icône...',
                                 filetypes = (('Image PNG', '*.png'),
                                              ('Image JPG', '*.jpg'),
                                              ('Image JPEG', '*.jpeg'),
                                              ("Tous types", "*.*")))
    image = Image.open(nomIcon)
    modImage = image.resize((48, 48))
    img = ImageTk.PhotoImage(modImage)
    chxIcon.configure(image = img)
    chxIcon.image = img
    pathIcon = nomIcon
    print(pathIcon)

def genererRac() : # La génération du raccourci
    global nom
    global chxLaunch
    print(chxSave)
    nom = txtName.get()
    print(nom)
    texte = "[Desktop Entry]\nEncoding=UTF-8\nType=" + chxSave
    texte += "\nName=" + nom
    fichier = chxExec
    texte += "\nExec=" + chxExec.cget("text")
    texte += "\nIcon=" + pathIcon
    print(texte)

    pathRac = user_desktop_dir()+"/"+nom+".desktop"
    # Création du fichier si non existant, sinon écrase l'existant
    with open(user_desktop_dir()+"/"+nom+".desktop", "w", encoding="utf-8") as f :
        f.write(texte)
        
    file = Path(pathRac)
    file.chmod(file.stat().st_mode | stat.S_IEXEC)
    os.system("chmod +x "+pathRac) # Rend le raccourci exécutable (autorisation manuelle nécessaire sur Logique OS 0.1)

    chxLaunch = Toplevel(root) # Le choix d'ajouter le même raccourci dans la liste du lanceur GNOME
    chxLaunch.title = "Ajouter au lanceur"
    chxLaunch.geometry = "350x200"
    chxLaunch.resizable(False, False)
    lblChx = Label(chxLaunch, text = "Souhaitez-vous ajouter\nce raccourci dans le\nlanceur d'applications ?")
    lblChx.grid(column = 1, row = 0)
    btnOui = Button(chxLaunch, text = "Oui", command = ouiLanceur)
    btnOui.grid(column = 0, row = 1)
    btnNon = Button(chxLaunch, text = "Non", command = nonLanceur)
    btnNon.grid(column = 2, row = 1)

def choix(selChx) : # Choix du type, reçoit ledit type en paramètre
    global chxSave
    chxSave = selChx
    print(chxSave)

def ouiLanceur() : # Si on choisit d'ajouter au lanceur GNOME
    global nom
    nonLanceur()
    pathDesk = user_desktop_dir()+"/"+nom+".desktop"
    os.system("cp "+pathDesk+" /home/"+user+"/.local/share/applications/")
    time.sleep(1)
    os.system("update-desktop-database /home/"+user+"/.local/share/applications")
    info = Toplevel(root)
    info.title("Information")
    # info.geometry("150x80")
    info.resizable(False, False)
    lblInfo = Label(info, text = "Ajouté au lanceur !")
    lblInfo.grid(column = 0, row = 0)
    info.update()
    info.geometry(str(lblInfo.winfo_width())+"x70")
    btnInfo = Button(info, text = "Ok", command = info.destroy)
    btnInfo.grid(column = 0, row = 1)

def nonLanceur() :
    global chxLaunch
    chxLaunch.destroy()


# Création et aménagement de la fenêtre principale

root = Tk()
root.title("Shorty")

chxLaunch = ""
chxType = ["Application"] # Tableau contenant les types (Application, URL...)
chxDefaut = StringVar(root)
chxDefaut.set(chxType[0]) # Choix par défaut
chxSave = ""
pathIcon = ""
nom = ""
user = os.getlogin()
# bureau = os.system("xdg-user-dir DESKTOP")
# print(os.environ.get('XDG_USER_DIR'))

# root.geometry("300x350")
root.resizable(False, False)

lblVersion = Label(root, text = "0.2.1") # Numéro de version
lblVersion.grid(column = 0, row = 0)

# Type
lblType = Label(root, text = "Type : ")
lblType.grid(column = 0, row = 1)
chx = OptionMenu(root, chxDefaut, *chxType, command=choix) # Affichage de la liste des types
chx.grid(column = 1, row = 1)

# Nom du raccourci souhaité
lblName = Label(root, text = "Nom : ")
lblName.grid(column = 0, row = 2)
txtName = Entry(root, width = 20)
txtName.grid(column = 1, row = 2)

# Chemin vers l'exécutable
lblExec = Label(root, text = "Exécutable : ")
lblExec.grid(column = 0, row = 3)
chxExec = Label(root, text = "...", width = 15, height = 1)
chxExec.grid(column = 1, row = 3)
btnExec = Button(root, text = "...", command = selFichier)
btnExec.grid(column = 2, row = 3)

# Chemin vers l'icône
lblIcon = Label(root, text = "Icône : ")
lblIcon.grid(column = 0, row = 4)
affIcon = ""
chxIcon = Label(root, image = affIcon)
chxIcon.grid(column = 1, row = 4)
btnIcon = Button(root, text="...", command = selIcon)
btnIcon.grid(column = 2, row = 4)

# Bouton pour générer le raccourci, avec un choix derrière
btnGen = Button(root, text = "Générer", command = genererRac)
btnGen.grid(column=0, row=5)


root.mainloop()