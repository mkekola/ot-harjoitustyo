import random

genders = ["Male", "Female"]
life_stages = ["Infant", "Toddler", "Child",
               "Teen", "Young Adult", "Adult", "Elder"]
voices = ["Sweet", "Melodic", "Lilted", "Clear", "Warm", "Brash"]
aspirations = ["Animal", "Athletic", "Creativity", "Deviance", "Family", "Food",
               "Fortune", "Knowledge", "Location", "Love", "Nature", "Popularity"]
skin_tones = ["Warm Light", "Warm Medium", "Warm Dark", "Neutral Light",
              "Neutral Medium", "Neutral Dark", "Cool Light", "Cool Medium", "Cool Dark"]
hair_styles = ["Short", "Medium", "Long", "Updo"]
hair_colors = ["Black", "Dark Brown", "Light Brown", "Red", "Dark Blonde",
               "Light Blonde", "Dark Grey", "Light Gray", "Blue", "Pink", "Green"]
eye_colors = ["Blue", "Light Blue", "Brown", "Dark Brown",
              "Light Brown", "Green", "Light Green", "Amber", "Black", "Grey"]

def create_random_character():
    character = {
        "Gender": random.choice(genders),
        "Life_Stage": random.choice(life_stages),
        "Voice": random.choice(voices),
        "Aspiration": random.choice(aspirations),
        "Skin_Tone": random.choice(skin_tones),
        "Hair_Style": random.choice(hair_styles),
        "Hair_Color": random.choice(hair_colors),
        "Eye_Color": random.choice(eye_colors)
    }
    return character

