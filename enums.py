from enum import Enum

class League(Enum):
    Standard = 0
    Hardcore = 1
    SSFStandard = 2
    SSFHardcore = 3
    Bestiary = 4
    HardcoreBestiary = 5
    SSFBestiary = 6
    SSFHardcoreBestiary = 7
    Flashback = 8
    HCFlashback = 9
    SSFFlashback = 10
    SSFHCFlashback = 11

    def map_enum_to_str(league):
        print(league)
        return {
            0: 'Standard',
            1: 'Hardcore',
            2: 'SSF Standard',
            3: 'SSF Hardcore',
            4: 'Bestiary',
            5: 'Hardcore Bestiary',
            6: 'SSF Bestiary',
            7: 'SSF Bestiary HC',
            8: 'Flashback Event (BRE001)',
            9: 'HC Flashback Event (BRE002)',
            10: 'SSF Flashback Event (BRE003)',
            11: 'HC SSF Flashback Event (BRE004)',
        }.get(int(league), 'Standard')
