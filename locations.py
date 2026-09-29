from BaseClasses import Location
from . import items

class BountyOfOneLocation(Location):
    game = "Bounty of One"

class LocationBuilder:
    def __init__(self, data):
        self.next_id = 708145
        self.data = data
        self.location_name_to_id = {}

    def create_location_list(self):
        self.add_sheriff_locations()
        self.add_deputy_locations()
        self.add_choice_locations()
        self.add_shop_locations()
        self.add_achievement_locations()
        return self.location_name_to_id

    def add_location(self, name):
        self.location_name_to_id[name] = self.next_id
        self.next_id += 1

    # TODO Create a full list of IDs for every location possible (not just needed in the world)
    def add_sheriff_locations(self):
        pass

    def add_deputy_locations(self):
        pass

    def add_choice_locations(self):
        pass

    def add_shop_locations(self):
        pass

    def add_achievement_locations(self):
        pass

    # probably not needed since all locations will be locked behind region locks
    def set_location_rules(self):
        pass



class LocationCreator:
    def __init__(self, world, data):
        self.world = world
        self.data = data

    def create_all_locations(self):
        self.create_locations()
        self.create_completion()

    # TODO Create actual locations in the world
    def create_locations(self):
        pass

    def create_completion(self):
        # Undertaker
        if self.world.options.goal == 0:
            for region in self.world.multiworld.get_regions(self.world.player):
                if region.name == "Undertaker":
                    for character in self.data["characters"]:
                        region.add_event(
                            f"Victory {character}", "Victory", location_type=BountyOfOneLocation,
                            item_type=items.BountyOfOneItem
                    )
                elif region.name.startswith("Undertaker"):
                    _, character = region.name.split()
                    region.add_event(
                        f"Victory {character}", "Victory", location_type=BountyOfOneLocation,
                        item_type=items.BountyOfOneItem
                    )
        # TODO Infamy
        if self.world.option.goal == 1:
            pass


    def get_location_names_with_ids(self, location_names):
        return {location_name: self.world.location_name_to_id[location_name] for location_name in location_names}