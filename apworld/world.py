from worlds.AutoWorld import World

from . import items, locations, regions
from . import options as boo_options
from .data import boo_data, Rules


class BountyOfOneWorld(World):
    game = "Bounty of One"

    web = boo_options.APQuestWebWorld()

    options_dataclass = boo_options.BountyOfOneOptions
    options: boo_options.BountyOfOneOptions

    location_name_to_id = locations.LocationBuilder(boo_data).create_location_list()
    item_name_to_id, default_item_classifications = items.ItemBuilder(boo_data).create_item_list()

    origin_region_name = "Menu"

    def __init__(self, world, player):
        super().__init__(world, player)

        self.location_creator = locations.LocationCreator(self, boo_data)
        self.item_creator = items.ItemCreator(self, boo_data)
        self.region_manager = regions.RegionManager(self, boo_data)
        self.rules = Rules()

    def generate_early(self):
        ### Validate yaml options
        if self.options.required_character_count > self.options.character_count:
            raise ValueError(
                "Amount of characters required to goal cannot be higher than the amount of characters in the pool."
            )

        if self.options.required_infamy_level > self.options.max_infamy_level:
            raise ValueError(
                "Infamy Level required to goal cannot be higher than the Maximum Infamy Level."
            )


        ### Create character pool and starting character
        starting_character = self.options.starting_character.current_key.capitalize()

        available_characters = [
            character for character in boo_data["characters"] if character != starting_character
        ]

        self.character_pool = [
            starting_character,
            *self.random.sample(available_characters, self.options.character_count - 1)
            ]
        self.multiworld.push_precollected(self.create_item(f"Character {starting_character} Unlock"))

    def create_regions(self):
        self.region_manager.create_and_connect_regions()
        self.location_creator.create_all_locations()

    def set_rules(self):
        self.region_manager.set_all_rules()
        if self.options.sheriff_unlocks:
            self.location_creator.set_location_rules()

    def create_items(self):
        self.item_creator.create_all_items()

    def create_item(self, name):
        return self.item_creator.create_item_with_classification(name)

    def get_filler_item_name(self):
        return self.item_creator.get_random_filler_item_name()

    def fill_slot_data(self):
        pass