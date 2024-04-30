import random


class Character():
    ''' Luokka, joka kuvaa pelin hahmoa. 
        Hahmolla on sukupuoli, elämänvaihe, ääni, tavoite, ihonväri, hiustyyli, hiusten väri ja silmien väri.    
        '''

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

    def __init__(self, id=None, gender=None, life_stage=None, voice=None, aspiration=None,
                 skin_tone=None, hair_style=None, hair_color=None, eye_color=None):
        ''' Luokan konstruktori, joka luo uuden hahmon.
            Args:
                id: Hahmon tunniste.
                gender: Hahmon sukupuoli.
                life_stage: Hahmon elämänvaihe.
                voice: Hahmon ääni.
                aspiration: Hahmon tavoite.
                skin_tone: Hahmon ihonväri.
                hair_style: Hahmon hiustyyli.
                hair_color: Hahmon hiusten väri.
                eye_color: Hahmon silmien väri.
                '''

        self.gender = gender if gender else random.choice(self.genders)
        self.life_stage = life_stage if life_stage else random.choice(
            self.life_stages)
        self.voice = voice if voice else random.choice(self.voices)
        self.aspiration = aspiration if aspiration else random.choice(
            self.aspirations)
        self.skin_tone = skin_tone if skin_tone else random.choice(
            self.skin_tones)
        self.hair_style = hair_style if hair_style else random.choice(
            self.hair_styles)
        self.hair_color = hair_color if hair_color else random.choice(
            self.hair_colors)
        self.eye_color = eye_color if eye_color else random.choice(
            self.eye_colors)

    def __str__(self):
        ''' Luokan merkkijonoesitys.
            Returns:
                Merkkijonoesitys, joka kuvaa hahmoa.
                '''
        return f"\t{self.gender} {self.life_stage} with a {self.voice} voice. \n\
        They aspire {self.aspiration}. They have {self.skin_tone} skin, \n\
        {self.hair_color} {self.hair_style} hair, and {self.eye_color} eyes. \n"
