def calculate_macros_for_target(fat_100g, carbs_100g, protein_100g, target_weight):
    """
    Calculates the macros for a custom weight based on the 100-gram values.

    Parameters:
    - fat_100g (float): Grams of fat per 100 grams.
    - carbs_100g (float): Grams of carbs per 100 grams.
    - protein_100g (float): Grams of protein per 100 grams.
    - target_weight (float): Custom weight in grams for which to calculate macros.

    Returns:
    - dict: Macros for the target weight.
    """
    # Rule of three to scale macros to target weight
    fat_target = (fat_100g / 100) * target_weight
    carbs_target = (carbs_100g / 100) * target_weight
    protein_target = (protein_100g / 100) * target_weight
    
    # Calories = (fat * 9) + (protein * 4) + (carbs * 4)
    calories_target = (fat_target * 9) + (protein_target * 4) + (carbs_target * 4)

    return {
        "fat_target": round(fat_target, 2),
        "carbs_target": round(carbs_target, 2),
        "protein_target": round(protein_target, 2),
        "calories_target": round(calories_target, 2),
    }

# Example usage
fat_100g = float(input("Enter the grams of fat per 100 grams: "))
carbs_100g = float(input("Enter the grams of carbs per 100 grams: "))
protein_100g = float(input("Enter the grams of protein per 100 grams: "))
target_weight = float(input("Enter your target weight in grams: "))

result = calculate_macros_for_target(fat_100g, carbs_100g, protein_100g, target_weight)

print(f"Macros and calories for {target_weight} grams:")
print(result)

# Wait for user input before closing
input("Press Enter to close the program...")


