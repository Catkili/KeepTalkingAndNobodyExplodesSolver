#!/usr/bin/env python
import sys
import os

#######################################################################################################
#######################################################################################################
###																								    ###
###																								    ###
###				Solveur pour Keep Talking and Nobody Explodes par Florian et Celia				    ###
###																								    ###
###																								    ###
#######################################################################################################
#######################################################################################################




########################################################################
#																	   #
#						 	Mot de passe							   #
#																	   #
########################################################################                   

def motDePasse():
	print("\t\tMot de Passe\n")
	listePrincipale = ["abats", "abime" ,"abois" ,"adieu", "delta"
						,"dense", "devin", "divin" ,"drame", "droit",
						"envol" ,"envie" ,"envoi", "erres" ,"essai",
						"fleur" ,"finit", "fiole", "kilos", "litre",
						"livre", "masse", "match", "matin", "mauve",
						"poser", "ports", "poule", "salir", "taire",
						"tarif", "tasse", "valve", "vanne", "vente"]
	alphabet = "abcdefghijklmnopqrstuvwxyz"				#Definition d'un alphabet pour verifier l'entrée utilisateur
	listeReponse = []
	lettres = str()

	while True :
		for iter in range (0,5):
			lettres = validerEntree(alphabet, Message ="Entre les \x1b[36m6 lettres\x1b[0m de la "+ str(iter+1) +" lettre, ou q pour quitter. Appuie sur Entree pour valider")
			if (lettres =='q'):
				return
			while (len(lettres)!=6):
				print("Le nombre de lettres n'est pas bon, recommence ! ")
				lettres = validerEntree(alphabet, MessagePerso = "\x1b[91mMauvaise saisie\x1b[0m, recommence ! \n")

			for mot in listePrincipale :
				for lettre in range(len(lettres)):
					if(mot[iter] == lettres[lettre]):
						if(mot not in listeReponse):
							listeReponse.append(mot)

			if len(listeReponse) > 1:
				print("\nListe des mots possibles : \n")
				for j in listeReponse :
					print(j)
				listePrincipale = listeReponse
				listeReponse = []
				print("\n")

			elif(len(listeReponse)) == 0:
				print("\x1b[91mErreur !\x1b[0m")
				listeReponse = []
				lettres = str()
				break

			else:
				clear()
				print("\n\x1b[92mLe mot est : "+listeReponse[0]+ '\x1b[0m\n')
				return

########################################################################
#																	   #
#						 	Fils Verticaux							   #
#																	   #
########################################################################                   

def filVerticaux():
	print("\t\tFils Verticaux \n")
	while(True):
		caracts = validerEntree("rbel","w", Message = "Tape à la suite, \x1b[91mr pour rouge, \x1b[36mb pour Bleu, \x1b[33me pour etoile, \x1b[37mw pour blanc et \x1b[90ml pour allumee\x1b[0m, ou rien, ou q pour quitter. Appuie sur Entree pour valider ")
		if(len(caracts) == 0):
			C()
		elif(len(caracts) == 1):
			if(caracts[0] == 'q'):
				return
			elif(caracts[0] == 'r'):
				S()
			elif(caracts[0] == 'b'):
				S()
			elif(caracts[0] == 'e'):
				C()
			elif(caracts[0] == 'l'):
				N()
			else:
				print("\x1b[91mErreur\x1b[0m\n")
				
		elif(len(caracts) == 2):
			if('r' in caracts and 'b' in caracts):
				S()
			elif('r' in caracts and 'e' in caracts):
				C()
			elif('r' in caracts and 'l' in caracts):
				B()
			elif('b' in caracts and 'e' in caracts):
				N()
			elif('b' in caracts and 'l' in caracts):
				P()
			elif('e' in caracts and 'l' in caracts):
				B()
			else:
				print("\x1b[91mErreur\x1b[0m\n")
				
		elif(len(caracts) == 3):
			if('r' in caracts and 'b' in caracts and 'e' in caracts):
				P()
			elif('r' in caracts and 'b' in caracts and 'l' in caracts):
				S()
			elif('b' in caracts and 'e' in caracts and 'l' in caracts):
				P()
			elif('r' in caracts and 'e' in caracts and 'l' in caracts):
				B()
			else:
				print("\x1b[91mErreur\x1b[0m\n")
		elif(len(caracts) == 4):
			N()
		else:
			print("\x1b[91mErreur\x1b[0m\n")
	
########################################################################
#																	   #
#						 	Suite de fonctions de 					   #
#								Fils Verticaux						   #
#																	   #
########################################################################                   
	
def S():
	if serial%2 == 0 : 
		print("\x1b[92mCoupe le fil\x1b[0m\n")
	else : 
		print("\x1b[91mNe coupe pas le fil\x1b[0m\n")	

def N():
	print("\x1b[91mNe coupe pas le fil\x1b[0m\n")
	
def C():
	print("\x1b[92mCoupe le fil\x1b[0m\n")
	
def P():
	if parallele == 'o' : 
		print("\x1b[92mCoupe le fil\x1b[0m\n")
	else : 
		print("\x1b[91mNe coupe pas le fil\x1b[0m\n")		

def B():
	if piles >= 2 : 
		print("\x1b[92mCoupe le fil\x1b[0m\n")
	else : 
		print("\x1b[91mNe coupe pas le fil\x1b[0m\n")	


########################################################################
#																	   #
#						 	Bouton									   #
#																	   #
########################################################################                   

def bouton():
	print("\t\tBouton\n")
	while(True):
		bouton = validerEntree("bwrjaem", Message = "Tape \x1b[94mb pour bleu, \x1b[37mw pour blanc, \x1b[91mr pour rouge et \x1b[93mj pour jaune \x1b[0mET A pour annuler, E pour Exploser, M pour Maintenir. Appuie sur Entree pour valider")
		if 'q' in bouton:
			return
		elif len(bouton) != 2 :
			print("\x1b[91mErreur !\x1b[0m\n")
		elif 'b' in bouton and 'a' in bouton :
			rube()
			return
		elif 'e' in bouton and piles>1:
			print("Appuie et lache\n")
			return
		elif 'w' in bouton and CAR == 'oui':
			rube()
		elif(FRK == 'o' and piles > 2):
			print("Appuie et lache\n")
			return
		elif('r' in bouton and 'm' in bouton):
			print("Appuie et lache\n")
			return
		else:
			rube()
			return
			
########################################################################
#																	   #
#						 	Rube									   #
#						dépendant de Bouton							   #
#																	   #
########################################################################                   
			
def rube():
	reponse = validerEntree("bjnwrq", Message = "Maintiens le bouton et donne la couleur : \x1b[94mb pour bleu, \x1b[37mw pour blanc, \x1b[91mr pour rouge et \x1b[93mj pour jaune \x1b[0m. Appuie sur Entree pour valider" )
	if len(reponse)!= 1:
		print("\x1b[91mErreur !\x1b[0m\n")
	elif(reponse == 'b'):
		print("Relache à \x1b[94m4\x1b[0m\n")
		return
	elif (reponse =='q'):
		return
	elif(reponse == 'j'):
		print("Relache à \x1b[94m5\x1b[0m\n")
		return
	else:
		print("Relache à \x1b[94m1\x1b[0m\n")
		return
			
			
########################################################################
#																	   #
#						 	Fils Horizontaux						   #
#																	   #
########################################################################                   
		
def filHorizontal():
	print("\t\tFils Horizontaux\n")
	fils = validerEntree("jbnrw",Message = "Rentrer les couleurs de fils dans l'ordre : \x1b[94mb pour bleu, \x1b[37mw pour blanc, \x1b[91mr pour rouge et \x1b[93mj pour jaune \x1b[0m et n pour noir. Appuie sur Entree pour valider")
	if('q' in fils):
		return
		
	elif(len(fils)==3):
		if('r' not in fils):
			print("Coupe le \x1b[94m2e\x1b[0m fil\n")
			return
		elif('w' == fils[2]):
			print("Coupe le \x1b[94mdernier\x1b[0m fil\n")
			return
		elif(fils.count('b')>=2):
			print("Coupe le \x1b[94mdernier fil bleu\x1b[0m\n")
			return
		else:
			print("Couper le \x1b[94mdernier\x1b[0m fil\n")
			return
			
	elif(len(fils)==4):
		if(fils.count('r')>1):
			if serial%2 == 1:
				print("Coupe le \x1b[91mdernier fil rouge\x1b[0m\n")
				return
		if(fils[3] == 'j'):
			if ('r' not in fils):
				print("Coupe le \x1b[94mpremier\x1b[0m fil\n" )
				return
		if(fils.count('b')==1):
			print("Coupe le \x1b[94mpremier\x1b[0m fil \n")
			return
		if(fils.count('j')>1):
			print("Coupe le \x1b[94mdernier\x1b[0m fil \n")
			return
		else : 
			print("Coupe le \x1b[94mdeuxieme\x1b[0m fil \n")
			return
			
	elif(len(fils)==5):
		if(fils[len(fils)-1]=='n'):
			if serial%2 == 1:
				print("Coupe le \x1b[94m4e\x1b[0m fil\n")
				return
		if(fils.count('j')>1 and fils.count('r')==1):
			print("Coupe le \x1b[94mpremier\x1b[0m fil\n")
			return
		if('n' not in fils):
			print("Couper le \x1b[94mdeuxieme\x1b[0m fil\n")		
			return
		else:
			print("Coupe le \x1b[94mpremier\x1b[0m fil \n")
			return
			
	elif(len(fils)==6):
		if('j' not in fils):
			if serial%2==1:
				print("Coupe le \x1b[94m3e\x1b[0m fil\n")
				return
		if(fils.count('j') == 1 and fils.count('w')>1 ):
			print("Coupe le \x1b[94m4e\x1b[0m fil\n")
			return
		if('r' not in fils):
			print("Coupe le \x1b[94mdernier\x1b[0m fil\n")
			return
		else:
			print("Coupe le \x1b[94m4e\x1b[0m fil\n")
			return
	else:
		print("\x1b[91mErreur\x1b[0m\n")


########################################################################
#																	   #
#						 	Jeux de mots    						   #
#																	   #
########################################################################                   

def jeuxDeMots():
	print("\t\tJeux de Mots\n")
	alphabet = "abcdefghijklmmnopqrstuvwxyz'"
	indi = 0
	while True:
		mot = validerEntree(alphabet, Message = "Rentre le mot. Appuie sur Entree pour valider")
		clear()
		if('q' in mot):
			break
		
		elif(mot == 'thon'):																		#En haut a gauche
			print("\x1b[94mHaut gauche\x1b[0m\n")
			mot_2()
			
		elif(mot == 'premier' or mot == 'ok' or mot == 'c'):										#En haut a droite
			print("\x1b[94mHaut droite\x1b[0m\n")
			mot_2()
								
		elif(mot == 'oui' or mot == 'mot' or mot == 'vert' or mot== 'rien'):		#Milieu gauche
			print("\x1b[94mMilieu gauche\x1b[0m\n")
			mot_2()
			
		elif(mot == 'vide' or mot == 'bouge' or mot == 'rouge' or mot == 'tes' or mot == 'ton' or mot == 'tons' or mot == 'vers'):				#milieu droite
			print("\x1b[94mMilieu droite\x1b[0m\n")
			mot_2()
			
		elif(mot == '' or mot == 'au' or mot == 'eau' or mot == 'haut'):	#Bas a gauche
			print("\x1b[94mBas gauche\x1b[0m\n")
			mot_2()
			
		elif(mot == '\x1b[94mverre' or mot == 'mots' or mot == 'non' or mot == 'maux' or mot == 't\'es' or mot == 'attends' or mot == "tu es" or mot == "c'est" or mot == 'ver' ):
			print("\x1b[94mBas droite\x1b[0m\n")
			mot_2()
			
		else :
			print("\x1b[91mErreur\x1b[0m\n")
			
########################################################################
#																	   #
#						mots_2 dépendant de 						   # 	
#							Jeux de mots    						   #
#																	   #
########################################################################
			
def mot_2():
	tableau = [["PRET", "OUI", "E", "EUX", "MILIEU", "GAUCHE", "APPUIE", "DROITE", "VIDE", "PRET", "NON", "PREMIER", "EUHHH", "RIEN", "ATTENDS"],
				["PREMIER", "GAUCHE", "E", "OUI", "MILIEU", "NON", "DROITE", "RIEN", "EUHHH", "ATTENDS", "PRET", "VIDE", "EUX", "APPUIE", "PREMIER"],
				["NON", "VIDE", "EUHHH", "ATTENDS", "PREMIER", "EUX", "PRET", "DROITE", "OUI", "RIEN", "GAUCHE", "APPUIE"," E", "NON", "MILIEU"],
				["VIDE", "ATTENDS", "DROITE", "E", "MILIEU", "VIDE", "APPUIE", "PRET", "RIEN", "NON", "EUX", "GAUCHE", "EUHHH", "OUI", "PREMIER"],
				["RIEN", "EUHHH", "DROITE", "E", "MILIEU", "OUI", "VIDE", "NON", "APPUIE", "GAUCHE", "EUX", "ATTENDS", "PREMIER", "RIEN", "PRET"],
				["OUI", "E", "DROITE", "EUHHH", "MILIEU", "PREMIER", "EUX", "APPUIE", "PRET", "RIEN", "OUI", "GAUCHE", "VIDE", "NON", "ATTENDS"],
				["EUX", "EUHHH", "EUX", "GAUCHE", "RIEN", "PRET", "VIDE", "MILIEU", "NON", "E", "PREMIER", "ATTENDS", "OUI", "APPUIE", "DROITE"],
				["EUHHH", "PRET", "RIEN", "GAUCHE", "EUX", "E", "OUI", "DROITE", "NON", "APPUIE", "VIDE", "EUHHH", "MILIEU", "ATTENDS", "PREMIER"],
				["GAUCHE", "DROITE", "GAUCHE", "PREMIER", "NON", "MILIEU", "OUI", "VIDE", "EUX", "EUHHH", "ATTENDS", "APPUIE", "PRET", "E", "RIEN"],
				["DROITE", "OUI", "RIEN", "PRET", "APPUIE", "NON", "ATTENDS", "EUX", "DROITE", "MILIEU", "GAUCHE", "EUHHH", "VIDE", "E", "PREMIER"],
				["MILIEU", "VIDE", "PRET", "E", "EUX", "RIEN", "APPUIE", "NON", "ATTENDS", "GAUCHE", "MILIEU", "DROITE", "PREMIER", "EUHHH", "OUI"],
				["E", "MILIEU", "NON", "PREMIER", "OUI", "EUHHH", "RIEN","ATTENDS", "E", "GAUCHE", "PRET", "VIDE", "APPUIE", "EUX", "DROITE"],
				["ATTENDS", "EUHHH", "NON", "VIDE", "E", "OUI", "GAUCHE", "PREMIER", "APPUIE", "EUX", "ATTENDS", "RIEN", "PRET", "DROITE", "MILIEU"],
				["APPUIE", "DROITE", "MILIEU", "OUI", "PRET", "APPUIE", "E", "RIEN", "EUHHH", "VIDE", "GAUCHE", "PREMIER", "EUX", "NON", "ATTENDS"],
				["TOI", "OK", "THON", "TON", "TONS", "SUIVANT", "AVANT", "T'ES", "MAINTIENS", "QUOI ?", "TOI", "QUOI", "COMME", "FAIT", "TES"],
				["THON", "TON", "SUIVANT", "COMME", "AVANT", "QUOI ?", "FAIT", "QUOI", "MAINTIENS", "TOI", "TES", "TONS", "OK", "T'ES", "THON"],
				["TON", "QUOI", "THON", "AVANT", "TON", "SUIVANT", "T'ES", "OK", "TES", "TONS", "TOI", "QUOI ?", "MAINTIENS", "COMME", "FAIT"],
				["TONS", "TOI", "TONS", "T'ES", "SUIVANT", "QUOI", "THON", "TES", "TON", "QUOI ?", "AVANT", "OK", "FAIT", "COMME", "MAINTIENS"],
				["T'ES", "FAIT", "TES", "T'ES", "AVANT", "QUOI ?", "OK", "TON", "MAINTIENS", "TONS", "COMME", "SUIVANT", "QUOI", "THON", "TOI"],
				["TES", "AVANT", "OK", "SUIVANT", "QUOI ?", "TONS", "T'ES", "QUOI", "FAIT", "TES", "TOI", "COMME", "MAINTIENS", "THON", "TON"],
				["AVANT", "AVANT", "TON", "THON", "TOI", "FAIT", "MAINTIENS", "QUOI", "SUIVANT", "OK", "COMME", "TONS", "T'ES", "TES", "QUOI ?"],
				["QUOI", "T'ES", "TES", "THON", "TONS", "SUIVANT", "QUOI", "FAIT", "TOI", "AVANT", "COMME", "TON", "OK", "MAINTIENS", "QUOI ?"],
				["QUOI ?", "TOI", "MAINTIENS", "TONS", "TON", "TES", "FAIT", "QUOI", "COMME", "THON", "AVANT", "T'ES", "SUIVANT", "QUOI ?", "OK"],
				["FAIT", "OK", "AVANT", "SUIVANT", "QUOI ?", "TON", "T'ES", "TONS", "MAINTIENS", "COMME", "TOI", "TES", "THON", "QUOI", "FAIT"],
				["SUIVANT", "QUOI ?", "AVANT", "QUOI", "TON", "MAINTIENS", "OK", "SUIVANT", "COMME", "FAIT", "THON", "T'ES", "TONS", "TES", "TOI"],
				["MAINTIENS", "THON", "TES", "FAIT", "QUOI", "TOI", "T'ES", "OK", "QUOI ?", "TONS", "SUIVANT", "MAINTIENS", "AVANT", "TON", "COMME"],
				["OK", "THON", "FAIT", "COMME", "TONS", "TOI", "MAINTIENS", "AVANT", "T'ES", "OK", "TES", "QUOI ?", "SUIVANT", "TON", "QUOI"],
				["COMME", "TONS", "SUIVANT", "TES", "T'ES", "MAINTIENS", "FAIT", "QUOI", "QUOI ?", "AVANT", "TOI", "COMME", "OK", "THON", "TON"]]

	alphabet = "abcdefghijklmmnopqrstuvwxyz'"
	while True :
		print("Rentre l'autre mot. Appuie sur Entree pour valider\n")
		mot_2 = validerEntree(alphabet).upper()

		if(len(mot_2)== 1 and 'Q' in mot_2):
			break
		for i in range(0,28):
			if(tableau[i][0] == mot_2):
				indi =1
				for j in range(1,14):
					print(tableau[i][j])

		if indi == 0 :
			print("\x1b[91mErreur ! \x1b[0m\n")
		elif indi == 1:			
			break
					  
########################################################################
#																	   #
#						 	Fils Diagonaux							   #
#																	   #
########################################################################                   
	
def filsDiagonaux():
	print("\t\tFils Diagonaux\n")
	compteurR = 0
	compteurB = 0
	compteurN = 0
	casR = ["c","b","a","ac","b", "ac","abc", "ab","b"]
	casB = ["b","ac","b","a","b","bc","c","ac","a"]
	casN = ["abc","ac","b","ac","b","bc","ab","c","c"]
	while True:
		print("Rentre la couleur puis la lettre. Appuie sur Entree pour valider.")
		lettres = validerEntree("abcrbn")
		if('q' in lettres):							#Cas d'exit
			return
		elif(lettres[0]== 'r'):						#Cas de la lettre R
			if(lettres[1] in casR[compteurR]):
				print("\n\x1b[92mCoupe le fil\x1b[0m\n")
			else:
				print("\n\x1b[91mNe coupe pas le fil\x1b[0m\n")
			compteurR += 1
		elif(lettres[0]== 'b'):						#Cas de la lettre B
			if(lettres[1] in casB[compteurB]):
				print("\n\x1b[92mCoupe le fil\x1b[0m\n")
			else:
				print("\n\x1b[91mNe coupe pas le fil\x1b[0m\n")
			compteurB += 1
		elif(lettres[0]== 'n'):						#Cas de la lettre N
			if(lettres[1] in casN[compteurN]):
				print("\n\x1b[92mCoupe le fil\x1b[0m\n")
			else:
				print("\n\x1b[91mNe coupe pas le fil\x1b[0m\n")
			compteurN += 1
		else:
			print('\x1b[91mErreur\x1b[0m\n')


########################################################################
#																	   #
#						 	Memory									   #
#																	   #
########################################################################                   

def memory() :
	print("\t\tMemory\n")
	memoire = [[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]] 							#Garde en memoire la position + le numero clique
	tableau = [['2p','2p', '3p','4p'],
				['4c','p1e','1p','p1e'],
				['c2e','c1e','3p','4c'],
				['p1e','1p','p2e','p2e'],
				['c1e','c2e','c4e','c3e']]											#A chaque etape, le bouton a cliquer en fonction de l'affichage: p=position, c=chiffre
	while True :																 	#pXe= position de l'etape X, cXe=meme chiffre qu'a l'etape X
		for etape in range(0,5): 																	#Etape par etape
			print("Quel est le \x1b[94mnumero\x1b[0m sur l'ecran ?")
			display = validerEntree("12345")
			if('q' in display): 																	
				return 																				#sortie
			display = int(display) 																		#convertit display en integer 

			if(len(tableau[etape][display-1]) == 2): 													#consigne pas besoin etapes precedentes	
				if ('p' in tableau[etape][display-1]): 													#consigne sur position
					print('Appuie sur le bouton en \x1b[94m'+ tableau[etape][display-1][0]+'e\x1b[0m \x1b[1mposition\x1b[0m\n') 
					memoire[etape][0] = int((tableau[etape][display-1])[0]) 							#On rentre dans la memoire la position cliquee
					if(etape != 4): 																	#On ne rentre pas en memoire la derniere etape
						memoire[etape][1] = validerEntree("1234", Message = "Quel est le \x1b[94mnumero\x1b[0m clique ?\n")					#Rentre en memoire le numero clique		
						if(memoire[etape][1] == 'q'): 												
							return 																	#On sort
						else : 
							memoire[etape][1] = int(memoire[etape][1])
				if ('c' in tableau[etape][display-1]): 												#Si la consiqne porte sur le numero
					print('Appuie sur le \x1b[1mnumero \x1b[94m' + tableau[etape][display-1][0]+'\x1b[0m\n') 				#On affiche la consigne
					memoire[etape][1] = int((tableau[etape][display-1])[0]) 							#On rentre en memoire le numero
					if(etape != 4): 																	#On ne rentre pas en memoire la derniere etape
						memoire[etape][0] = int(validerEntree("1234", Message = "Quel est la \x1b[94mposition\x1b[0m du numero clique ?\n")) #On rentre en memoire la position
						if(memoire[etape][1] == 'q'): 												#Condition de sortie
							return 																	
			else : 																					#Si on a besoin des etapes precedentes
				ancienne_etape = int((tableau[etape][display-1])[1])-1 								#On recupere l'etape dont on a besoin
				if('p' in tableau[etape][display-1]): 												#Si on a besoin de la position d'une etape precedente
					print('Appuie sur le chiffre en \x1b[94m' + str(memoire[ancienne_etape][0])+'e\x1b[1m position\x1b[0m\n')
					memoire[etape][0] = memoire[ancienne_etape][0] 									#On rentre en memoire la position
					if(etape != 4): 																	#On ne rentre pas en memoire la derniere etape
						memoire[etape][1] = int(validerEntree("1234", Message = "Quel est le \x1b[94mnumero\x1b[0m clique ?\n")) 				#On rentre en memoire le numero
						if(memoire[etape][1] == 'q'): 												#Sortie
							return
				if ('c' in tableau[etape][display-1]): 												#Si on a besoin du numero d'une etape precedente
					print('Appuie sur le \x1b[1mnumero \x1b[94m'+str(memoire[ancienne_etape][1])+'\x1b[0m\n') 				
					memoire[etape][1] = memoire[ancienne_etape][1] 									#On prend en memoire le chiffre
					if(etape != 4): 																	#On ne prend pas en memoire la derniere etape
						memoire[etape][0] = int(validerEntree("1234", Message = "Quel est la\x1b[94m position\x1b[0m du numero clique ?\n")) 	#On prend en memoire la position cliquee
						if(memoire[etape][1] == 'q'): 												
							return



########################################################################
#																	   #
#						 	Morse									   #
#																	   #
########################################################################                   

def morse(): 
	print("\t\tMorse\n")
	tableau = [[],[],[],[],[],[]] 																	#Tableau des sequences dans leur ordre d'apparition + indicateur de debut de mot
	tableauOrdonne=[[],[],[],[],[]] 																#Tableau des sequences dans le bon ordre, sans indicateur de debut de mot
	mot=[[],[],[],[],[]] 																			#Tableau des lettres dans le bon ordre
	mots = ['vitre',505,'ville',515,'chose',522,'signe',532,'ligne',542,'linge',535,'champ',545,'litre',552,'phase',555,'chaud',565,'bille',572,'balle', 575,'singe', 582,'plume',592,'pluie',595,'salle',600] #Tableau des mots associes a leurs frequences
	lettres = ['a','cl','b','lccc','c','lclc','d','lcc','e','c','f','cclc','g','llc',
			'h','cccc','i','cc','j','clll','k','lcl','l','clcc','m','ll','n','lc','o','lll','p','cllc','q',
			'llcl','r','clc','s','ccc','t','l','u','ccl','v','cccl'] 								#Tableau de correspondance lettre/sequence
	i = 0
	n = 0
	indicateur = 0																								#On compte le nombre de fois ou l'utilisateur rentre 'd'
	while True:
		tableau[i] = validerEntree("cld", Message = str(i+1)+"e lettre : Tape c pour court, l pour long et d pour debut du mot. Appuie sur Entree pour valider")
		while(len(tableau[i]) >1 and 'd' in tableau[i]):
			tableau[i] = validerEntree("cld", Message = "\x1b[91mOn ne peut pas combiner D avec L ou C\x1b[0m\n")
		if('q' in tableau[i]): 																		#La condition de sortie lorsqu'on doit recommencer
			return 																				
		if tableau[i] not in lettres :
		    tableau[i] = validerEntree("cld", Message = "\x1b[91mErreur : cette lettre n'existe pas, recommence cette saisie.\x1b[0m")
		if(tableau[i] == 'd'):																	#On verifie qu'il n'y ait pas plusieurs d
			indicateur += 1 
		i += 1																	
		if(indicateur == 2 ):																	#Si l'utilisateur rentre plusieurs fois l'indicateur de debut,
			clear()
			print('\x1b[91mErreur ! Tu as indique deux fois le debut. Recommence au depart\x1b[0m\n') 			
			tableau = [[],[],[],[],[],[]] 															#On vide le tableau
			i = 0
			indicateur = 0
																								#Si la sequence est correcte, on passe a la lettre suivante
		if(i == 6 and indicateur < 1):
			clear()
			print('\x1b[91mErreur ! Recommence depuis le debut\x1b[0m\n') 			
			tableau = [[],[],[],[],[],[]] 															#On vide le tableau
			i = 0
			indicateur = 0
					
		if (i==6 and indicateur == 1):																#Lorsqu'on a rentré toutes les sequences, on passe a la conversion
			for l in range(6): 																		#Ordonne et classe
				if(tableau[l] == 'd'): 																
					for j in range(5): 																
						tableauOrdonne[j] = tableau[(l+1+j)%6] 										
			for k in range(5): 																		#Convertit les séquences en lettres
				for m in range(len(lettres)): 														
						if( m%2==1 ): 																
							if(tableauOrdonne[k] == lettres[m]):									
								mot[k] = lettres[m-1]
			
			compteur = 0
			while( n == 0 ): 																	#Tant qu'on a pas trouve d'erreur
				for b in range(0,len(mots),2): 														#Parcours le tableau des mots
					z = 0																		#compteur compte le nombre d'occurence de bonnes lettres
					for j in mots[b]:															#Pour les lettre des mots
						if(j == mot[z]):																
							compteur += 1
							z += 1
						else:
							compteur = 0
							z=0
							break
					if(compteur == 5):
						print('\x1b[92m'+str(mots[b+1])+"\x1b[0m\n") 														#On affiche la frequence pour la radio
						return 																
				clear()
				print("\x1b[91mCe mot n'existe pas ! Recommence\x1b[0m\n") 							
				tableau = [[],[],[],[],[],[]] 											#On repart de zero
				i = 0 																	#On doit reprendre toutes les lettres
				n = 1 																	#On indique qu'il y a une erreur
				indicateur = 0			
				
			
			
			
			

							
							
########################################################################							
#							validerEntree							   #
########################################################################
# StringOk sont les caracteres autorisés							   #
# StringNotOk sont les caracteres non autorisés						   #
# Message est la String à afficher pour informer la saisie demandée	   #
# MessagePerso est la string personnalisée d'affichage d'erreur		   #
########################################################################

def validerEntree(StringOk="abcdefghijklmnopqrstuvwxz",StringNotOk="",Message="", MessagePerso="\x1b[91mErreur de saisie, recommencez.\x1b[0m\n"):
	if(len(Message) != 0):
		print(Message)
	bool = True
	while bool:
		entree = input().lower()
		if (len(entree)==1 and 'q' in entree):
			return entree
		for letters in entree :
			if(len(StringNotOk) != 0): 
				if(letters in StringNotOk):
					entree = entree.replace(letters,"")
					continue
			if(len(StringOk) != 0):
				if((letters not in StringOk)):	
					print(MessagePerso)
					bool = True
					break
				else:
					bool = False
	return entree
	
	
def clear():
	if(os.name == 'nt'):
		os.system('cls')
	else:
		os.system('clear')


########################################################################
#																	   #
#						 	Main									   #
#																	   #
########################################################################       
clear() 
print("\t*********** Keep Talking and Nobody Explodes ***********\n\nPour démarrer la partie, rentre les caracteristiques de la bombe :\n")           
 
serial = validerEntree("1234567890",Message="Quel est le \x1b[36m dernier chiffre du numero de serie\x1b[0m ? Appuie sur Entree pour valider :")
if('q' in serial):
	sys.exit()
else :
	serial = int(serial)

piles = validerEntree("1234567890", Message ="Combien y a-t-il de \x1b[36mpiles\x1b[0m ? Appuie sur Entree pour valider", MessagePerso="Erreur")
if 'q' in piles :
	sys.exit()
else :
	piles = int(piles)

parallele = validerEntree("on",Message = "Y a-t-il un \x1b[36mport parallele\x1b[0m ? (o/n) Appuie sur Entree pour valider")
if('q' in parallele ): 
	sys.exit()

FRK = validerEntree("on",Message="Y a-til un indicateur \x1b[36mFRK\x1b[0m \x1b[1mallume\x1b[0m ? (o/n) Appuie sur Entree pour valider")
if('q' in FRK): 
	sys.exit()

CAR = validerEntree("on",Message="Y a-t-il un indicateur \x1b[36mCAR\x1b[0m \x1b[1m allume\x1b[0m ? (o/n) Appuie sur Entree pour valider")
if('q' in CAR): 
	sys.exit()

clear()

while True:
	module = validerEntree("12345678",Message="Keep Talking, selectionne le module\n1 - Mot de passe\n2 - Bouton\n3 - Fils verticaux\n4 - Fils Horizontaux\n5 - Fils diagonaux\n6 - Jeux de mots\n7 - Memory\n8 - Morse\n", MessagePerso="Ce module n'existe pas ! Recommence\n")
	if('q' in module ):
		sys.exit()
	module=int(module)
	if module == 1:
	    clear()
	    motDePasse()
	elif module == 2:
	    clear()
	    bouton()
	elif module == 3:
	    clear()
	    filVerticaux()
	elif module == 4:
	    clear()
	    filHorizontal()
	elif module == 5:
	    clear()
	    filsDiagonaux()
	elif module == 6:
	    clear()
	    jeuxDeMots()
	elif module == 7 :
	    clear()
	    memory()
	elif module == 8:
	    clear()
	    morse()
	else:
		print("Erreur\n")


