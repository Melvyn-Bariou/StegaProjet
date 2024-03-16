#################################################
#Module_Stegano 
#Fait par Melvyn et Alexis
#################################################

from tkinter import *
from PIL import Image, ImageTk
from Module_Image import image_to_bin , convert_to_decimal

def get_lsb(liste_pixel):
    """
    Description : Prend le lsb de chaques valeurs binaires des pixels et les mets dans une liste
    
    Input :
    liste_pixel (list) : les 3 valeurs RGB du pixel dans une liste
    
    Output :
    lsb (list) : les lsb du pixel
    """
    binaire = [bin(x) for liste in liste_pixel for x in liste]
    lsb = [int(x[-1]) for x in binaire]
    return lsb


def convertir_bit_lettre(liste_bit):
    """
    Description : Convertit les bits récuprés lors de l'extraction du message dans l'images et convertit les bits en caractères
    afin de retrouver le message
    
    Input :
    liste_bit (list) : la liste des bits récupéré dans l'image
    
    Output :
    (str) : le message si il avait été incorporé avant dans l'image
    """
    message = []
    for i in range(0, len(liste_bit), 9):
        lettre = chr(int("".join(map(str, liste_bit[i:i+9])), 2))
        message.append(lettre)
    return "".join(message)

def bit_in_image(pixel , bit):
    """
    Description : Pour un pixel donnée en binaire , remplace le lsb du pixel par le bit du message a cacher
    
    Input :
    pixel (int) : valeur lsb du pixel a modifier
    bit (int) :  bit a mettre dans le lsb du pixel
    
    Output :
    (int) : le pixel avec le nouvel lsb
    """
    return (pixel // 10 * 10) + bit 

def string_to_binary(mot):
    """
    Description : Convertit une str , un mot en binaire    
    Input :
    mot (str) : le mot (message) de l'utilisateur
    
    Output :
    binary (list) : une liste contenant les valeurs binaires des lettres du mot
    """
    binary = [format(ord(char), '09b') for char in mot]
    binary = [int(bit) for b in binary for bit in b]
    return binary


def hide_lenmsg(image , bin_nbr):
    """
    Description : Cache la longueur du message en binaire sur les 3 premieres listes des pixels de l'image (dans le lsb toujours)
    Input :
    image (list) : l'image sous forme de liste de liste des valeurs RGB
    msg (list) : la longueur du message en binaire
    
    Output :
    new_image (list) : image modifiee avec la longueur du message sur les 3 premieres listes
    """
    new_image = []
    pixels = image
    message = bin_nbr
    while pixels:
        ligne = pixels.pop(0)
        ligne_temp = []
        while ligne:
            pixel = ligne.pop(0)
            if message:
                new_pixel = bit_in_image(pixel, message.pop(0))
            else:
                new_pixel = pixel
            ligne_temp.append(new_pixel)
        new_image.append(ligne_temp)
    return new_image

def create_new_img(image , msg ,index):
    """
    Description : Cache le message dans l'image a partir de la 4 e liste de la liste image (3 e indice) 
    Input :
    image (list) : l'image sous forme de liste de liste des valeurs RGB
    msg (list) : le message en binaire a cacher
    index (int) : le nombre indiquant la liste a partir duquel le programme peut commencer a rassembler les lsb du message
    
    Output :
    new_image (list) : image modifiee avec la longueur du message et le message cache
    """
    new_image = []
    pixels = image
    save_image_init = image
    save_list = []
    
    #le programme enleve les 3 premieres listes de l'image pour ne pas modifier la longueur binaire du message
    for i in range(index):
        save_list.append(pixels.pop(0)) 
    message = msg
    while pixels:
        ligne = pixels.pop(0)
        ligne_temp = []
        while ligne:
            pixel = ligne.pop(0)
            if message:
                new_pixel = bit_in_image(pixel, message.pop(0))
            else:
                new_pixel = pixel
            ligne_temp.append(new_pixel)
        new_image.append(ligne_temp)
   
    save_list.extend(new_image)
    return save_list

def bin_to_str(liste_binaire:list)->str:
    """
    Description : Convertit le code binaire des lettres en message
    
    Input :
    msg (list) : message binaire a convertir
    
    Output :
    message (str) : message qui a été convertit
    """
    message = ""
    for binary in liste_binaire:
        binnary_str = ''.join(str(b) for b in binary)
        
        lettre  = chr(int(binnary_str , 2))
        message += lettre 
    return message

def incorporer_message(image , msg , longueur_img , largeur_img):
    """
    Description : Cache le message dans les valeurs LSB  des pixels de l'image (Une des fonctions principale du projet)
    
    Input :
    msg (list) : message binaire a incorporer
    image (list) : liste contenant les valeurs RGB de chaque pixels en binaire
    
    Output :
    new_image (list): Image avec le message caché et la longueur du message aussi caché
    """
    
    message = string_to_binary(msg)
    longueur_img_msg = len(message)
    long_msg_in_bin = [int(x) for x in bin(longueur_img_msg)[2:].zfill(9)]
    binary_image = image_to_bin(image , longueur_img , largeur_img)
    
    int_list = []
    for bin_grp in binary_image:
        int_grp = []
        for binary in bin_grp:
            int_bin = int(binary.replace("0b", ""))
            int_grp.append(int_bin)
        int_list.append(int_grp)
    
    #on obtient l'image avec les valeurs de ses pixels rgb en binaire
    pixels = int_list
    
    #on incorpore le nbr de bits du message a recuprerer en binaire sous 9 bits dans les 3 premieres listes
    lenmsg = hide_lenmsg(pixels , long_msg_in_bin)
    
    #on incorpore le message dans l image a partir de la 3 eme liste
    new_image = create_new_img(lenmsg , message , 3)
    
    # la nouvelle image est reconvertie en décimal pour obtenir les nouvelles valeurs r,g,b des pixels
    new_image = convert_to_decimal(new_image)
    return new_image
    
    
def extraire_message(image_modifiee , longueur_img , largeur_img):
    """
    Description : Récupère le message qui est caché dans l'image (Une des autres fonctions principale du projet)
    
    Input :
    modified_image (list) : Image contenant le message
    
    Output :
    message (str) : le message qui a été trouvé dans l'image
    """
    save_list = []
    save_msg  = []
    binary_image = image_to_bin(image_modifiee ,longueur_img , largeur_img )
    
    int_list = []
    for bin_grp in binary_image:
        int_grp = []
        for b in bin_grp:
            int_bin = int(b.replace("0b", ""))
            int_grp.append(int_bin)
        int_list.append(int_grp)
    
    #on obtient l'image modifiee avec les valeurs des pixels en binaire
    pixels = int_list
    for i in range(3):
        save_list.append(pixels.pop(0))
    nbr_bin = get_lsb(save_list)
    #on obtient la longueur du message cachee dans les 3 premieres listes de l image 
    nbr_str = ''.join(str(x) for x in nbr_bin)
    nbr = int(nbr_str, 2)
 
    div_nbr = nbr%3 #on divise par 3 le nbr pour avoir le nombre exact de liste a recupérer car il y a 3 lsb a recuperer par pixels
    index_parcour = 0
    index_parcour = (nbr//3) 
    idx_parcour = index_parcour
    for i in range(idx_parcour):
        save_msg.append(pixels.pop(0))
    #on obtient les bits du message puis on les reconvertits en lettres pour obtenir le message cache    
    msg_bin = get_lsb(save_msg)
    message = convertir_bit_lettre(msg_bin)
    return message