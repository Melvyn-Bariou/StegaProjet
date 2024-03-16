#####################################################
# Module_Image
# Fait par Alexis et Melvyn
#####################################################

from PIL import Image, ImageTk

def image_to_bin(img , largeur , hauteur):
    """
    Description : Convertir les valeurs RGB de l'image en valeurs binaires
    
    Input :
    img (list) : l'image que l'on veut modifier
    largeur (int) : la largeur de l'image (width)
    hauteur (int) : la hauteur de l'image (height)
    
    Output :
    image_binaire (list) : une liste contenant les valeurs RVB des pixels de l image en binaire
    """
    image = Image.open(img)
    image_binaire = []
    for i in range(largeur):
        for j in range(hauteur):
            #Si il y a de l'alpha mais le projet ne prend pas en compte les images contenant de l'alpha
            #r ,v , b , a = image.getpixel((i,j))
            r ,v , b= image.getpixel((i,j))
            #binary_image.append([bin(r).replace("0b",""),bin(v).replace("0b",""),bin(b).replace("0b","")]) # possibilité d ajouter l alpha de l image car format png ! rajouter : ,a
            image_binaire.append([bin(r),bin(v),bin(b)])    
    return image_binaire
    
def convert_to_decimal(rgb_val):
    """
    Description : Convertit les valeurs RGB des pixels binaire en decimal
    
    Input :
    rgb_val (list) : une liste contenant les valeurs RGB des pixels de l image
    
    Output :
    rgb_new_img (list) : une liste contenant les valeurs RGB des pixels de l image en decimal
    """
    rgb_new_img =  [[int(str(x), 2) for x in couleur] for couleur in rgb_val]
    return rgb_new_img
                
def bin_to_image(img_bin):
    """
    Description : Convertit une liste de liste binaire de valeurs RGB en valeurs decimales
    
    Input :
    img_bin (list) : une liste contenant les valeurs RGB des pixels de l image
    
    Output :
    rgb_image (list) : une liste contenant les valeurs RGB des pixels de l image 
    """
    rgb_image = []
    for p in img_bin:
        r,v,b= p
        rbg_image.append([int(r,2),int(v,2),int(b,2)])
    return rbg_image
