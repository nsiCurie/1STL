# coding: utf-8
# In[3]:

import matplotlib.pyplot as plt
import numpy as np

from tkinter import*
from tkinter import messagebox
from tkinter import Tk
from tkinter.messagebox import showerror


""" ______________________________________________________________________________________ """
""" Saisir ci-dessous les valeurs mesurées avec chacune des deux méthodes : valeurs notées """
""" avec le point et séparées par des virgules ! puis exécuter le programme                """
""" ______________________________________________________________________________________ """

f_autoll=[10.8,11.3,10.5,9.8,9.9,10.1]
f_Bessel=[11.0,11.2,11.1,10.9,11.0,11.1]


N_autocoll=len(f_autoll)
N_Bessel=len(f_Bessel)

if N_autocoll<2 and N_Bessel<2 :
    Tk_Appli = Tk()
    Tk_Appli.withdraw()
    showerror("Saisie incomplète", "Vous n'avez pas saisi suffisamment de valeurs ! \nAttention à utliser le point et non la virgule pour la saisie.")
    Tk_Appli.destroy()

else:
    f=plt.figure(figsize=(16,9))
    ax = f.add_subplot(111)
    f.patch.set_facecolor('#E0E0E0')
    ax.patch.set_facecolor('#525354')

    l1=f_autoll+f_Bessel
    plt.hist([f_autoll, f_Bessel],align = 'mid', range=(min(l1),max(l1)),bins=1+int((max(l1)-min(l1))*10),color=['#51BFCC','#F7B01D'])
    plt.ylabel('fréquence')
    plt.xlabel('distance focale')
    plt.grid(True)

    """ Statistiques méthode d'autocollimation : """
    if N_autocoll>2 :
        Moy_autocoll=np.mean(f_autoll)
        Sexp_autocoll=np.std(f_autoll, ddof = 1)
        Stat_autocoll= "Autocollimatiion : \n Nombre de valeurs :"+ str(N_autocoll)+"\n Valeur à retenir : " + str(Moy_autocoll) + "\n Ecart-type : "+str(Sexp_autocoll)
    else :
        Stat_autocoll="Autocollimation : pas assez de valeurs"
    """Statistiques méthode de Bessel : """
    if N_Bessel >1 :
        Moy_Bessel=np.mean(f_Bessel)
        Sexp_Bessel=np.std(f_Bessel, ddof = 1)
        Stat_Bessel= "Bessel : \n Nombre de valeurs :"+ str(N_Bessel)+"\n Valeur à retenir : " + str(Moy_Bessel) + "\n Ecart-type : "+str(Sexp_Bessel)
    else :
        Stat_Bessel="Bessel : pas assez de valeurs"

    plt.legend([Stat_autocoll,Stat_Bessel])
    plt.title("Mesure d'une distance focale par différentes méthodes")
    plt.show()


