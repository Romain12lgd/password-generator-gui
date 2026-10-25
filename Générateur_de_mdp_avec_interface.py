from random import *
from string import *
import tkinter as tk

#Fonction qui génère le mot de passe
def generer_un_mdp(longueur, options):
    construction = ""
    mdp_list = []
    if options["minuscules"]:
        construction += ascii_lowercase
        mdp_list.append(choice(ascii_lowercase))
    if options["majuscules"]:
            construction += ascii_uppercase
            mdp_list.append(choice(ascii_uppercase))
    if options["chiffres"]:
            construction += digits
            mdp_list.append(choice(digits))
    if options["ponctuations"]:
            construction += punctuation
            mdp_list.append(choice(punctuation))

    if not construction:
        return "Impossible de générer un mot de passe sans aucun caractère !"

    reste = longueur - len(mdp_list)
    #Ajout des caractère manquant, mélange et regroupement
    mdp_list.extend(choices(construction, k=reste)) 
    shuffle(mdp_list)
    mdp = "".join(mdp_list)
    return mdp

#Fonction pour le clique du bouton
def action_generer():
    # Récupérer les choix
    options = {
        "minuscules": var_minuscules.get(),
        "majuscules": var_majuscules.get(),
        "chiffres": var_chiffres.get(),
        "ponctuations": var_ponctuations.get()
    }
    
    # Récupérer la taille
    try:
        taille = int(champ_taille.get())
        if taille < 8:
            label_resultat.config(text="Minimum 8 caractères !")
            return
    except ValueError:
        label_resultat.config(text="Entre un nombre valide !")
        return
        
    # Générer le mot de passe
    global dernier_mdp
    dernier_mdp = generer_un_mdp(taille, options)
    
    # Afficher le résultat
    label_resultat.config(text=f"Mot de passe : {dernier_mdp}")

#Copier le mot de passe
def copier():
    try:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(dernier_mdp)
        label_resultat.config(text="Mot de passe copié !")
    except:
        label_resultat.config(text="Générer un mot de passe d'abord")

couleur_cadre = "#858585"

fenetre = tk.Tk()
fenetre.title("Générer un mot de passe sécurisé.")
fenetre.geometry("280x240")

mon_texte = tk.Label(fenetre, text="Générateur de mot de passe")
mon_texte.pack()

mon_bouton = tk.Button(fenetre, text="Générer", command=action_generer, cursor="hand2")
mon_bouton.pack()

var_minuscules = tk.BooleanVar(value=True)
var_majuscules = tk.BooleanVar(value=True)
var_chiffres = tk.BooleanVar(value=True)
var_ponctuations = tk.BooleanVar(value=True)

cadre_options = tk.Frame(fenetre, bg=couleur_cadre, bd=2, relief="groove")
cadre_options.pack(padx=10, pady=10, fill="x")

case_minuscules = tk.Checkbutton(cadre_options, text="Minuscules", variable=var_minuscules, cursor="hand2")
case_minuscules.config(bg=couleur_cadre)

case_majuscules = tk.Checkbutton(cadre_options, text="Majuscules", variable=var_majuscules, cursor="hand2")
case_majuscules.config(bg=couleur_cadre)

case_chiffres = tk.Checkbutton(cadre_options, text="Chiffres", variable=var_chiffres, cursor="hand2")
case_chiffres.config(bg=couleur_cadre)

case_ponctuation = tk.Checkbutton(cadre_options, text="Ponctuations", variable=var_ponctuations, cursor="hand2")
case_ponctuation.config(bg=couleur_cadre)

cadre_options.columnconfigure(0, weight=1)
cadre_options.columnconfigure(1, weight=1)

case_minuscules.grid(row=0, column=0, sticky="w", padx=20, pady=5)
case_majuscules.grid(row=0, column=1, sticky="w", padx=20, pady=5)
case_chiffres.grid(row=1, column=0, sticky="w", padx=20, pady=5)
case_ponctuation.grid(row=1, column=1, sticky="w", padx=20, pady=5)

label_taille = tk.Label(fenetre, text="Longueur du mot de passe (min 8) :")
label_taille.pack()

champ_taille = tk.Entry(fenetre, width=10, relief="flat") 
champ_taille.insert(0, "12")
champ_taille.pack()

label_resultat = tk.Label(fenetre)
label_resultat.config(text="Mot de passe : (Générer un mot de passe)")
label_resultat.pack()

mon_bouton_copier = tk.Button(fenetre, text="Copier", command=copier, cursor="hand2")
mon_bouton_copier.pack()

fenetre.mainloop()