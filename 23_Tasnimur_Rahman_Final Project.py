import random

# Sample database of names
names_db = {
    "male": {
        "English": ["James", "John", "Robert", "Michael", "William"],
        "French": ["Louis", "Pierre", "Jean", "Henri", "Philippe"],
        "Fantasy": ["Aragon", "Thalion", "Draven", "Zephyr", "Kael"]
    },
    "female": {
        "English": ["Mary", "Patricia", "Linda", "Barbara", "Elizabeth"],
        "French": ["Marie", "Sophie", "Claire", "Isabelle", "Chantal"],
        "Fantasy": ["Elaria", "Sylvana", "Amara", "Lyria", "Fayeth"]
    },
    "neutral": {
        "English": ["Taylor", "Jordan", "Casey", "Alex", "Riley"],
        "French": ["Camille", "Noel", "Dominique", "René", "Sasha"],
        "Fantasy": ["Auron", "Zeren", "Korin", "Cayde", "Riven"]
    }
}


def generate_name(gender="neutral", origin="English", theme=None):
    """
    Generate a random name based on the provided gender, origin, and theme.
    - gender: 'male', 'female', or 'neutral'
    - origin: 'English', 'French', or 'Fantasy'
    - theme: Additional customization (future scope)
    """
    try:
        # Fetch names based on gender and origin
        name_list = names_db[gender][origin]
        return random.choice(name_list)
    except KeyError:
        return "Invalid choice. Please try again with valid options."


# User interaction
def main():
    print("Welcome to the Name Generator!")
    gender = input("Choose gender (male/female/neutral): ").strip().lower()
    origin = input("Choose origin (English/French/Fantasy): ").strip().capitalize()

    name = generate_name(gender=gender, origin=origin)
    print(f"Generated Name: {name}")


if __name__ == "__main__":
    main()
