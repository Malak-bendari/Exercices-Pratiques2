        #--- Phase 1 : Collecte des informations ---
password = input("Entrez un mot de passe à vérifier : ")
password_length = len(password)
has_digit = any(c.isdigit() for c in password)

        # --- Phase 2 : Calculs ---
is_long_enough = password_length >= 8
is_strong = is_long_enough and has_digit

        # --- Phase 3 : Affichage ---
print("\n--- ANALYSE DU MOT DE PASSE ---")


print(f"Longueur d'au moins 8 caractères : {'Valide' if is_long_enough else 'Non Valide'}")
print(f"Contient au moins un chiffre : {'Valide' if has_digit else 'Non Valide'}")


if is_strong:
    print("Votre mot de passe est considéré comme fort ! ")
else:
    print("Votre mot de passe est considéré comme faible !")