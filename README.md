FastAPI Backend for Fantasy Sports Player Management
This project provides a backend service for managing fantasy sports players, supporting operations such as selecting an operator, filtering by game type, slate name, and retrieving player details. The service includes features such as pagination and allows the user to interact with different aspects of a fantasy sports slate.

Features
Operator Selection: Get a list of unique operators to select.
Game Type Selection: Based on the selected operator, fetch the corresponding game types.
Slate Name Selection: Select a game type to retrieve the relevant slate names.
Player List: Display a list of players based on selected filters, including operator, game type, and slate name. Players can be paginated for better performance.
Responsive: The backend is optimized for desktop layouts (md and up), but mobile responsiveness is not a requirement.
Setup
Clone the repository to your local machine:

bash
Copy code
git clone (https://github.com/oussama-smart/FantasyFootball-backend)
cd <project_directory>
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Create or update the data.json file with your data structure. Ensure that the file contains the necessary fantasy sports data, including operator, operatorGameType, operatorName, and dfsSlatePlayers.

Start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
This will start the server on http://localhost:8000.

API Endpoints
<b>1. Get Operators</b>
Endpoint: /api/operators
Method: GET

Fetch a list of unique operators.

Example Request:
http
Copy code
GET /api/operators
Example Response:
json
Copy code
["Operator 1", "Operator 2", "Operator 3"]
<b>2. Get Operator Game Types</b>
Endpoint: /api/operatorGameTypes
Method: GET
Query Parameters:

operator: (Optional) Filter by operator name.
Fetch a list of unique operator game types filtered by the selected operator.

Example Request:
http
Copy code
GET /api/operatorGameTypes?operator=Operator 1
Example Response:
json
Copy code
["Game Type 1", "Game Type 2"]
<b>3. Get Slate Names</b>
Endpoint: /api/slateNames
Method: GET
Query Parameters:

operator: (Optional) Filter by operator name.
operatorGameType: (Optional) Filter by operator game type.
Fetch a list of unique slate names filtered by the selected operator and game type.

Example Request:
http
Copy code
GET /api/slateNames?operator=Operator 1&operatorGameType=Game Type 1
Example Response:
json
Copy code
["Slate 1", "Slate 2"]
<b>4. Get Players</b>
Endpoint: /api/players
Method: GET
Query Parameters:

operator: (Optional) Filter by operator name.
operatorGameType: (Optional) Filter by operator game type.
slateName: (Optional) Filter by slate name.
page: (Optional, default: 1) Page number for pagination.
limit: (Optional, default: 10) Number of players per page.
Fetch a list of players, optionally filtered by operator, game type, and slate name. Supports pagination.

Example Request:
http
Copy code
GET /api/players?operator=Operator 1&operatorGameType=Game Type 1&slateName=Slate 1&page=1&limit=10
Example Response:
json
Copy code
[
  {
    "playerId": 1,
    "operatorPlayerName": "Player 1",
    "position": "Forward",
    "team": "Team A",
    "salary": 5000,
    "fantasyPoints": 30.5,
    "projectedOwnership": 0.12
  },
  {
    "playerId": 2,
    "operatorPlayerName": "Player 2",
    "position": "Guard",
    "team": "Team B",
    "salary": 4800,
    "fantasyPoints": 28.1,
    "projectedOwnership": 0.15
  }
]
Pagination
The player list is paginated by default. Use the page and limit query parameters to control pagination.

page: The current page of players (default is 1).
limit: The number of players per page (default is 10).
Example:

http
Copy code
GET /api/players?limit=5&page=2
This request will return the second page of players, with 5 players per page.

Models
Player Model
The Player model represents a player in the system. It includes the following attributes:

playerId: The unique ID of the player.
operatorPlayerName: The name of the player from the operator.
position: The position of the player.
team: The team the player belongs to.
salary: The player's salary.
fantasyPoints: The player's fantasy points.
projectedOwnership: The projected ownership of the player (optional).
Slate Model
A slate consists of operator, game type, slate name, and a list of players associated with that slate.

Deployment
For production deployments, consider using Docker to containerize the FastAPI app and deploy it with Kubernetes or another container orchestration system.