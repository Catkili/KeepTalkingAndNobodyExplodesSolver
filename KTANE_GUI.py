#coding: utf-8

import tkinter
import tkinter.font as tkFont


largeurBout = 15
hauteurBout = 2
margeX = 0
margeY = 0



	
#######################################################

class Ktane(tkinter.Tk):
	def __init__(self):
		tkinter.Tk.__init__(self)
		self.frame = None
		self.title("KTANE")
		#self.geometry("600x600")
		
		self.switch_frame(Menu)


	def switch_frame(self, frame_class):
		newFrame = frame_class(self)
		if(self.frame is not None):
			self.frame.grid_remove()
		self.frame = newFrame
		self.frame.grid(padx = 20, pady = 20, sticky = "ewsn")
		
#######################################################

class Menu(tkinter.Frame):

	def __init__(self, master):

		tkinter.Frame.__init__(self, master)

		tkinter.Frame.configure(self, bg = "white")
		#Infos de la bombe
		tkinter.Label(self, text="Info de la bombe",bg = "#97B7FF", fg = "white", width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY).grid(row = 0, column =0, sticky="EW")
		tkinter.Label(self, text="Numéro de série :",bg = "white", padx = margeX, pady = margeY).grid(row = 1, column =0)
		self.numero_serie = tkinter.IntVar()
		self.serial_entry = tkinter.Entry(self, textvariable = self.numero_serie, bg = "white", width= 15)
		self.serial_entry.grid(row = 2, column = 0)
		self.serial_entry.focus()
		self.aideImage2 = tkinter.PhotoImage(file = 'aide.png')
		self.aide2 = self.aideImage2.subsample(20,20)
		
		tkinter.Label(self, text="Nombre de piles :",bg = "white", padx = margeX, pady = margeY).grid(row = 3, column = 0)
		self.nb_piles = tkinter.IntVar()
		self.piles_entry = tkinter.Entry(self, textvariable = self.nb_piles, bg = "white", width=15)
		self.piles_entry.grid(row = 4, column = 0)

		self.parallele_v = tkinter.IntVar() 
		self.parallele_text = tkinter.Checkbutton(self, text = "Port parallèle", bg = "white", variable = self.parallele_v, padx = margeX, pady = margeY)
		self.parallele_text.grid(row = 5, column = 0)


		tkinter.Label(self, text="Indicateur FRK allumé?",bg = "white", padx = margeX, pady = margeY).grid(row = 6, column = 0)
		self.var_FRK = tkinter.StringVar()
		self.choix_oui = tkinter.Radiobutton(self, text="Oui", variable = self.var_FRK, value="o",bg = "white", padx = margeX, pady = margeY)
		self.choix_oui.grid(row = 7, column = 0, sticky="w")
		self.choix_non = tkinter.Radiobutton(self, text="Non", variable = self.var_FRK, value="n",bg = "white", padx = margeX, pady = margeY)
		self.choix_non.grid(row = 7, column = 0, sticky="e")

		tkinter.Label(self, text="Indicateur CAR allumé?",bg = "white", padx = margeX, pady = margeY).grid(row = 8, column = 0)
		self.var_CAR = tkinter.StringVar()
		self.choix_oui_CAR = tkinter.Radiobutton(self, text="Oui", variable = self.var_CAR, value="o",bg = "white", padx = margeX, pady = margeY).grid(row = 9, column = 0, sticky='w')
		self.choix_non_CAR = tkinter.Radiobutton(self, text="Non", variable = self.var_CAR, value="n",bg = "white", padx = margeX, pady = margeY).grid(row = 9, column = 0, sticky='e')
		self.bind("<Return>", self.valider)

		tkinter.Label(self, text="Menu",bg = "#97B7FF", fg = "white", width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY).grid(row = 0, column = 1, sticky="ew")
		self.fh = tkinter.Button(self, text="Fils Horizontaux", bg = "white", width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(FilsHorizontaux)])
		self.fh.grid(row = 1, column = 1, sticky="ew")
		self.fh.bind("<Return>", lambda event: [self.valider(), master.switch_frame(FilsHorizontaux)] )
		self.fd = tkinter.Button(self, text="Fils Diagonaux", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(FilsDiagonaux)])
		self.fd.grid(row = 2, column = 1, sticky="ew")
		self.fd.bind("<Return>", lambda event: [self.valider(), master.switch_frame(FilsDiagonaux)] )
		self.fv = tkinter.Button(self, text="Fils Verticaux", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(FilsVerticaux)])
		self.fv.grid(row = 3, column = 1, sticky="ew")
		self.fv.bind("<Return>", lambda event: [self.valider(), master.switch_frame(FilsVerticaux)] )
		self.me = tkinter.Button(self, text="Memory", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(Memory)])
		self.me.grid(row = 4, column = 1, sticky="ew")
		self.me.bind("<Return>", lambda event: [self.valider(), master.switch_frame(Memory)] )
		self.jdm = tkinter.Button(self, text="Jeux de Mots", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(JeuxDeMots)])
		self.jdm.grid(row = 5, column = 1, sticky="ew")
		self.jdm.bind("<Return>", lambda event: [self.valider(), master.switch_frame(JeuxDeMots)] )
		self.mdp = tkinter.Button(self, text="Mots de Passe", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(MotDePasse)])
		self.mdp.grid(row = 6, column = 1, sticky="ew")
		self.mdp.bind("<Return>", lambda event: [self.valider(), master.switch_frame(MotsDePasse)] )
		self.mo = tkinter.Button(self, text="Morse", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(Morse)])
		self.mo.grid(row = 7, column = 1, sticky="ew")
		self.mo.bind("<Return>", lambda event: [self.valider(), master.switch_frame(Morse)] )
		self.b = tkinter.Button(self, text="Boutons", bg = "white",width = largeurBout, height = hauteurBout, padx = margeX, pady = margeY, command=lambda: [self.valider(), master.switch_frame(Boutons)])
		self.b.grid(row = 8, column = 1, sticky="ew")
		self.b.bind("<Return>", lambda event: [self.valider(), master.switch_frame(Boutons)] )
		tkinter.Button(self, image = self.aide2, command = lambda : self.menuAide()).grid(row = 0, column = 2, sticky = 'e')

	def get_entry_serial(self):
		global serial
		serial = int(self.serial_entry.get())
		return serial
		
	def get_entry_piles(self):
		global piles
		piles = int(self.piles_entry.get())
		return piles

	def get_parallele(self):
		global parallele
		parallele = self.parallele_v.get()
		return parallele
		
	def get_FRK(self):
		global FRK
		FRK = self.var_FRK.get()
		return FRK
	
	def get_CAR(self):
		global CAR
		CAR = self.var_CAR.get()
		return CAR
		
	def valider(self):
		self.get_entry_serial()
		self.get_entry_piles()
		self.get_parallele()
		self.get_FRK()
		self.get_CAR()


	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		tkinter.Label(self.menuAide, text = "Désamorcer des bombes", font = ("Calibri", 20)).grid()
		tkinter.Label(self.menuAide, text = "Une bombe explose quand son compte à rebours atteint 0:00 ou quand trop d'erreurs ont été commises. \n Le seul moyen de désamorcer une bombe avant qu'elle n'explose est de désarmer chaque module séparément avant que le compte à rebours ne se termine. \n Chaque bombe aura jusqu'à 11 modules qui devront être désarmés. Chaque module est indépendant et peut être désarmé dans n'importe quel ordre. \n Les instructions pour désarmer les modules peuvent être trouvées dans la Section 1.\n Les modules 'Demandants' sont une exception et sont décrits dans la Section 2.").grid()
		tkinter.Label(self.menuAide, text = "Erreurs", font = ("Calibri", 20)).grid()
		tkinter.Label(self.menuAide, text = "Si le désamorceur fait une erreur, la bombe enregistre une erreur qui est montrée au-dessus du compte à rebours. \n Les bombes avec un compteur d'erreur exploseront à la troisième erreur. \n Le compte à rebours ira plus vite à chaque erreur commise. \n S'il n'y a pas d'indicateur d'erreur au-dessus du compte à rebours, la bombe explosera à la première faute commise, ne laissant aucune place à l'erreur.").grid()
		tkinter.Label(self.menuAide, text = "Obtenir des informations", font = ("Calibri", 20)).grid()
		tkinter.Label(self.menuAide, text = "Certaines instructions pour désarmer des modules nécessiteront des informations spécifiques sur la bombe, comme le numéro de série. \n Ce type d'information se trouve typiquement sur les côtés de la bombe. \n Se référer aux annexes A, B et C pour plus d'informations d'identification qui seront utiles pour désarmer certains modules.").grid()
		return


#######################################################

class FilsHorizontaux(tkinter.Frame):

	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		fontStyle = tkFont.Font( size=20)
		tkinter.Label(self, text="Fils Horizontaux", font = fontStyle ).grid(row = 0, column = 0, columnspan = 2)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 4, column = 1, sticky = 'W')
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0, columnspan = 2)
		self.consigne.set("Rentrer les couleurs de fils dans l'ordre : \n b pour bleu, w pour blanc, r pour rouge, j pour jaune et n pour noir.")
		
		self.fils_1 = tkinter.StringVar()
		self.fils_entry = tkinter.Entry(self, textvariable = self.fils_1)
		self.fils_entry.grid(row = 2, column = 0, sticky = 'EW')
		self.fils_entry.focus()
		
		self.valider = tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout,  command = lambda : [self.get_entry_fils()]).grid(row = 2, column = 1, sticky = 'W')
		
		tkinter.Button(self, text = "Recommencer", width = largeurBout, height = hauteurBout, command = lambda : [self.fils_entry.delete(0, tkinter.END), self.result.destroy()]).grid(row = 4, column =0, sticky = 'W')
		
		self.fils_entry.bind('<Return>', lambda event : self.get_entry_fils())
		self.result = tkinter.StringVar()
		self.result_text = tkinter.Label(self, textvariable = self.result, justify = tkinter.LEFT)
		self.result_text.grid(row = 3, column = 0, sticky = 'W')
		self.result.set("Solution: ")

	def get_entry_fils(self):
		self.fils = self.fils_1.get().lower()
		self.filHorizontal()

	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Un module de fils peut contenir entre 3 et 6 fils. \n Seulement un fil a besoin d'être coupé pour désarmer le module. \n Les fils sont ordonnés de haut en bas."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return

	def filHorizontal(self):
		if(len(self.fils)==3):
			if('r' not in self.fils):
				self.result.set("Solution: Coupe le 2e fil")
			elif('w' == self.fils[2]):
				self.result.set("Solution: Coupe le dernier fil")
			elif(self.fils.count('b')>=2):
				self.result.set("Solution: Coupe le dernier fil bleu")
			else:
				self.result.set("Solution: Coupe le dernier fil")
		elif(len(self.fils)==4):
			if(self.fils.count('r')>1):
				if serial%2 == 1:
					self.result.set("Solution: Coupe le dernier fil rouge")
			elif(self.fils[3] == 'j'):
				if ('r' not in self.fils):
					self.result.set("Solution: Coupe le premier fil")
			elif(self.fils.count('b')==1):
				self.result.set("Solution: Coupe le premier fil")
			elif(self.fils.count('j')>1):
				self.result.set("Solution: Coupe le dernier fil")
			else : 
				self.result.set("Solution: Coupe le 2e fil")
		elif(len(self.fils)==5):
			if(self.fils[len(self.fils)-1]=='n'):
				if serial%2 == 1:
					self.result.set("Solution: Coupe le 4e fil")
			elif(self.fils.count('j')>1 and self.fils.count('r')==1):
				self.result.set("Solution: Coupe le premier fil")
			elif('n' not in self.fils):
				self.result.set("Solution: Coupe le 2e fil")
			else:
				self.result.set("Solution: Coupe le premier fil")
		elif(len(self.fils)==6):
			if('j' not in self.fils):
				if serial%2==1:
					self.result.set("Solution: Coupe le 3e fil")
			elif(self.fils.count('j') == 1 and self.fils.count('w')>1 ):
				self.result.set("Solution: Coupe le 4e fil")
			elif('r' not in self.fils):
				self.result.set("Solution: Coupe le dernier fil")
			else:
				self.result.set("Solution: Coupe le 4e fil")
		else:
			self.result.set("Solution: Erreur")

#######################################################

class FilsDiagonaux(tkinter.Frame):
	compteurR = 0
	compteurB = 0
	compteurN = 0
		
	def __init__(self, master):
		fontStyle = tkFont.Font( size=20)
		tkinter.Frame.__init__(self, master)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		tkinter.Label(self, text="Fils Diagonaux", font = fontStyle).grid(row = 0, column = 0, columnspan = 2)
		tkinter.Label(self, text = "Rentre la couleur puis la lettre.", justify = tkinter.LEFT).grid(row = 1, column = 0, columnspan = 2)
		self.textResult = tkinter.StringVar()
		self.result = tkinter.Label(self, textvariable = self.textResult)
		self.result.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
		self.textResult.set("Solution: ")
		
		self.fils_d = tkinter.StringVar()
		self.fils_entry_d = tkinter.Entry(self, textvariable = self.fils_d, width=10)
		self.fils_entry_d.grid(row = 2, column = 0)
		self.fils_entry_d.focus()
		
		self.valider = tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.get_entry_fils_d(), self.fils_entry_d.delete(0, tkinter.END)]).grid(row = 2, column = 1, sticky = 'W')
		
		tkinter.Button(self, text = "Recommencer", width = largeurBout, height = hauteurBout, command = lambda : self.recommencer()).grid(row = 4, column =0, sticky = 'W')
		
		self.fils_entry_d.bind('<Return>', lambda event : [self.get_entry_fils_d(), self.fils_entry_d.delete(0, tkinter.END)])
		
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 4, column = 1)
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
	
	def recommencer(self):
		self.textResult.set("Solution: ")
		self.compteurR = 0
		self.compteurB = 0
		self.compteurN = 0

	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Sur ce module, il y a plusieurs panneaux contenant des fils mais seulement un panneau est visible à la fois.\n  Passer au panneau suivant en appuyant sur la flèche du bas et au panneau précédent avec la flèche du haut. \n Couper tous les fils du panneau qui doivent être coupés, avant de passer au suivant."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return


	def get_entry_fils_d(self):
		self.lettres = self.fils_d.get().lower()
		self.filsDiagonaux()

		
		
	def filsDiagonaux(self):
		casR = ["c","b","a","ac","b", "ac","abc", "ab","b"]
		casB = ["b","ac","b","a","b","bc","c","ac","a"]
		casN = ["abc","ac","b","ac","b","bc","ab","c","c"]
		if(self.lettres[0]== 'r'):						#Cas de la lettre R
			if(self.lettres[1] in casR[self.compteurR]):
				self.textResult.set("Solution: Coupe le fil")
			else:
				self.textResult.set("Solution: Ne coupe pas le fil")
			self.compteurR += 1
		elif(self.lettres[0]== 'b'):						#Cas de la lettre B
			if(self.lettres[1] in casB[self.compteurB]):
				self.textResult.set("Solution: Coupe le fil")
			else:
				self.textResult.set("Solution: Ne coupe pas le fil")
			self.compteurB += 1
		elif(self.lettres[0]== 'n'):						#Cas de la lettre N
			if(self.lettres[1] in casN[self.compteurN]):
				self.textResult.set("Solution: Coupe le fil")
			else:
				self.textResult.set("Solution: Ne coupe pas le fil")
			self.compteurN += 1
		else:
			self.textResult.set("Solution: Erreur")
			
#######################################################

class FilsVerticaux(tkinter.Frame):
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		fontStyle = tkFont.Font( size=20)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		tkinter.Label(self, text="Fils Verticaux", font = fontStyle).grid(row = 0, column = 0, columnspan = 2)
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 4, column = 1, sticky = 'w')
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0)
		self.consigne.set("Tape à la suite : \n R - Rouge, B - Bleu, W - blanc \n E - Etoile, L - allumee, ou rien")
		self.result = tkinter.StringVar()
		self.textResult = tkinter.Label(self, textvariable = self.result)
		self.textResult.grid(row = 3, column = 0)
		tkinter.Label(self, text = "Solution:").grid(row = 3, column = 0, sticky = 'w')
		
		self.fils_v = tkinter.StringVar()
		self.fv_entry = tkinter.Entry(self, textvariable = self.fils_v)
		self.fv_entry.grid(row = 2, column = 0)
		self.fv_entry.bind('<Return>', lambda event : [self.get_entry_fv(), self.fv_entry.delete(0, tkinter.END)])
		self.fv_entry.focus()
		
		self.valider = tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.get_entry_fv(), self.fv_entry.delete(0, tkinter.END)]).grid(row = 2, column = 1, sticky = 'W')
		
	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Regarder chaque fil : il y a une lumière au-dessus et de l'espace pour le symbole « ★ » sous le fil. \n Pour chaque combinaison de fil/lumière/symbole, rentrer la combinaison pour savoir s'il faut couper le fil ou non. \n Chaque fil peut être rayé de multiples couleurs."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return

	
	def get_entry_fv(self):
		self.caracts = self.fils_v.get().lower()
		self.filVerticaux()
		
	def S(self):
		if(serial%2 == 0) : 
			self.result.set("Coupe le fil")
		else : 
			self.result.set("Coupe le fil")

	def N(self):
		self.result.set("Ne coupe pas le fil")
		
	def C(self):
		self.result.set("Coupe le fil")
		
	def P(self):
		if parallele == 1 : 
			self.result.set("Coupe le fil")
		else : 
			self.result.set("Ne coupe pas le fil")		

	def B(self):
		if piles >= 2 : 
			self.result.set("Coupe le fil")
		else : 
			self.result.set("Ne coupe pas le fil")


		
	def filVerticaux(self):
		if(len(self.caracts) == 0):
			self.C()
		elif(len(self.caracts) == 1):
			if(self.caracts[0] == 'r'):
				self.S()
			elif(self.caracts[0] == 'b'):
				self.S()
			elif(self.caracts[0] == 'e'):
				self.C()
			elif(self.caracts[0] == 'l'):
				self.N()
			else:
				self.result.set("Erreur")
				
		elif(len(self.caracts) == 2):
			if('r' in self.caracts and 'b' in self.caracts):
				self.S()
			elif('r' in self.caracts and 'e' in self.caracts):
				self.C()
			elif('r' in self.caracts and 'l' in self.caracts):
				self.B()
			elif('b' in self.caracts and 'e' in self.caracts):
				self.N()
			elif('b' in self.caracts and 'l' in self.caracts):
				self.P()
			elif('e' in self.caracts and 'l' in self.caracts):
				self.B()
			else:
				self.result.set("Erreur")
				
		elif(len(self.caracts) == 3):
			if('r' in self.caracts and 'b' in self.caracts and 'e' in self.caracts):
				self.P()
			elif('r' in self.caracts and 'b' in self.caracts and 'l' in self.caracts):
				self.S()
			elif('b' in self.caracts and 'e' in self.caracts and 'l' in self.caracts):
				self.P()
			elif('r' in self.caracts and 'e' in self.caracts and 'l' in self.caracts):
				self.B()
			else:
				self.result.set("Erreur")
		elif(len(self.caracts) == 4):
			self.N()
		else:
			self.result.set("Erreur")


			
#######################################################

class Memory(tkinter.Frame):
	def __init__(self, master):
		fontStyle = tkFont.Font( size=20)
		self.compteur = 0
		self.memoire = [[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]] 							#Garde en memoire la position + le numero clique
		self.tableau = [['2p','2p', '3p','4p'],
					['4c','p1e','1p','p1e'],
					['c2e','c1e','3p','4c'],
					['p1e','1p','p2e','p2e'],
					['c1e','c2e','c4e','c3e']]
		tkinter.Frame.__init__(self, master)
		self.etape = 0
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		tkinter.Label(self, text="Memory", font = fontStyle).grid(row = 0, column = 0, columnspan = 2)
		self.consigne = tkinter.StringVar()
		self.consigne.set("Quel est le numéro affiché ? \n ")
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0)
		self.memory_var = tkinter.StringVar()
		self.memoryEntry = tkinter.Entry(self, textvariable = self.memory_var)
		self.memoryEntry.grid(row = 2, column = 0, sticky = 'w')
		self.memoryEntry.focus()
		self.memoryEntry.bind("<Return>", lambda event : [self.memory(), self.memoryEntry.delete(0, tkinter.END)])
		tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.memory(), self.memoryEntry.delete(0, tkinter.END)]).grid(row = 2, column = 1, sticky = 'e')
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 3, column = 1, sticky = 'e')
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		tkinter.Button(self, text = "Recommencer", width = largeurBout, height = hauteurBout, command = lambda : self.recommencer()).grid(row = 3, column = 0, sticky = 'w')
		
	def recommencer(self):
		self.etape = 0
		self.memoire = [[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]]
		self.consigne.set("Quel est le numéro affiché ? \n ")
		self.compteur = 0
	
	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Appuyer sur la bonne touche pour aller à la prochaine étape. Compléter toutes les étapes pour désarmer le module. \n Appuyer sur un bouton incorrect vous fera revenir à l'étape 1. \n Les boutons sont ordonnés de gauche à droite."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return


	def get_memory(self):
		self.display = int(self.memory_var.get())
		return self.display
		
	def memory(self) :
		self.compteur = 0
		self.display = self.get_memory()
		for i in range(0, len(self.memoire)):
			for j in range(0, len(self.memoire[i])):
				if(self.memoire[i][j] != [0]):
					self.compteur += 1
		if(self.compteur % 2 == 0):
			if(len(self.tableau[self.etape][self.display-1]) == 2): 				#consigne pas besoin etapes precedentes	
				if ('p' in self.tableau[self.etape][self.display-1]): 													#consigne sur position
					self.consigne.set("Appuie sur la "+ self.tableau[self.etape][self.display-1][0]+"e position. \nQuel est le numéro cliqué ?")
					self.memoire[self.etape][0] = int((self.tableau[self.etape][self.display-1])[0]) #On rentre dans la memoire la position cliquee
					return
				if ('c' in self.tableau[self.etape][self.display-1]): 								#Si la consiqne porte sur le numero
					self.consigne.set("Appuie sur le " + self.tableau[self.etape][self.display-1][0]+ ". \nQuelle est sa position ?") 	#On affiche la consigne
					self.memoire[self.etape][1] = int((self.tableau[self.etape][self.display-1])[0]) 		#On rentre en memoire le numero
					return
										
			else : 																#Si on a besoin des etapes precedentes
				self.ancienne_etape = int((self.tableau[self.etape][self.display-1])[1])-1 			#On recupere l'etape dont on a besoin
				if('p' in self.tableau[self.etape][self.display-1]): 								#Si on a besoin de la position d'une etape precedente
					self.consigne.set("Appuie sur la " + str(self.memoire[self.ancienne_etape][0])+"e position. \nQuel est le numéro cliqué ? ")
					self.memoire[self.etape][0] = self.memoire[self.ancienne_etape][0] 		#On rentre en memoire la position
					return				
				if ('c' in self.tableau[self.etape][self.display-1]): 							#Si on a besoin du numero d'une etape precedente
					self.consigne.set("Appuie sur le "+str(self.memoire[self.ancienne_etape][1])+". \nQuelle est sa position ?" 	)			
					self.memoire[self.etape][1] = self.memoire[self.ancienne_etape][1] 									#On prend en memoire le chiffre
					return
	
		else :
			if(self.etape != 4): 
				if self.memoire[self.etape][0] ==[0]:
					self.memoire[self.etape][0] = self.display
					self.etape +=1
					self.consigne.set("Quel est le numéro affiché ? \n ")
					return
				else : 
					self.memoire[self.etape][1] = self.display
					self.etape +=1
					self.consigne.set("Quel est le numéro affiché ?\n ")
					return
		
				#A chaque etape, le bouton a cliquer en fonction de l'affichage: p=position, c=chiffre
				

#######################################################

class JeuxDeMots(tkinter.Frame):
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		fontStyle = tkFont.Font( size=20)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		self.motEntry = tkinter.StringVar()
		self.jeuDeMot = tkinter.Entry(self, textvariable = self.motEntry)

		tkinter.Label(self, text="Jeux de mots", font = fontStyle ).grid(row = 0, column = 0, columnspan = 3)
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 3, column = 1, sticky = 'E')
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0)
		self.consigne.set("Rentre le mot.")
		self.valider = tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.jeuDeMot_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
		self.valider.grid(row = 2, column = 1)

		self.jeuDeMot.grid(row = 2, column = 0, sticky = 'EW')
		self.jeuDeMot.focus()
		self.jeuDeMot.bind('<Return>', lambda event : [self.jeuDeMot_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
		self.result = tkinter.StringVar()
		self.resultText = tkinter.Label(self, textvariable = self.result)
		self.resultText.grid(row = 3, column = 0, sticky = 'e')
		self.result.set("") 
		tkinter.Label(self, text = "Solution:").grid(row = 3, column = 0, sticky = 'w')
		

	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Lire l'écran et rentrer le mot affiché pour déterminer quel libellé de bouton lire.\n Rentrer le libellé de ce bouton pour savoir quel bouton appuyer. \n Appuyer sur le premier mot qui apparaît dans la liste correspondante \n Recommencer jusqu'à ce que le module soit désarmé."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return

			
	def jeuDeMot_fonc(self):
		self.indi = 0
		self.mot = self.motEntry.get().lower()
		if(self.mot == 'thon'):																		#En haut a gauche
			self.result.set("Haut gauche.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			
		elif(self.mot == 'premier' or self.mot == 'ok' or self.mot == 'c'):										#En haut a droite
			self.result.set("Haut droite.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
								
		elif(self.mot == 'oui' or self.mot == 'mot' or self.mot == 'vert' or self.mot== 'rien'):		#Milieu gauche
			self.result.set("Milieu gauche.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			
		elif(self.mot == 'vide' or self.mot == 'bouge' or self.mot == 'rouge' or self.mot == 'tes' or self.mot == 'ton' or self.mot == 'tons' or self.mot == 'vers'):				#milieu droite
			self.result.set("Milieu droite.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			
		elif(self.mot == '' or self.mot == 'au' or self.mot == 'eau' or self.mot == 'haut'):	#Bas a gauche
			self.result.set("Bas gauche.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			
		elif(self.mot == 'verre' or self.mot == 'mots' or self.mot == 'non' or self.mot == 'maux' or self.mot == 't\'es' or self.mot == 'attends' or self.mot == "tu es" or self.mot == "c'est" or self.mot == 'ver' ):
			self.result.set("Bas droite.")
			self.consigne.set("Rentre l'autre mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [ self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.mot_2_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			
		else :
			self.result.set("Erreur")
																	   

	def mot_2_fonc(self):
		self.mot_2 = self.motEntry.get().upper()
		self.tableau = [["PRET", "OUI", "E", "EUX", "MILIEU", "GAUCHE", "APPUIE", "DROITE", "VIDE", "PRET", "NON", "PREMIER", "EUHHH", "RIEN", "ATTENDS"],
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

		liste = []
		for i in range(0,28):
			if(self.tableau[i][0] == self.mot_2):
				self.indi =1
				for j in range(1,14):
					liste.append(self.tableau[i][j])

		if self.indi == 0 :
			self.result.set("Erreur !")
			
		elif self.indi == 1:	
			self.result.set(liste)	
			self.consigne.set("Rentre le mot.")
			self.jeuDeMot.bind('<Return>', lambda event : [self.jeuDeMot_fonc(), self.jeuDeMot.delete(0, tkinter.END)])
			self.valider.configure(command = lambda :[self.jeuDeMot_fonc(), self.jeuDeMot.delete(0, tkinter.END)])	

			
					  
#######################################################

class MotDePasse(tkinter.Frame):
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		fontStyle = tkFont.Font( size=20)
		tkinter.Label(self, text="Mot de Passe", font = fontStyle).grid(row = 0, column = 0)
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0)
		self.lettres_var = tkinter.StringVar()
		self.consigne.set("Rentre les 6 lettres de la 1ere lettre")
		self.lettresEntry = tkinter.Entry(self, textvariable = self.lettres_var)
		self.lettresEntry.grid(row = 2, column = 0)
		self.lettresEntry.focus()
		self.lettresEntry.bind("<Return>", lambda event : [self.getLettre(), self.motDePasse_2(), self.lettresEntry.delete(0, tkinter.END)])
		self.valider = tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.getLettre(), self.motDePasse_2(), self.lettresEntry.delete(0, tkinter.END)])
		self.valider.grid(row = 2, column = 1)
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command = lambda: master.switch_frame(Menu)).grid(row = 4, column = 1)
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.result = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.result).grid(row = 3, column = 0, sticky = 'e', columnspan = 2)
		tkinter.Label(self, text = "Solution:", justify = tkinter.LEFT).grid(row = 3, column = 0, sticky = 'w')
		self.iter = 0
		self.listePrincipale = ["abats", "abime" ,"abois" ,"adieu", "delta"
						,"dense", "devin", "divin" ,"drame", "droit",
						"envol" ,"envie" ,"envoi", "erres" ,"essai",
						"fleur" ,"finit", "fiole", "kilos", "litre",
						"livre", "masse", "match", "matin", "mauve",
						"poser", "ports", "poule", "salir", "taire",
						"tarif", "tasse", "valve", "vanne", "vente"]
		self.listeReponse = []
		self.recommencerBout = tkinter.Button(self, text = "Recommencer", width = largeurBout, height = hauteurBout, command = lambda : self.recommencer())
		self.recommencerBout.grid(row = 4, column = 0)

	def recommencer(self):
		self.consigne.set("Rentre les 6 lettres de la 1ere lettre")
		self.listePrincipale = ["abats", "abime" ,"abois" ,"adieu", "delta","dense", "devin", "divin" ,"drame", "droit", "envol" ,"envie" ,"envoi", "erres" ,"essai", "fleur" ,"finit", "fiole", "kilos", "litre", "livre", "masse", "match", "matin", "mauve", "poser", "ports", "poule", "salir", "taire", "tarif", "tasse", "valve", "vanne", "vente"]
		self.result.set("Solution: ")
		self.iter = 0
		self.listeReponse = []
		return
		
	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Les boutons au-dessus et en dessous d'une position permettent de passer en revue les différentes lettres possibles pour cette position. \n Seule une combinaison des lettres disponibles correspond à un mot possible. \n Appuyer sur le bouton « Valider » quand les lettres forment un mot correct."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return


	def getLettre(self):
		self.lettres = self.lettres_var.get().lower()

	def motDePasse_2(self):
		while (len(self.lettres)!=6):
			self.result.set("Le nombre de lettres n'est pas bon, recommence ! ")
			return
		for self.mot in self.listePrincipale :
			for self.lettre in range(len(self.lettres)):
				if(self.mot[self.iter] == self.lettres[self.lettre]):
					if(self.mot not in self.listeReponse):
						self.listeReponse.append(self.mot)

		if len(self.listeReponse) > 1:
			self.liste=[]
			for j in self.listeReponse :
				self.liste.append(j)
			self.result.set(self.liste)
			self.listePrincipale = self.listeReponse
			self.listeReponse = []
			self.iter +=1
			self.consigne.set("Entre les 6 lettres de la "+ str(self.iter+1) +"eme lettre")

		elif(len(self.listeReponse)) == 0:
			self.result.set("Erreur !")
			self.listeReponse = []
		else:
			self.result.set(self.listeReponse[0])
			self.iter+=1
			self.consigne.set("Entre les 6 lettres de la "+ str(self.iter+1) +"eme lettre")
			return


#######################################################

class Morse(tkinter.Frame):
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		fontStyle = tkFont.Font( size=20)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		self.i = 0
		tkinter.Label(self, text="Morse", font = fontStyle).grid(row = 0, column = 0, columnspan = 2)
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 4, column = 1)
		tkinter.Button(self, text = "Recommencer", width = largeurBout, height = hauteurBout, command = lambda : self.recommencer()).grid(row = 4, column  = 0)
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
		self.consigne.set(str(self.i+1)+"e sequence : Tape c pour court, l pour long et d pour debut du mot.")
		self.morseVar = tkinter.StringVar()
		self.morseEntry = tkinter.Entry(self, textvariable = self.morseVar)
		self.morseEntry.grid(row = 2, column = 0)
		self.morseEntry.focus()
		self.morseEntry.bind("<Return>", lambda event : [self.morse_get(), self.morse(), self.morseEntry.delete(0, tkinter.END)])
		tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command= lambda : [self.morse_get(), self.morse(), self.morseEntry.delete(0, tkinter.END)]).grid(row = 2, column = 1)
		self.result = tkinter.StringVar()
		self.resultText = tkinter.Label(self, textvariable = self.result).grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
		self.result.set("Solution: ")
		self.tableau = [[],[],[],[],[],[]]								#Tableau des sequences dans leur ordre d'apparition + indicateur de debut de mot
		self.tableauOrdonne=[[],[],[],[],[]] 								#Tableau des sequences dans le bon ordre, sans indicateur de debut de mot
		self.mot=[[],[],[],[],[]] 																			#Tableau des lettres dans le bon ordre
		self.mots = ['vitre',505,'ville',515,'chose',522,'signe',532,'ligne',542,'linge',535,'champ',545,'litre',552,'phase',555,'chaud',565,'bille',572,'balle', 575,'singe', 582,'plume',592,'pluie',595,'salle',600] #Tableau des mots associes a leurs frequences
		self.lettres = ['a','cl','b','lccc','c','lclc','d','lcc','e','c','f','cclc','g','llc',
				'h','cccc','i','cc','j','clll','k','lcl','l','clcc','m','ll','n','lc','o','lll','p','cllc','q',
				'llcl','r','clc','s','ccc','t','l','u','ccl','v','cccl'] 								#Tableau de correspondance lettre/sequence

		self.n = 0
		self.indicateur = 0	
		
	def recommencer(self):
		self.i = 0
		self.consigne.set(str(self.i+1)+"e sequence : Tape c pour court, l pour long et d pour debut du mot.")
		self.tableau = [[],[],[],[],[],[]]							
		self.tableauOrdonne=[[],[],[],[],[]] 								
		self.mot=[[],[],[],[],[]]
		self.n = 0
		self.indicateur = 0
		self.result.set("Solution: ")
	
	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Rentrer les différentes séquences de lumières clignotantes. \n Le signal se répètera, avec une longue pause entre les répétitions. \n Les chiffres qui s'affichent lorsque vous avez terminé correspondent à la fréquence à régler. \n Appuyer sur le bouton de transmission (TX) une fois fini."
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return


	def morse_get(self):
		self.tableau[self.i] = self.morseVar.get().lower()
		
	def morse(self): 
		while(len(self.tableau[self.i]) >1 and 'd' in self.tableau[self.i]):
			self.result.set("Solution: On ne peut pas combiner D avec L ou C") 																				
		if self.tableau[self.i] not in self.lettres :
			self.result.set("Solution: Erreur ! Cette lettre n'existe pas, recommence cette saisie.")
			self.tableau[self.i] = []														
			self.i -= 1
			
		if(self.tableau[self.i] == 'd'):																	#On verifie qu'il n'y ait pas plusieurs d
			self.indicateur += 1 
		self.i += 1	
		self.consigne.set(str(self.i+1)+"e sequence : Tape c pour court, l pour long et d pour debut du mot.")	
		if self.i == 6 :	
			self.consigne.set("Toutes les sequences ont ete rentrees")												
		if(self.indicateur == 2 ):														#Si l'utilisateur rentre plusieurs fois l'indicateur de debut,
			self.result.set('Solution: Erreur ! Tu as indique deux fois le debut. Recommence au depart\x1b') 			
			self.tableau = [[],[],[],[],[],[]] 															#On vide le tableau
			self.i = 0
			self.indicateur = 0
																					#Si la sequence est correcte, on passe a la lettre suivante
		if(self.i == 6 and self.indicateur < 1):
			self.result.set("Solution: Erreur ! Il n'y a pas de début. Recommence depuis le debut") 			
			self.tableau = [[],[],[],[],[],[]] 															#On vide le tableau
			self.i = 0
			self.indicateur = 0
					
		if (self.i==6 and self.indicateur == 1):										#Lorsqu'on a rentré toutes les sequences, on passe a la conversion
			for self.l in range(6): 																		#Ordonne et classe
				if(self.tableau[self.l] == 'd'): 																
					for self.j in range(5): 																
						self.tableauOrdonne[self.j] = self.tableau[(self.l+1+self.j)%6] 										
			for self.k in range(5): 																		#Convertit les séquences en lettres
				for self.m in range(len(self.lettres)): 														
						if( self.m%2==1 ): 																
							if(self.tableauOrdonne[self.k] == self.lettres[self.m]):									
								self.mot[self.k] = self.lettres[self.m-1]
			
			self.compteur = 0
			while( self.n == 0 ): 																	#Tant qu'on a pas trouve d'erreur
				for self.b in range(0,len(self.mots),2): 														#Parcours le tableau des mots
					self.z = 0															#compteur compte le nombre d'occurence de bonnes lettres
					for self.j in self.mots[self.b]:															#Pour les lettre des mots
						if(self.j == self.mot[self.z]):																
							self.compteur += 1
							self.z += 1
						else:
							self.compteur = 0
							self.z=0
							break
					if(self.compteur == 5):
						self.result.set(str(self.mots[self.b+1])) 				
						return 																
				self.result.set("Solution: Ce mot n'existe pas ! Clique sur 'Recommence'") 	
				self.n = 1	
				
			
			
			
			


#######################################################

class Boutons(tkinter.Frame):
	def __init__(self, master):
		tkinter.Frame.__init__(self, master)
		tkinter.Button(self, image = aide, command = lambda : self.menuAide()).grid(row = 0, column = 1, sticky = 'e')
		fontStyle = tkFont.Font( size=20)
		tkinter.Label(self, text="Boutons", font = fontStyle ).grid(row = 0, column = 0, columnspan = 3)
		tkinter.Button(self, text="Retour", width = largeurBout, height = hauteurBout, command=lambda: master.switch_frame(Menu)).grid(row = 3, column = 1, sticky = 'E')
		master.bind('<Escape>', lambda event : master.switch_frame(Menu))
		self.consigne = tkinter.StringVar()
		tkinter.Label(self, textvariable = self.consigne, justify = tkinter.LEFT).grid(row = 1, column = 0)
		self.consigne.set("Tape b pour bleu, w pour blanc, r pour rouge et j pour jaune \n ET A pour annuler, E pour Exploser, M pour Maintenir.")
		tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.boutons()]).grid(row = 2, column = 1, sticky = 'W')

		self.boutons_v = tkinter.StringVar()
		self.boutonsEntry = tkinter.Entry(self, textvariable = self.boutons_v)
		self.boutonsEntry.grid(row = 2, column = 0, sticky = 'EW')
		self.boutonsEntry.bind('<Return>', lambda event : self.boutons())
		self.boutonsEntry.focus()
		
		self.result = tkinter.StringVar()
		self.textResult = tkinter.Label(self, textvariable = self.result)
		self.textResult.grid(row = 3, column = 0, sticky = 'w')
		self.result.set("Solution: ")
		
	def get_entry_boutons(self):
		self.bouton = self.boutons_v.get().lower()
		return self.bouton
		
	def menuAide(self):
		self.menuAide = tkinter.Tk()
		self.menuAide.title("Aide")
		self.Texte = "Rentrer la couleur du bouton et le texte inscrit dessus. \n Si le bouton est maintenu cliqué, une bande colorée s'affiche à droite. \n Relâcher alors le bouton à un moment spécifique en fonction de la couleur de cette bande"
		tkinter.Label(self.menuAide, text = self.Texte).grid()
		return


	def get_entry_rube(self):
		self.reponse = self.rube.get().lower()	
		self.rube_2()
		return self.reponse	
			
	def boutons(self):
		self.bouton = self.get_entry_boutons()
		if len(self.bouton) != 2 :
			self.result.set('Solution: Erreur')
		elif 'b' in self.bouton and 'a' in self.bouton :
			self.rube()
			return
		elif 'e' in self.bouton and piles>1:
			self.result.set('Solution: Appuie et relache')
		elif 'w' in self.bouton and CAR == 'oui':
			self.rube()
		elif(FRK == 'o' and piles > 2):
			self.result.set('Solution: Appuie et lache')
		elif('r' in self.bouton and 'm' in self.bouton):
			self.result.set('Solution: Appuie et lache')
		else:
			self.rube()
		return

			
			
	def rube(self):
		self.result.set("Solution: Maintiens le bouton et donne la couleur : \n b pour bleu, w pour blanc, r pour rouge et j pour jaune" )
		self.rube = tkinter.StringVar()
		self.rubeEntry = tkinter.Entry(self, textvariable = self.rube)
		self.rubeEntry.grid(row = 4, column = 0, sticky = 'EW')
		self.rubeEntry.focus()
		self.rubeEntry.bind('<Return>', lambda event : self.get_entry_rube())
		tkinter.Button(self, text = "Valider", width = largeurBout, height = hauteurBout, command = lambda : [self.get_entry_rube()]).grid(row = 4, column = 1, sticky = 'W')
		
		
		
	def rube_2(self):
		self.result_2 = tkinter.StringVar()
		self.result_2_text = tkinter.Label(self, textvariable = self.result_2)
		self.result_2.set("Solution: ")
		self.result_2_text.grid(row = 5, column = 0, sticky = 'w')
		if len(self.reponse)!= 1:
			self.result_2.set('Solution: Erreur')
		elif(self.reponse == 'b'):
			self.result_2.set('Solution: Relache à 4')
		elif(self.reponse == 'j'):
			self.result_2.set('Solution: Relache à 5')
		else:
			self.result_2.set('Solution: Relache à 1')
#######################################################

if __name__ == "__main__":

	app = Ktane()	
	aideImage = tkinter.PhotoImage(file = 'aide.png')
	aide = aideImage.subsample(20,20)
	app.mainloop()
	




