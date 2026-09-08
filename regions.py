from BaseClasses import Region
from rule_builder.rules import Has, HasAny, Rule

class RegionManager:
    def __init__(self, world, data):
        self.world = world
        self.data = data
        self.connections = []

    def create_and_connect_regions(self):
        self.create_regions()
        self.connect_regions()

    def set_all_rules(self):
        self.set_entrance_rules()
        self.set_completion()

    def create_regions(self):
        self.create_region_menu()
        if self.world.options.kills_per_character:
            self.create_regions_per_character()
        else:
            self.create_regions_shared()

    def add_region(self, name):
        self.world.multiworld.regions.append(Region(name,self.world.player,self.world.multiworld))

    def create_regions_per_character(self):
        """
        Region generation for option KillsPerCharacter = true
        """
        for region, leads_to in self.data["regions"].items():
            for character in self.data["characters"]:
                region_name = f"{region} {character}"
                self.add_region(region_name)
                for destination in leads_to:
                    goal_name = f"{destination} {character}"
                    self.connections.append((region_name, goal_name))

    def create_regions_shared(self):
        """
        Region generation for option KillsPerCharacter = false
        """
        for region, leads_to in self.data["regions"].items():
            self.add_region(region)
            for destination in leads_to:
                self.connections.append((region, destination))

    def create_region_menu(self):
        """
        Region generation for menu
        """
        self.add_region("Menu")
        if self.world.options.chests_per_character or self.world.options.kills_per_character:
            for character in self.data["characters"]:
                self.connections.append(("Menu", f"Character Unlocked: {character}"))
        else:
            self.connections.append(("Menu", "Phase One"))

    # TODO Missing connection from Character Unlocked to Phase One
    def connect_regions(self):
        for origin, destination in self.connections:
            connect_from = self.world.get_region(origin)
            connect_to = self.world.get_region(destination)
            connect_from.connect(connect_to, f"{origin} -> {destination}")

    def set_entrance_rules(self):
        for entrance in self.world.multiworld.get_entrances(self.world.player):
            if "Character Unlocked:" in entrance.name:
                character = entrance.name.split()[-1]
                self.world.set_rule(entrance, Has(f"{character} Unlock"))

            for sheriff, _ in self.data["sheriffs"].items():
                if sheriff in entrance.name:
                    self.world.set_rule(entrance, Has(f"{sheriff} Unlock"))

    def set_completion(self):
        pass
        #world.set_completion_rule(Has("Victory"))