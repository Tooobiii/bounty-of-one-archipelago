from BaseClasses import Location

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
        location_with_id = self.get_location_name_with_id(name)
        region.add_locations(location_with_id, BountyOfOneLocation)

    # Create actual locations in the world
    def create_locations(self):
        for character in self.world.character_pool:
            for infamy in range(self.world.options.max_infamy_level + 1):
                region = self.world.get_region(f"{character} Infamy {infamy}")

                for deputy_n in range(1, self.world.options.deputy_check_count + 1):
                    self.add_location(region, f"{character} - Deputy {deputy_n} #{infamy}")

                for upgrade_n in range(1, self.world.options.upgrade_check_count + 1):
                    self.add_location(region, f"{character} - Upgrade {upgrade_n} #{infamy}")

                for object_n in range(1, self.world.options.object_check_count + 1):
                    self.add_location(region, f"{character} - Object {object_n} #{infamy}")

                for sheriff in self.data["sheriffs"]:
                    self.add_location(region, f"{character} - Sheriff {sheriff} #{infamy}")

    def set_location_rules(self):
        sheriff_rules = self.world.rules.sheriff_rules()
        for location in self.world.multiworld.get_locations(self.world.player):
            for sheriff, rule in sheriff_rules.items():
                if sheriff in location.name:
                    self.world.set_rule(location, rule)
                    break

    def create_completion(self):
        infamy_goal = self.world.options.required_infamy_level
        for region in self.world.multiworld.get_regions(self.world.player):
            if f"Infamy {infamy_goal}" in region.name:
                character = region.name.split()[0]
                event_name = f"Victory {character}"
                region.add_event(
                    event_name, "Victory", location_type=BountyOfOneLocation,
                    item_type=items.BountyOfOneItem
                )

                event = self.world.get_location(event_name)
                self.world.set_rule(event, self.world.rules.undertaker)


    def get_location_names_with_ids(self, location_names):
        return {location_name: self.world.location_name_to_id[location_name] for location_name in location_names}

    def get_location_name_with_id(self, location_name):
        return {location_name: self.world.location_name_to_id[location_name]}