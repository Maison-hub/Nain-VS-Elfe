import random
import os
def clear_screen(): 
    """permet de nettoyer la console peut importe l'OS"""
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 
class nain:
    """classe du nain"""
    def __init__(self, nom):
        self.nom = nom
        self.att = 5
        self.deff = 3
        self.hp = 4
    def cri(self):
        """renvoie Le cri du guerrier"""
        return "POUR XAR'SAROTH!!!!"
class elf:
    """classe de l'elfe"""
    def __init__(self, nom):
        self.nom = nom
        self.att = 4
        self.deff = 3
        self.hp = 5
    def cri(self):
        """renvoie Le cri du guerrier"""
        return "DANS GOMBO Y'A GOMBO Y'A AUBERGINE Y'A TOMATE Y'A AIL ET Y'A OIGNON"
def attaque(perso):
    """Prend en paramètre un objet de la classe Nain ou Elfe et renvoie un nombre aleatoire pour savoir avec combien de points le personnage attaque"""
    pts = random.randint(1, perso.att)
    return pts
def defense(perso):
    """Prend en paramètre un objet de la classe Nain ou Elfe et renvoie un nombre aleatoire pour savoir avec combien de points le personnage se défend"""
    pts = random.randint(1, perso.deff)
    return pts
def combat(loose, win)-> list: 
    "Prend en paramètre deux personnages et fait la différence des fonctions attaque() et defense()"
    att = attaque(win)
    armure = defense(loose)
    hp = armure - att
    return [hp, att, armure, win, loose]
def result(tab:list):
    """interprete la fonction combat() et renvoie mis en forme en console le resultat du combat """
    clear_screen()
    cbt = f"----------\n COMBAT \n----------\n{tab[3].cri()}\nResultat de l'attaque de {tab[3].nom}: {tab[1]} \nResultat de la defense de {tab[4].nom}: {tab[2]}"
    if tab[0] >= 0:
        return f"{cbt} \npas de dégats"
    elif tab[0] < 0:
        tab[4].deff -= 1
        return f"{cbt} \n{tab[4].nom} à perdu 1 point de vie"
def game():
    """succéssion de combat tant qu'il reste de la vie aux personnages"""
    clear_screen()
    print("---------------------------------\n BIENVENUE DANS ELFE VERSUS NAIN \n---------------------------------")
    perso_nain = nain(str(input("Nom du Nain :")))
    perso_elfe = elf(str(input("Nom de l'Elfe :")))
    clear_screen()
    print(f"Le nom du nain est: {perso_nain.nom}\nLe nom de l'elf est: {perso_elfe.nom}")
    while perso_nain.deff > 0 and perso_elfe.deff > 0:
        choix = input("choisissez qui attaque (n)ain ou (e)lf : ")
        if choix == "n":
            print(result(combat(perso_elfe, perso_nain)))
        elif choix == "e":
            print(result(combat(perso_nain, perso_elfe)))
    if perso_nain.deff <= 0:
        clear_screen()
        print(f"Fin du combat c'est {perso_elfe.nom} qui a gagné")
    elif perso_elfe.deff <= 0:
        clear_screen()
        print(f"Fin du combat c'est {perso_nain.nom} qui a gagné")
    encore = input("Voulez vous faire une autre partie o = oui / n = non: ")
    if encore == "o":
        game()
    else:
        os.system('exit()')
game()
