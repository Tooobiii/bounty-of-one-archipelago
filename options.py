from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, DefaultOnToggle

class Goal(Choice):
    """
    What to do to goal
    undertaker: Beat Undertaker with a number of characters
    infamy: Finish a run with a certain Infamy Level (0-10)
    """
    option_undertaker = 0
    option_infamy = 1

    default = option_infamy

class GoalWithCharacters(Range):
    """
    Amount of Characters to beat Undertaker
    Only applies if goal is set to option_undertaker
    """
    display_name = "Goal With Characters"
    range_start = 1
    range_end = 12
    default = 4

class GoalWithInfamy(Range):
    """
    Level of Infamy required for a run to count as goaled
    Only applies if goal is set to option_infamy
    """
    display_name = "Goal With Infamy"
    range_start = 1
    range_end = 10
    default = 10

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

class KillsPerCharacter(DefaultOnToggle):
    """
    Should each character have their own deputy and sheriff checks?
    If disabled, all those checks will consequently be in sphere 1.
    """
    display_name = "Deputy Kills per Character"

class DeputyKillsPhaseOne(Range):
    """
    Amount of Deputy Checks in Phase One
    """
    display_name = "Deputy Kills Phase One"
    range_start = 0
    range_end = 100
    default = 20

class DeputyKillsPhaseTwo(Range):
    """
    Amount of Deputy Checks in Phase Two
    """
    display_name = "Deputy Kills Phase Two"
    range_start = 0
    range_end = 100
    default = 15

class DeputyKillsPhaseThree(Range):
    """
    Amount of Deputy Checks in Phase Three
    """
    display_name = "Deputy Kills Phase Three"
    range_start = 0
    range_end = 100
    default = 10

class ChestsPerCharacter(DefaultOnToggle):
    """
    Should each character have their own upgrade checks?
    If disabled, all those checks will consequently be in sphere 1.
    """
    display_name = "Upgrade Amount per Character"

class UpgradeAmount(Range):
    """
    Total amount of Upgrade Checks from LevelUp Chests
    """
    display_name = "Upgrades per Character"
    range_start = 0
    range_end = 200
    default = 50

class ObjectAmount(Range):
    """
    Total amount of Objects Checks from Deputy/Sheriff Chests
    """
    display_name = "Objects per Character"
    range_start = 0
    range_end = 50
    default = 10

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
    goal: Goal
    goal_with_characters: GoalWithCharacters
    goal_with_infamy: GoalWithInfamy
    starting_character: StartingCharacter
    kills_per_character: KillsPerCharacter
    phase_one_deputies: DeputyKillsPhaseOne
    phase_two_deputies: DeputyKillsPhaseTwo
    phase_three_deputies: DeputyKillsPhaseThree
    chests_per_character: ChestsPerCharacter
    upgrade_amount: UpgradeAmount
    object_amount: ObjectAmount
    trap_chance: TrapChance