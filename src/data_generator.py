import random
from typing import List, Dict, Tuple
import json

class StoryGenerator:
    def __init__(self, seed: int = 42):
        random.seed(seed)
        self.names = [
            "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy",
            "Kevin", "Laura", "Mallory", "Niaj", "Olivia", "Peggy", "Quentin", "Rupert", "Sybil", "Trent",
            "Ursula", "Victor", "Walter", "Xavier", "Yvonne", "Zelda", "Arthur", "Beatrix", "Caleb", "Daphne",
            "Elias", "Fiona", "Gabriel", "Hannah", "Isaac", "Julia", "Kai", "Luna", "Milo", "Nora",
            "Oliver", "Penelope", "Quinn", "Rowan", "Silas", "Thea", "Ulysses", "Violet", "Wyatt", "Xena",
            "Yasmine", "Zachary", "Liam", "Emma", "Noah", "Ava", "James", "Isabella", "William", "Sophia",
            "Benjamin", "Mia", "Lucas", "Charlotte", "Henry", "Amelia", "Alexander", "Harper", "Michael", "Evelyn",
            "Daniel", "Abigail", "Jacob", "Emily", "Logan", "Elizabeth", "Jackson", "Mila", "Ella",
            "Sebastian", "Avery", "Mateo", "Sofia", "Jack", "Camila", "Owen", "Aria", "Theodore", "Scarlett"
        ]
        self.professions = [
            "Doctor", "Teacher", "Engineer", "Artist", "Chef", "Pilot", "Nurse", "Lawyer", "Scientist", "Writer",
            "Musician", "Farmer", "Police Officer", "Firefighter", "Architect", "Carpenter", "Baker", "Actor", "Dancer", "Librarian",
            "Mechanic", "Journalist", "Photographer", "Veterinarian", "Dentist", "Pharmacist", "Electrician", "Plumber", "Florist", "Gardener"
        ]
        self.locations = [
            "Kitchen", "Living Room", "Garden", "Library", "Balcony", "Dining Hall", "Basement", "Attic", "Study", "Garage",
            "Patio", "Bedroom", "Guest Room", "Ballroom", "Conservatory", "Wine Cellar", "Pantry", "Veranda", "Foyer", "Music Room"
        ]
        self.drinks = [
            "Tea", "Coffee", "Water", "Juice", "Wine", "Beer", "Soda", "Cocktail", "Smoothie", "Milk",
            "Lemonade", "Champagne", "Whiskey", "Martini", "Cider", "Cocoa", "Iced Tea", "Espresso", "Latte", "Mocha"
        ]

    def generate_story(self, num_characters: int) -> Dict:
        """
        Generates a story with N characters, each having a profession, location, and drink.
        """
        if num_characters > len(self.names):
            raise ValueError(f"Max characters supported is {len(self.names)}, requested {num_characters}")

        # Select characters
        selected_names = random.sample(self.names, num_characters)
        
        # Assign attributes
        character_data = {}
        for name in selected_names:
            character_data[name] = {
                "Profession": random.choice(self.professions),
                "Location": random.choice(self.locations),
                "Drink": random.choice(self.drinks)
            }

        # Generate narrative sentences
        intro = "It was a lively evening at the Grand Manor. Many guests had arrived for the gala.\n"
        sentences = []
        
        # Introduction sentences
        for name, data in character_data.items():
            # Mix up the order of attribute revelation
            facts = [
                f"{name} works as a {data['Profession']}.",
                f"{name} was seen in the {data['Location']}.",
                f"{name} was holding a glass of {data['Drink']}."
            ]
            sentences.extend(facts)

        # Shuffle sentences to prevent simple block-based attention
        random.shuffle(sentences)
        
        # Add some noise/interaction (optional, keeping it simple for now to purely test tracking)
        # Maybe add timestamps or "Later..."
        
        story_text = intro + " ".join(sentences)

        # Generate specific questions
        questions = []
        for name, data in character_data.items():
            questions.append({
                "question": f"What is {name}'s profession?",
                "answer": data['Profession'],
                "type": "Profession"
            })
            questions.append({
                "question": f"Where is {name}?",
                "answer": data['Location'],
                "type": "Location"
            })
            questions.append({
                "question": f"What is {name} drinking?",
                "answer": data['Drink'],
                "type": "Drink"
            })

        return {
            "num_characters": num_characters,
            "story": story_text,
            "characters": character_data,
            "questions": questions
        }

if __name__ == "__main__":
    # Test
    gen = StoryGenerator()
    data = gen.generate_story(5)
    print(data['story'][:500])
    print(data['questions'][0])
