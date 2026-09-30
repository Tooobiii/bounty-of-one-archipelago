from BaseClasses import Item, ItemClassification

class BountyOfOneItem(Item):
    game = "Bounty of One"

class ItemBuilder:
    def __init__(self, data):
        self.next_id = 708145
        self.data = data
        self.item_name_to_id = {}
        self.default_item_classifications = {}

    # Create all possible items
    def create_item_list(self):
        self.add_sheriff_unlocks()
        self.add_character_unlocks()
        self.add_progressive_unlocks()
        self.add_permanent_stats()
        self.add_fillers()
        self.add_traps()
        return self.item_name_to_id, self.default_item_classifications

    # Helper function to add an item to the item list
    def add_item(self, name, classification):
        self.item_name_to_id[name] = self.next_id
        self.default_item_classifications[name] = classification
        self.next_id += 1

    def add_sheriff_unlocks(self):
        for sheriff, _ in self.data["sheriffs"].items():
            item_name = f"Sheriff {sheriff} Unlock"
            self.add_item(name=item_name, classification=ItemClassification.progression)

    def add_character_unlocks(self):
        for character in self.data["characters"]:
            item_name = f"Character {character} Unlock"
            self.add_item(name=item_name, classification=ItemClassification.progression)

    def add_progressive_unlocks(self):
        for progressive_type, count in self.data["progressive"].items():
            item_name = f"Progressive {progressive_type}"
            self.add_item(name=item_name, classification=ItemClassification.useful)

    def add_permanent_stats(self):
        for stat in self.data["permanent"]:
            item_name = f"Permanent {stat}"
            self.add_item(name=item_name, classification=ItemClassification.useful)

    def add_fillers(self):
        for filler in self.data["filler"]:
            item_name = f"{filler}"
            self.add_item(name=item_name, classification=ItemClassification.filler)

    def add_traps(self):
        for trap in self.data["traps"]:
            item_name = f"{trap}"
            self.add_item(name=item_name, classification=ItemClassification.trap)

# TODO Maybe cut data and get filler item thru default_item_classifications?
class ItemCreator:
    def __init__(self, world, data):
        self.world = world
        self.data = data

    # Create actual locations in the world
    # TODO Create all items in the world
    def create_all_items(self):
        pass

    def create_item_with_classification(self, name):
        classification = self.world.default_item_classifications[name]
        return BountyOfOneItem(name, classification, self.world.item_name_to_id[name], self.world.player)

    def get_random_filler_item_name(self):
        if self.world.random.randint(1,100) <= self.world.options.trap_chance:
            return self.world.random.choice(self.data["traps"])
        return self.world.random.choice(self.data["filler"])