import os
import logging
from dotenv import load_dotenv

# Protein Database
PROTEIN_DATABASE = {
    'pizza': {
        'type': 'Mixed (Animal and Plant)',
        'protein_per_100g': 11.0,
        'protein_sources': ['Cheese', 'Meat Toppings', 'Wheat Flour']
    },
    'chicken': {
        'type': 'Animal-based',
        'protein_per_100g': 31.0,
        'protein_sources': ['Chicken Muscle Tissue']
    },
    'tofu': {
        'type': 'Plant-based',
        'protein_per_100g': 17.3,
        'protein_sources': ['Soybean']
    },
    'salmon': {
        'type': 'Animal-based',
        'protein_per_100g': 20.4,
        'protein_sources': ['Fish Muscle']
    },
    'eggs': {
        'type': 'Animal-based',
        'protein_per_100g': 13.0,
        'protein_sources': ['Egg White', 'Egg Yolk']
    }
}

class ProteinInfoManager:
    @staticmethod
    def get_protein_info(food_name):
        """Retrieve protein information for a specific food"""
        food_name = food_name.lower()
        return PROTEIN_DATABASE.get(food_name, {
            'type': 'Unknown',
            'protein_per_100g': 'Not Available',
            'protein_sources': []
        })

    @staticmethod
    def format_protein_details(food_name):
        """Format protein details in a readable manner"""
        info = ProteinInfoManager.get_protein_info(food_name)
        return f"""
        **Protein Information for {food_name.capitalize()}**
        - Protein Type: {info['type']}
        - Protein per 100g: {info['protein_per_100g']}g
        - Protein Sources: {', '.join(info['protein_sources'])}
        """

def main():
    # Interactive protein information retrieval
    while True:
        food_name = input("Enter a food name (or 'quit' to exit): ").strip()
        
        if food_name.lower() == 'quit':
            break
        
        try:
            protein_details = ProteinInfoManager.format_protein_details(food_name)
            print(protein_details)
        except Exception as e:
            print(f"Error retrieving protein information: {e}")

if __name__ == "__main__":
    main()