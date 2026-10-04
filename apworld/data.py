from rule_builder.rules import Has

boo_data = {
    ### GENERAL ###
    "characters": [
        "Serra",
        "Nigel",
        "Ollin",
        "Natoko",
        "Roger",
        "R0b3rt",
        "Madlyn",
        "Jody",
        "Ernesto",
        "Sisyphus",
        "Richard",
        "Mitchell"
    ],
    "sheriffs": [
        "Simple Tom",
        "Rex, Cupcake and Brutus",
        "Ruthless Ruth",
        "Crazy Denzel",
        "Undertaker"
    ],
    ### LOCATIONS
    "locations_per_character": [
        "Deputy Kill",
        "Upgrade Choice",
        "Object Choice",
        "Sheriff Kill",
        "Level reached"
    ],
    "locations_global": [
        "Shop Purchase",
        "Achievement"
    ],
    ### ITEMS ###
    "unlocks": [
        "characters",
        "sheriffs",
    ],
    "progressive": {
        "Upgrade Rarity": 5,
        "Object Rarity": 4,
        "Double Coin Drop Chance": 10,
    },
    "permanent": [
        "Damage Up",
        "Attack Speed Up",
        "+1 Dash",
        "Health Up",
        "Speed Up",
        "Cooldown Reduction",
        "Area Effect",
        "Collectible Range",
        "Crit Chance Up",
        "Crit Damage Up",
        "+1 Bounce",
        "+1 Pierce",
        "Upgrade Die",
        "Chest Die",
        "Banish Upgrade Die",
        "Banish Object Die",
        "Starting Chest",
        "Additional Upgrade Choice"
    ],
    "filler": [
        "Damage Up",
        "Attack Speed Up",
        "+1 Dash",
        "Health Up",
        "Speed Up",
        "Cooldown Reduction",
        "Area Effect Up",
        "Collectible Range Up",
        "Crit Chance Up",
        "Crit Damage Up",
        "Bounce",
        "Pierce",
        "20 Gold Nuggets",
        "Level Up",
        "Health Refill",
        "Collect all Coins",
        "Kill all Enemies"
    ],
    "traps": [
        "Damage Trap",
        "Freezing Trap",
        "Pacifist Trap",
        "Dash Trap"
    ],
}

class Rules:
    def __init__(self):
        self.tom = Has("Sheriff Simple Tom Unlock")
        self.rex = Has("Sheriff Rex, Cupcake and Brutus Unlock")
        self.ruth = Has("Sheriff Ruthless Ruth Unlock") & (self.tom | self.rex)
        self.denzel = Has("Sheriff Crazy Denzel Unlock") & (self.tom | self.rex)
        self.undertaker = Has("Sheriff Undertaker Unlock") & (self.ruth | self.denzel)

    def sheriff_rules(self):
        return {
            "Simple Tom": self.tom,
            "Rex, Cupcake and Brutus": self.rex,
            "Ruthless Ruth": self.ruth,
            "Crazy Denzel": self.denzel,
            "Undertaker": self.undertaker,
        }