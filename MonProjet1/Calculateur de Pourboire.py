        # --- Phase 1 : Collecte des informations ---
bill_total_str = input("Montant total de la facture (MAD) : ")
bill_total = float(bill_total_str)

tip_percentage_str = input("Pourcentage de pourboire (ex: 15%, 18%, 20%) : ")
tip_percentage = int(tip_percentage_str)

num_people_str = input("Nombre de personnes qui partagent : ")
num_people = int(num_people_str)

        # ---Phase 2 : Calculs ---
tip_amount = bill_total * (tip_percentage / 100)
total_with_tip = bill_total + tip_amount
amount_per_person = total_with_tip / num_people
final_amount_per_person = round(amount_per_person, 2)  # arrondi à 2 décimales

        # --- Phase 3 : Affichage ---
print("\n--- RÉSUMÉ DU PAIEMENT ---")
print(f"Total avec pourboire : {total_with_tip:.2f} MAD")
print(f"Chaque personne doit payer : {final_amount_per_person:.2f} MAD")
print(
    f"Basé sur une facture de {bill_total:.2f} MAD "
    f"avec un pourboire de {tip_percentage}% partagé entre {num_people} personne(s)."
)
