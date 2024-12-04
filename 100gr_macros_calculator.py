def convert_to_100g(fat, carbs, protein, portion_size):
    """
    Converts macros (fat, carbs, protein) and calories from a given portion size
    to their 100-gram equivalent using the rule of three.

    Parameters:
    - fat (float): Amount of fat in grams for the given portion size.
    - carbs (float): Amount of carbs in grams for the given portion size.
    - protein (float): Amount of protein in grams for the given portion size.
    - portion_size (float): Portion size in grams.

    Returns:
    - dict: Macros and calories for a 100-gram portion.
    """
    fat_100g = (fat / portion_size) * 100
    carbs_100g = (carbs / portion_size) * 100
    protein_100g = (protein / portion_size) * 100
    calories = (fat * 9) + (protein * 4) + (carbs * 4)
    calories_100g = (calories / portion_size) * 100

    return {
        "fat_100g": round(fat_100g, 2),
        "carbs_100g": round(carbs_100g, 2),
        "protein_100g": round(protein_100g, 2),
        "calories_100g": round(calories_100g, 2),
    }

# Example usage
fat = float(input("Enter the grams of fat: "))
carbs = float(input("Enter the grams of carbs: "))
protein = float(input("Enter the grams of protein: "))
portion_size = float(input("Enter the portion size in grams: "))

result = convert_to_100g(fat, carbs, protein, portion_size)
print("Macros and calories for a 100-gram portion:")
print(result)

# Wait for user input before closing
input("Press Enter to close the program...")
