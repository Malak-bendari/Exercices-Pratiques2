        #--- Phase 1 : Collecte des informations ---
original_amount_str = input("Quantité originale de l'ingrédient (ex: 250) : ")
original_amount = float(original_amount_str)

original_servings_str = input("Nombre de personnes pour la recette originale : ")
original_servings = int(original_servings_str)

desired_servings_str = input("Nombre de personnes pour lesquelles vous voulez cuisiner : ")
desired_servings = int(desired_servings_str)

        # --- Phase 2 : Calculs ---
scaling_factor = desired_servings / original_servings
new_amount = original_amount * scaling_factor
new_amount = round(new_amount, 1)

        # --- Phase 3 : Affichage ---
print("\n--- AJUSTEMENT DE LA RECETTE ---")
print(f"La recette originale est pour {original_servings} personnes.")
print(f"Pour cuisiner pour {desired_servings} personnes, vous aurez besoin de {new_amount} unités de votre ingrédient.")
