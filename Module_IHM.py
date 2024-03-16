####################################################
# Module IHM
# Fait par Melvyn
####################################################

from tkinter import *
from PIL import Image, ImageTk
from Module_Stegano import *
from tkinter import filedialog
import time

def init_fenetre():
    fen = Tk()
    #Configuration de la fenetre
    fen.title("Logiciel Steganographie réalisé par Melvyn et Alexis")
    fen.iconbitmap("icon.ico")
    fen.config(bg = "#F5F0F5")
    fen.geometry("1000x800") 
    fen.minsize(1000,800)
    fen.attributes("-fullscreen", True)
    longueur_ref = 450
    largeur_ref = 350
    
    #Creations des frames (cadres)
    Frame1 = Frame(fen , bg="#8F94A5" , height=largeur_ref , width = longueur_ref  , borderwidth = 10,relief=SUNKEN)
    Frame1.place(x = 20 , y = 100)
    
    Frame2 = Frame(fen , bg="#647782" , height=375 , width = 470 , borderwidth = 10,relief=SUNKEN)
    Frame2.place(x = 510 , y = 100)
    
    Frame3 = Frame(fen , bg="grey" , height=100 , width = 470 , borderwidth = 10,relief=SUNKEN)
    Frame3.place(x = 510 , y = 550)
    
    #############################
    #Les fonctions necessaires au fonctionnement de l interface
    #############################
    
    def ouvrir_image():
        """
        Description : Ouvre une fenetre pour choisir l'image et  sauvegarde le chemin de l'image a incorporer/extraire un message
        
        Output :
        chemin_image (str): le chemin de l'image a incorporer/extraire un message
        """
        global chemin_image
        #Le Format de l'image doit etre un .png et ne doit pas contenir d'alpha (de la transparence)
        image_path = filedialog.askopenfilename(initialdir = "Images/",title = "Choisissez un fichier", filetypes = (("fichiers png","*.png"),("all files","*.*")))
        if image_path:
            chemin_image = image_path
            afficher_new_imagev2(chemin_image)
            button1['state'] = NORMAL
            button2['state'] = NORMAL
            entry['state'] = NORMAL
            return chemin_image
    
    def recreer_image(liste_rgb_image1 , largeur , hauteur):
        """
        Description : Recrée une nouvelle image a partir des valeurs rgb des pixels de l'image modifiée par stéganographie
    
        Input :
        liste_rgb_image1 (list) : liste de liste des pixels de l'image
        largeur (int) : la largeur de l'image
        hauteur (int) : la hauteur de l'image
        
        Output :
        new_image (image): la nouvelle image recrée en ayant fait de la stéganographie
        """
        #On crée la nouvelle image a partir d une liste de liste des valeurs RGB des pixels
        new_image = Image.new("RGB", (largeur, hauteur))
        new_image.putdata([tuple(pixel) for pixel in liste_rgb_image1])
        
        #On change son orientation pour que l'image soit du bon sens
        new_image = new_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        new_image = new_image.transpose(Image.Transpose.ROTATE_270)
        
        time.sleep(1)
        new_image.save("new_image.png" , "png")
        time.sleep(1)
    
    def validation_entry(msg):
        """
        Description : Verifie si le texte/ message en entrée ne dépasse pas une longueur de 29 caractères
        
        Input :
        texte (str) : le message de l'utilisateur
        """
        if len(msg) >= 30:
            return False
        else:
            return True
    
    def on_button1_pressed():
        """
        Description : S'occupe d'appeler toutes les fonctions nécessaire pour cacher le message 
        Est appelée quand l'utilisateur a appuyé sur le bouton pour envoyer le message a cacher
        """
        montrer_saisie()
        message = entry.get() 
        image_to_modify = chemin_image
        img1_stega  = incorporer_message(image_to_modify, message , size_of_image[0] ,size_of_image[1])
        #On recrée l'image
        new_image = recreer_image(img1_stega , size_of_image[1] , size_of_image[0])
        afficher_new_image()
        entry.destroy()
        button1.destroy()
        button2.destroy()
    
    def on_button2_pressed():
        """
        Description : S'occupe d'appeler toutes les fonctions nécessaire pour extraire le message 
        Est appelée quand l'utilisateur a appuyé sur le bouton pour extraire le message d'une image
        """
        image_find_msg = chemin_image
        message = extraire_message(image_find_msg ,size_of_image[0] ,size_of_image[1] )
        label8 = Label(Frame3 , text = message , bg="#F5F0F5" , font=("Helvetica", 12) , wraplength=450)
        label8.pack()
        button2.destroy()
        entry.destroy()
        button1.destroy()
    
    def on_button3_pressed():
        """
        Description : S'occupe d'appeler toutes la fonction pour choisir une image dans l'ordinateur de l'utilisateur 
        Est appelée quand l'utilisateur a appuyé sur le bouton pour choisir une image
        """
        ouvrir_image()
        button3.destroy()
    
    def afficher_new_imagev2(chemin_fichier):
        """
        Description : Affiche une image dans une Frame a partir du chemin de l'image (Affiche la première image)
    
        Input :
        chemin_image (str) : le chemin de l'image
        
        Output :
        size_of_image (tuple): la taille de l'image (largeur,hauteur)
        """
        image_choosen = Image.open(chemin_fichier)
        global size_of_image
        size_of_image =  image_choosen.size
        
        image_choosen_resized = image_choosen.resize((longueur_ref  , largeur_ref), Image.Resampling.LANCZOS)
        global image_choosen2
        image_choosen2 =  ImageTk.PhotoImage(image_choosen_resized)
        
        #Affichage de la premiere Image
        label1 = Label(Frame1 , image = image_choosen2)
        label1.pack()
        
    def afficher_new_image():
        """
        Description : Affiche la deuxieme image
        """
        new_img  = Image.open("new_image.png")
        new_img_resize = new_img.resize((longueur_ref  , largeur_ref), Image.Resampling.LANCZOS)
        global new_image2
        new_image2 = ImageTk.PhotoImage(new_img_resize)
        
        label3 = Label(Frame2 , text = "L'image modifiée" , bg="#647782" , font=("Helvetica", 12))
        label3.pack()
        label2 = Label(Frame2 , image = new_image2)
        label2.pack()
             
    def montrer_saisie():
        """
        Description : Affiche le message a cacher entré par l'utilisateur 
        """
        texte = entry.get()  
        if len(texte) <=30:
            label5.config(text = texte)

    #Affichage du texte et des differents boutons
    
    label3 = Label(fen , text = "Réalisé par Melvyn et Alexis" , bg="#F5F0F5" , font=("Helvetica", 7))
    label3.place(x=20 , y=35)
    
    label4 = Label(fen , text = "Puis entrez un message a cacher dans l'image choisie : " , bg="#F5F0F5" , font=("Helvetica", 12, "bold"))
    label4.place(x=20 , y=550)
        
    entry = Entry(fen , bg = "#F5F0F5" , width = 50, state = DISABLED)
    entry.place(x=20 , y=595)
    entry.config(validate='key', validatecommand=(fen.register(validation_entry), '%P'))
    
    label5 = Label(fen , text="" , bg="#F5F0F5" , font=("Helvetica", 12))
    label5.place(x=46 , y = 650)
    
    label6 = Label(Frame1 , text = "L'image que vous avez choisi pour incorporer/extraire un message" , bg="#8F94A5" , font=("Helvetica", 12))
    label6.pack()
    
    label7 = Label(Frame3 , text = "Message caché dans l'image choisie" , bg="grey" , font=("Helvetica", 12) , width = 50)
    label7.pack()
    
    label8 = Label(fen , text = "Ou bien vérifiez si quelque chose ne se cache pas dans l'image :  " , bg="#F5F0F5" , font=("Helvetica", 12, "bold"))
    label8.place(x=20 , y=680)
    
    button1 = Button(fen , text="Cliquez ici pour cacher votre message !" , command = on_button1_pressed , font=("Helvetica", 12), state = DISABLED)    
    button1.place(x=20 , y = 625)
    
    button2 = Button(fen , text="Cliquez ici pour vérifier si un message se cache dans l'image" , command = on_button2_pressed , font=("Helvetica", 12) , state = DISABLED)    
    button2.place(x=20 , y = 725)
    
    button3 = Button(fen , text="Cliquez ici pour choisir une image" , command = on_button3_pressed , font=("Helvetica", 12))
    button3.place(x=20 , y = 500)
    
    #boucle de la fenetre , Ne pas toucher 
    fen.mainloop()  

init_fenetre()
