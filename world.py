from worlds.AutoWorld import World

from . import items, locations, regions
from . import options as boo_options
from .data import boo_data
from ..oot import location_name_to_id


class BountyOfOneWorld(World):
    game = "Bounty of One"

    options_dataclass = boo_options.BountyOfOneOptions # DONE
    options: boo_options.BountyOfOneOptions # DONE

    location_name_to_id = locations.LocationBuilder(boo_data).create_location_list() # DONE
    item_name_to_id, default_item_classifications = items.ItemBuilder(boo_data).create_item_list() # DONE

    origin_region_name = "Menu"

    def __init__(self, world, player):
        super().__init__(world, player)

        self.location_creator = locations.LocationCreator(self, boo_data)
        self.item_creator = items.ItemCreator(self, boo_data)
        self.region_manager = regions.RegionManager(self, boo_data)

        self.character_pool = self.world.random.sample(self.data["characters"], self.world.options.character_pool)

    def create_regions(self):
        self.region_manager.create_and_connect_regions() # DONE
        self.location_creator.create_all_locations() # DONE

    def set_rules(self):
        self.region_manager.set_all_rules() # DONE
        if self.options.unlock_sheriffs:
            self.location_creator.set_location_rules(location_name_to_id) # DONE

    def create_items(self):
        self.item_creator.create_all_items() # NOT DONE

    def create_item(self, name):
        return self.item_creator.create_item_with_classification(name) # DONE

    def get_filler_item_name(self):
        return self.item_creator.get_random_filler_item_name() # DONE (needs rework maybe)

    def fill_slot_data(self):
        pass # NOT DONE