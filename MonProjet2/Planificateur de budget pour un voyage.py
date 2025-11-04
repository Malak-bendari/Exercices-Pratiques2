        #--- Phase 1 : Collecte des informations ---
distance_km_str = input("Distance Total du voyage (en km) : ")
distance_km = float(distance_km_str)

efficiency_str = input("la consommation de carburant (litres / 100 km) : ")
efficiency = float(efficiency_str)

price_per_liter_str = input("Prix actuel du carburant (MAD/litre) : ")
price_per_liter = float(price_per_liter_str)

        # --- Phase 2 : Calculs ---
fuel_needed = (distance_km / 100) * efficiency
total_cost = fuel_needed * price_per_liter
total_cost = round(total_cost, 2)

        # --- Phase 3 : Affichage ---
print("\n--- ESTIMATION DU BUDGET CARBURANT ---")
print(f"Distance totale du voyage : {distance_km:.1f} km")
print(f"Carburant nécessaire : {fuel_needed:.2f} litres")
print(f"Le coût estimé du carburant pour ce voyage sera de {total_cost:.2f} MAD")
