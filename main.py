from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
import json

app = FastAPI()

# Load data from JSON
with open("data.json") as file:
    data = json.load(file)

class Player(BaseModel):
    playerId: int
    operatorPlayerName: str
    position: str
    team: str
    salary: int
    fantasyPoints: float
    projectedOwnership: Optional[float]

@app.get("/api/operators", response_model=List[str])
def get_operators():
    """
    Get a list of unique operators.
    """
    operators = list({slate["operator"] for slate in data})
    return operators


@app.get("/api/operatorGameTypes", response_model=List[str])
def get_operator_game_types(operator: str = None):
    """
    Get a list of unique operator game types, optionally filtered by operator.
    """
    filtered_data = data
    if operator:
        filtered_data = [slate for slate in data if slate["operator"] == operator]
    game_types = list({slate["operatorGameType"] for slate in filtered_data})
    return game_types


@app.get("/api/slateNames", response_model=List[str])
def get_slate_names(operator: str = None, operatorGameType: str = None):
    """
    Get a list of unique slate names, optionally filtered by operator and game type.
    """
    filtered_data = data
    if operator:
        filtered_data = [slate for slate in filtered_data if slate["operator"] == operator]
    if operatorGameType:
        filtered_data = [slate for slate in filtered_data if slate["operatorGameType"] == operatorGameType]
    slate_names = list({slate["operatorName"] for slate in filtered_data})
    return slate_names


@app.get("/api/players", response_model=List[Player])
def get_players(
    operator: Optional[str] = Query(None, description="Filter by operator name"),
    operatorGameType: Optional[str] = Query(None, description="Filter by operator game type"),
    slateName: Optional[str] = Query(None, description="Filter by slate name"),
    page: int = Query(1, description="Page number"),
    limit: int = Query(10, description="Number of players per page")
):
    """
    Get a list of players, optionally filtered by operator, game type, and slate name.
    """
    # Apply filters based on query parameters
    filtered_data = data
    if operator:
        filtered_data = [item for item in filtered_data if item["operator"] == operator]
    if operatorGameType:
        filtered_data = [item for item in filtered_data if item["operatorGameType"] == operatorGameType]
    if slateName:
        filtered_data = [item for item in filtered_data if item["operatorName"] == slateName]

    # Extract players
    players = []
    for slate in filtered_data:
        players.extend(slate["dfsSlatePlayers"])

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated_players = players[start:end]

    # Map player data to the Player model
    response = [
        Player(
            playerId=player.get("playerId", None),
            operatorPlayerName=player.get("operatorPlayerName", ""),
            position=player.get("operatorPosition", ""),
            team=player.get("team", ""),
            salary=player.get("operatorSalary", 0),
            fantasyPoints=player.get("fantasyPoints", 0),
            projectedOwnership=player.get("projectedOwnership", None),
        )
        for player in paginated_players
    ]

    return response
