
# 🗝️Fantasy Sports API🗝️

A FastAPI-based backend API that provides endpoints to retrieve data on fantasy sports operators, game types, slate names, and player statistics. 
The data is loaded from a JSON file, and several filters can be applied to get specific subsets of data.




## Table of Contents

- Setup
- Usage
- API Endpoints
  - GET /api/operators
  - GET /api/operatorGameTypes
  - GET /api/slateNames
  - GET /api/players
- Development
  
## Setup
1.Clone this repository:

     git clone https://github.com/oussama-smart/FantasyFootball-backend

2.Navigate into the project directory:

     cd FantasyFootball-backend

3.Create a virtual environment (optional, but recommended):
     python -m venv venv

4.Install the required dependencies:

     pip install -r requirements.txt

5.Ensure you have the data.json file in the root directory with the required data format.

6.Run the FastAPI app:

     uvicorn main:app --reload
     The API should now be available at http://127.0.0.1:8000.

## Usage

     Once the server is running, you can access the following API endpoints.
## API Endpoints

##### GET /api/operators
     Description:Returns a list of unique operators.
     Parameters:None
     Response:
        ["Operator1", "Operator2", "Operator3"]

##### GET /api/operatorGameTypes
     Description:Returns a list of unique game types filtered by the operator, if provided.
     Parameters:
            operator (optional): Filter by operator name (e.g., Operator1).
     Response:
            ["GameType1", "GameType2"]

##### GET /api/slateNames
     Description:Returns a list of unique slate names filtered by operator and/or game type, if provided.
     Parameters:
            operator (optional): Filter by operator name (e.g., Operator1).
            operatorGameType (optional): Filter by operator game type (e.g., GameType1).
     Response:
            ["SlateName1", "SlateName2"]
##### GET /api/players

     Description:Returns a list of players with various details, optionally filtered by    operator, game type, and slate name.
     Parameters:
        operator (optional): Filter by operator name (e.g., Operator1).
        operatorGameType (optional): Filter by operator game type (e.g., GameType1).
        slateName (optional): Filter by slate name (e.g., SlateName1).
        page (optional): The page number for pagination (default is 1).
        limit (optional): The number of players per page (default is 10).
     Response:
        [
            {
                "playerId": 1,
                "operatorPlayerName": "Player1",
                "position": "Forward",
                "team": "Team A",
                "salary": 10000,
                "fantasyPoints": 50.0,
                "projectedOwnership": 0.12
            },
            {
                "playerId": 2,
                "operatorPlayerName": "Player2",
                "position": "Guard",
                "team": "Team B",
                "salary": 8000,
                "fantasyPoints": 40.0,
                "projectedOwnership": 0.08
            }
        ]