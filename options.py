from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle

class UnlockSheriffs(Toggle):
    """
    Adds 5 items which each unlock one sheriff
    Run ends early if you don't have the appropriate sheriff unlocked when it would normally appear
    """
    display_name = "Unlock Sheriffs"

# TODO Check that CharacterPool >= CharacterRequired
class CharacterPool(Range):
    """
    Amount of characters in the item pool
    More characters create more locations
    """
    display_name = "Character Pool"
    range_start = 1
    range_end = 12
    default = 12

# TODO Check that MaxInfamy >= InfamyRequired
class MaxInfamy(Range):
    """
    How many progressive Infamy Items in the pool
    """
    display_name = "Maximum Infamy"
    range_start = 0
    range_end = 10
    default = 10

class InfamyGoal(Range):
    """
    Minimum Infamy Level for a goaled run
    """
    display_name = "Infamy Required"
    range_start = 0
    range_end = 10
    default = 10

class CharacterGoal(Range):
    """
    Amount of distinct characters to goal a run
    """
    display_name = "Character Required"
    range_start = 1
    range_end = 12
    default = 12

class StartingCharacter(Choice):
    """
    The character which will be available from the start
    """
    display_name = "Starting Character"
    option_serra = 0
    option_nigel = 3
    option_ollin = 2
    option_natoko = 4
    option_roger = 1
    option_r0b3rt = 6
    option_madlyn = 5
    option_jody = 7
    option_ernesto = 9
    option_sisyphus = 12
    option_richard = 13
    option_mitchell = 14

    default = option_serra

class DeputyLocations(Range):
    """
    Amount of Deputy Checks per Character per Infamy
    """
    display_name = "Amount of Deputy Locations"
    range_start = 0
    range_end = 20
    default = 5

class UpgradeLocations(Range):
    """
    Amount of Upgrade Checks from LevelUp Chests per Character per Infamy
    """
    display_name = "Amount of Upgrade Locations"
    range_start = 0
    range_end = 20
    default = 5

class ObjectLocations(Range):
    """
    Amount of Object Checks from Deputy/Sheriff Chests per Character per Infamy
    """
    display_name = "Amount of Object Locations"
    range_start = 0
    range_end = 20
    default = 2

class TrapChance(Range):
    """
    Chance for filler items to be replaced by traps
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 20

@dataclass
class BountyOfOneOptions(PerGameCommonOptions):
    unlock_sheriffs: UnlockSheriffs
    character_pool: CharacterPool
    max_infamy: MaxInfamy
    infamy_goal: InfamyGoal
    character_goal: CharacterGoal
    starting_character: StartingCharacter
    deputy_amount: DeputyLocations
    upgrade_amount: UpgradeLocations
    object_amount: ObjectLocations
    trap_chance: TrapChance