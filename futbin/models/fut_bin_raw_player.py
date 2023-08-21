from dataclasses import dataclass
from typing import List


@dataclass
class FutBinRawPlayer:
    id: str = ""
    name: str = ""
    rating: str = ""
    qualityAndRarity: List[str] = None
    clubId: str = ""
    clubName: str = ""
    nationId: str = ""
    nationName: str = ""
    leagueId: str = ""
    leagueName: str = ""

    mainPosition: str = ""
    otherPositions: List[str] = None

    priceText: str = ""

