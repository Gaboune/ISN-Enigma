from tkinter import *

def jaipasdidee(n):
    liste1=[23, 18, 6, 19, 1, 12, 5, 8, 24, 11, 16, 7, 25, 14, 3, 2, 13, 9, 22, 20, 10, 21, 26, 15, 17, 4]   # ces 5 listes correspondent aux 5 rotos prédéfinis
    liste2=[5, 15, 17, 26, 22, 23, 9, 14, 8, 1, 20, 16, 7, 18, 21, 3, 4, 19, 10, 6, 11, 2, 25, 13, 24, 12]
    liste3=[10, 22, 7, 19, 23, 15, 16, 6, 4, 18, 3, 2, 13, 11, 1, 9, 14, 24, 20, 17, 21, 26, 8, 5, 25, 12]
    liste4=[8, 25, 10, 5, 19, 6, 16, 2, 1, 7, 3, 23, 18, 26, 15, 9, 20, 17, 21, 24, 14, 22, 4, 11, 12, 13]
    liste5=[13, 25, 12, 24, 2, 17, 20, 8, 10, 22, 9, 26, 7, 19, 14, 1, 4, 21, 16, 18, 23, 11, 6, 3, 15, 5]
    rotor=[]
    if n==1:
        rotor=liste1
    elif n==2:
        rotor=liste2
    elif n==3:
        rotor=liste3
    elif n==4:
        rotor=liste4
    elif n==5:
        rotor=liste5
    return rotor

def chiffrealettre(chiffreentree):
    multiplicateur=int(chiffreentree/26)
    if chiffreentree<27 :
        lettresorti=chr(chiffreentree+64)
    elif chiffreentree%26==0 :
        lettresorti=chr(90)
    else :
        chiffreentree=chiffreentree-multiplicateur*26
        lettresorti=chr(chiffreentree+64)
    return lettresorti

def base26(chiffre):            #si 27 rentre, il sort un 1, transforme en base 26
    tempo=int((chiffre-1)/26)
    if tempo>0:
        chiffre=chiffre-tempo*26
    return chiffre


def lettreachiffre(lettredentree):
    lettredentree=lettredentree.upper()
    chiffresorti=ord(lettredentree)-64
    return chiffresorti

def coder():
    
    r1=int(Choixrotor.get())      # on récupère les choix rotor, cad quelle liste prédéfinie à quelle position
    r2=int(Choixrotor2.get())
    r3=int(Choixrotor3.get())
    
    rotor1=jaipasdidee(r1)
    rotor2=jaipasdidee(r2)
    rotor3=jaipasdidee(r3)
    
    rpos1=int(Positionrotor.get())
    rpos2=int(Positionrotor2.get())
    rpos3=int(Positionrotor3.get())
    
    
    tab1=Choixliason1.get()
    tab2=Choixliason2.get()
    tab3=Choixliason3.get()
    tab4=Choixliason4.get()
    tab5=Choixliason5.get()
    tab6=Choixliason6.get()
    tab7=Choixliason7.get()
    tab8=Choixliason8.get()
    tab9=Choixliason9.get()
    tab10=Choixliason10.get()
    tab11=Choixliason11.get()
    tab12=Choixliason12.get()
    tab13=Choixliason13.get()
    tab14=Choixliason14.get()
    tab15=Choixliason15.get()
    tab16=Choixliason16.get()
    tab17=Choixliason17.get()
    tab18=Choixliason18.get()
    tab19=Choixliason19.get()
    tab20=Choixliason20.get()
    
    phraseentre=messageentre.get()
    phraseentre=phraseentre.replace(" ","")
    
    phrasesorti=[]
    
    for i in range(len(phraseentre)):
        lettre=phraseentre[i]
        if lettre==tab1:                    #tableau de connection
            lettre=tab11
        elif lettre==tab2:                   
            lettre=tab12
        elif lettre==tab3:                   
            lettre=tab13
        elif lettre==tab4:                   
            lettre=tab14
        elif lettre==tab5:                   
            lettre=tab15
        elif lettre==tab6:                   
            lettre=tab16
        elif lettre==tab7:                   
            lettre=tab17
        elif lettre==tab8:                   
            lettre=tab18
        elif lettre==tab9:                   
            lettre=tab19
        elif lettre==tab10:                   
            lettre=tab20
        chiffre=lettreachiffre(lettre)
        chiffre=chiffre+rotor1[rpos1]
        chiffre=chiffre+rotor2[rpos2]
        chiffre=chiffre+rotor3[rpos3]
        rpos1=rpos1+1
        if rpos1==26:
            rpos1=0
            rpos2=rpos2+1
            if rpos2==26:
                rpos2=0
                rpos3=rpos3+1
        chiffre=base26(chiffre)
        lettre=chiffrealettre(chiffre)
        phrasesorti.append(lettre)
    messagesorti=Label(Mafenetre,width=110,text=phrasesorti)
    messagesorti.place(x=480,y=872)

def decoder():
    
    r1=int(Choixrotor.get())      # on récupère les choix rotor, cad quelle liste prédéfinie à quelle position
    r2=int(Choixrotor2.get())
    r3=int(Choixrotor3.get())
    
    rotor1=jaipasdidee(r1)
    rotor2=jaipasdidee(r2)
    rotor3=jaipasdidee(r3)
    
    rpos1=int(Positionrotor.get())
    rpos2=int(Positionrotor2.get())
    rpos3=int(Positionrotor3.get())
    
    tab1=Choixliason1.get()
    tab2=Choixliason2.get()
    tab3=Choixliason3.get()
    tab4=Choixliason4.get()
    tab5=Choixliason5.get()
    tab6=Choixliason6.get()
    tab7=Choixliason7.get()
    tab8=Choixliason8.get()
    tab9=Choixliason9.get()
    tab10=Choixliason10.get()
    tab11=Choixliason11.get()
    tab12=Choixliason12.get()
    tab13=Choixliason13.get()
    tab14=Choixliason14.get()
    tab15=Choixliason15.get()
    tab16=Choixliason16.get()
    tab17=Choixliason17.get()
    tab18=Choixliason18.get()
    tab19=Choixliason19.get()
    tab20=Choixliason20.get()
    
    phraseentre=messageentre.get()
    phrasesorti=[]
    
    for i in range(len(phraseentre)):
        lettre=phraseentre[i]
        
        chiffre=lettreachiffre(lettre)
        chiffre=chiffre-rotor3[rpos3]
        chiffre=chiffre-rotor2[rpos2]
        chiffre=chiffre-rotor1[rpos1]
        rpos1=rpos1+1
        if rpos1==26:
            rpos1=0
            rpos2=rpos2+1
            if rpos2==26:
                rpos2=0
                rpos3=rpos3+1
        chiffre=chiffre+26*3
        chiffre=base26(chiffre)
        lettre=chiffrealettre(chiffre)
        if lettre==tab11:                    #tableau de connection
            lettre=tab1
        elif lettre==tab12:                   
            lettre=tab2
        elif lettre==tab13:                   
            lettre=tab3
        elif lettre==tab14:                   
            lettre=tab4
        elif lettre==tab15:                   
            lettre=tab5
        elif lettre==tab16:                   
            lettre=tab6
        elif lettre==tab17:                   
            lettre=tab7
        elif lettre==tab18:                   
            lettre=tab8
        elif lettre==tab19:                   
            lettre=tab9
        elif lettre==tab20:                   
            lettre=tab10
        phrasesorti.append(lettre)
        
    messagesorti=Label(Mafenetre,width=110,text=phrasesorti)
    messagesorti.place(x=480,y=872)
    
    
# Création de la fenêtre principale #
Mafenetre = Tk()
Mafenetre.title('ENIGMA')
Mafenetre.geometry('1600x1000')
Mafenetre.config(background="grey")

# Création du bouton quitter #
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.place(x = 1500, y = 50)

# Création du Bouton Codage #
Boutoncoder = Button(Mafenetre, text ='Codage',width=15,font=(18),command=coder)
Boutoncoder.place(x=1200, y=800)
Boutoncoder.config(bg="saddle brown")

# Création du bouton décodage #
Boutondecoder = Button(Mafenetre, text ='Décodage',width=15,font=(18),command=decoder)
Boutondecoder.place(x=1380, y=800)
Boutondecoder.config(bg="saddle brown")

# Création des phrases de demande du rotor #
phrasechoix=Label(Mafenetre,text="Saisissez le premier rotor :",font=(15))
phrasechoix.config(background="grey")
phrasechoix.place(x=250,y=400)

phrasechoix2=Label(Mafenetre,text="Saisissez le deuxième rotor :",font=(15))
phrasechoix2.config(background="grey")
phrasechoix2.place(x=250,y=450)

phrasechoix3=Label(Mafenetre,text="Saisissez le troisième rotor :",font=(15))
phrasechoix3.config(background="grey")
phrasechoix3.place(x=250,y=500)

# Création des zones de saisie pour le choix des rotors #
Choixrotor=Entry(Mafenetre,width=4)
Choixrotor.place(x=455,y=401)

Choixrotor2=Entry(Mafenetre,width=4)
Choixrotor2.place(x=455,y=451)

Choixrotor3=Entry(Mafenetre,width=4)
Choixrotor3.place(x=455,y=501)

# Création des phrases de demande de la position des rotors #
phraseposition=Label(Mafenetre,text="Saisissez la première position :",font=(15))
phraseposition.config(background="grey")
phraseposition.place(x=250,y=599)

phraseposition2=Label(Mafenetre,text="Saisissez la première position :",font=(15))
phraseposition2.config(background="grey")
phraseposition2.place(x=250,y=649)

phraseposition3=Label(Mafenetre,text="Saisissez la première position :",font=(15))
phraseposition3.config(background="grey")
phraseposition3.place(x=250,y=699)

# Création des zones de saisie pour la position des rotors #
Positionrotor=Entry(Mafenetre,width=4)
Positionrotor.place(x=480,y=600)

Positionrotor2=Entry(Mafenetre,width=4)
Positionrotor2.place(x=480,y=650)

Positionrotor3=Entry(Mafenetre,width=4)
Positionrotor3.place(x=480, y=700)

# Création des zones de saisie pour les liaisons des rotors #
Choixliason1=Entry(Mafenetre,width=3)
Choixliason1.place(x=1035,y=400)
Choixliason2=Entry(Mafenetre,width=3)
Choixliason2.place(x=1035,y=425)
Choixliason3=Entry(Mafenetre,width=3)
Choixliason3.place(x=1035,y=450)
Choixliason4=Entry(Mafenetre,width=3)
Choixliason4.place(x=1035,y=475)
Choixliason5=Entry(Mafenetre,width=3)
Choixliason5.place(x=1035,y=500)
Choixliason6=Entry(Mafenetre,width=3)
Choixliason6.place(x=1035,y=525)
Choixliason7=Entry(Mafenetre,width=3)
Choixliason7.place(x=1035,y=550)
Choixliason8=Entry(Mafenetre,width=3)
Choixliason8.place(x=1035,y=575)
Choixliason9=Entry(Mafenetre,width=3)
Choixliason9.place(x=1035,y=600)
Choixliason10=Entry(Mafenetre,width=3)
Choixliason10.place(x=1035,y=625)
Choixliason11=Entry(Mafenetre,width=3)
Choixliason11.place(x=1085,y=400)
Choixliason12=Entry(Mafenetre,width=3)
Choixliason12.place(x=1085,y=425)
Choixliason13=Entry(Mafenetre,width=3)
Choixliason13.place(x=1085,y=450)
Choixliason14=Entry(Mafenetre,width=3)
Choixliason14.place(x=1085,y=475)
Choixliason15=Entry(Mafenetre,width=3)
Choixliason15.place(x=1085,y=500)
Choixliason16=Entry(Mafenetre,width=3)
Choixliason16.place(x=1085,y=525)
Choixliason17=Entry(Mafenetre,width=3)
Choixliason17.place(x=1085,y=550)
Choixliason18=Entry(Mafenetre,width=3)
Choixliason18.place(x=1085,y=575)
Choixliason19=Entry(Mafenetre,width=3)
Choixliason19.place(x=1085,y=600)
Choixliason20=Entry(Mafenetre,width=3)
Choixliason20.place(x=1085,y=625)

# Création de la phrase liaisons #
phrasedemandliaison=Label(Mafenetre,text="Etablir les 10 liaisons",font=(15))
phrasedemandliaison.config(background="grey")
phrasedemandliaison.place(x=1000,y=350)

# Création de la phrase de demande du message à coder ou décoder d'entré #
phrasemessageentre=Label(Mafenetre,text="Saisissez le message :",font=(15))
phrasemessageentre.config(background="grey")
phrasemessageentre.place(x=305,y=800)

# Création de la zone de saisie message à coder ou décoder #
messageentre=Entry(Mafenetre,width=110)
messageentre.place(x=480,y=802)

# Création de la phrase de demande du message codé ou décodé de sorti #
phrasemessagesorti=Label(Mafenetre,text="Voici le message :",font=(15))
phrasemessagesorti.config(background="grey")
phrasemessagesorti.place(x=337,y=870)

# Création de la zone de saisie message codé ou décodé de sorti #



# Création de la vérification de la clé #
phraseverification=Button(Mafenetre,text="Vérification de la clé : ",font=(18))
phraseverification.config(background="saddle brown")
phraseverification.place(x=640,y=400)

Mafenetre.mainloop()



















