from BaseClasses import Location
from rule_builder.rules import Has, HasAll, Rule
from . import items

class BountyOfOneLocation(Location):
    game = "Bounty of One"

class LocationBuilder:
    def __init__(self, data):
        self.next_id = 708145
        self.data = data
        self.location_name_to_id = {}

    # Create all possible locations
    def create_location_list(self):
        self.add_sheriff_locations()
        self.add_character_locations()
        self.add_level_locations()
        self.add_achievement_locations()
        self.add_shop_locations()
        return self.location_name_to_id

    # Helper function to add a location to the location list
    def add_location(self, name):
        self.location_name_to_id[name] = self.next_id
        self.next_id += 1

    def add_sheriff_locations(self):
        for sheriff in self.data["sheriffs"]:
            for character in self.data["characters"]:
                for infamy in range(11):
                    location_name = f"{character} - Sheriff {sheriff} #{infamy}"
                    self.add_location(location_name)

    def add_character_locations(self):
        for character in self.data["characters"]:
            for infamy in range(11):
                for count in range(1, 21):
                    deputy_location = f"{character} - Deputy {count} #{infamy}"
                    object_location = f"{character} - Object {count} #{infamy}"
                    upgrade_location = f"{character} - Upgrade {count} #{infamy}"
                    self.add_location(deputy_location)
                    self.add_location(object_location)
                    self.add_location(upgrade_location)

    def add_level_locations(self):
        pass

    def add_achievement_locations(self):
        pass

    def add_shop_locations(self):
        pass



class LocationCreator:
    def __init__(self, world, data):
        self.world = world
        self.data = data

    def create_all_locations(self):
        self.create_locations()
        self.create_completion()

    # Helper function to add a location to the world
    def add_location(self, region, name):
        location_with_id = self.get_location_names_with_ids(name)
        region.add_locations(location_with_id, BountyOfOneLocation)

    # Create actual locations in the world
    def create_locations(self):
        for character in self.world.character_pool:
            for infamy in range(self.world.options.max_infamy + 1):
                region = self.world.get_region(f"{character} Infamy {infamy}")

                for deputy_n in range(1, self.world.options.deputy_amount + 1):
                    self.add_location(region, f"{character} - Deputy {deputy_n} #{infamy}")

                for upgrade_n in range(1, self.world.options.upgrade_amount + 1):
                    self.add_location(region, f"{character} - Upgrade {upgrade_n} #{infamy}")

                for object_n in range(1, self.world.options.max_object + 1):
                    self.add_location(region, f"{character} - Object {object_n} #{infamy}")

                for sheriff in self.data["sheriffs"]:
                    self.add_location(region, f"{character} - Sheriff {sheriff} #{infamy}")

    def set_location_rules(self, location_name_to_id):
        tom = Has("Simple Tom Unlock")
        rex = Has("Rex, Cupcake and Brutus Unlock")
        ruth = Has("Ruthless Ruth Unlock") & (tom | rex)
        denzel = Has("Crazy Denzel Unlock") & (tom | rex)
        undertaker = Has("Undertaker Unlock") & (ruth | denzel)

        rules = {
            "Simple Tom": tom,
            "Rex, Cupcake and Brutus": rex,
            "Ruthless Ruth": ruth,
            "Crazy Denzel": denzel,
            "Undertaker": undertaker,
        }

        for location_name in location_name_to_id:
            for sheriff, rule in rules.items():
                if sheriff in location_name:
                    location = self.world.get_location(location_name)
                    self.world.set_rule(location, rule)
                    break

    def create_completion(self):
        infamy_goal = self.world.options.infamy_goal
        for region in self.world.multiworld.get_regions(self.world.player):
            if region.name.contains(f"Infamy {infamy_goal}"):
                character = region.name.split()[0]
                region.add_event(
                    f"Victory {character}", "Victory", location_type=BountyOfOneLocation,
                    item_type=items.BountyOfOneItem
                )


    def get_location_names_with_ids(self, location_names):
        return {location_name: self.world.location_name_to_id[location_name] for location_name in location_names}