from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle
from worlds.AutoWorld import WebWorld

class CharacterCount(Range):
    """
    Set the number of characters that can be unlocked (including the starting character)
    More characters add more checks
    """
    display_name = "Character Pool"
    range_start = 1
    range_end = 12
    default = 6

class DeputyCheckCount(Range):
    """
    Number of Deputy checks available per Character and Infamy Level
    """
    display_name = "Deputies"
    range_start = 0
    range_end = 20
    default = 4

class MaxInfamyLevel(Range):
    """
    Maximum Infamy Level that can be unlocked
    """
    display_name = "Maximum Infamy Level"
    range_start = 0
    range_end = 10
    default = 8

class ObjectCheckCount(Range):
    """
    Number of Object checks Chests per Character and Infamy Level
    """
    display_name = "Objects"
    range_start = 0
    range_end = 20
    default = 2

class PermanentUpgradeCount(Range):
    """
    Set the number of permanent upgrades (per stat)
    """
    display_name = "Permanent Upgrades"
    range_start = 0
    range_end = 5
    default = 1

class RequiredCharacterCount(Range):
    """
    Number of different characters that must complete a run
    """
    display_name = "Character Count"
    range_start = 1
    range_end = 12
    default = 4

class RequiredInfamyLevel(Range):
    """
    Minimum Infamy Level required for a completed run to count toward the goal
    """
    display_name = "Infamy Level"
    range_start = 0
    range_end = 10
    default = 8

class SheriffUnlocks(Toggle):
    """
    Adds unlock items for all five sheriffs
    """
    display_name = "Sheriff Unlocks"

class StartingCharacter(Choice):
    """
    Choose character to start with
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

class TrapChance(Range):
    """
    Percentage chance for filler items to be replaced by traps
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 20

class UpgradeCheckCount(Range):
    """
    Number of Upgrade checks per Character and Infamy Level
    """
    display_name = "Upgrades"
    range_start = 0
    range_end = 20
    default = 4

@dataclass
class BountyOfOneOptions(PerGameCommonOptions):
    starting_character: StartingCharacter
    character_count: CharacterCount
    max_infamy_level: MaxInfamyLevel
    sheriff_unlocks: SheriffUnlocks
    trap_chance: TrapChance

    required_character_count: RequiredCharacterCount
    required_infamy_level: RequiredInfamyLevel

    deputy_check_count: DeputyCheckCount
    upgrade_check_count: UpgradeCheckCount
    object_check_count: ObjectCheckCount

    permanent_upgrade_count: PermanentUpgradeCount

option_groups = [
    OptionGroup(
        "General",
        [StartingCharacter, CharacterCount, MaxInfamyLevel, SheriffUnlocks, TrapChance],
    ),
    OptionGroup(
        "Goal Requirements",
        [RequiredCharacterCount, RequiredInfamyLevel],
    ),
    OptionGroup(
        "Locations",
        [DeputyCheckCount, UpgradeCheckCount, ObjectCheckCount],
    ),
    OptionGroup(
        "Items",
        [PermanentUpgradeCount],
    ),
]

class APQuestWebWorld(WebWorld):
    option_groups = option_groups