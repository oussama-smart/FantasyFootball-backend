<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Project Documentation</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #2d3a3b; }
        h2 { color: #4b5c5e; }
        pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; }
        .code-block { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
        .endpoint { font-weight: bold; }
    </style>
</head>
<body>
    <h1>FastAPI Project Documentation</h1>

    <h2>Requirements</h2>
    <p>To run this project, you need Python 3.7 or higher. The following dependencies are required:</p>
    <ul>
        <li>FastAPI</li>
        <li>Uvicorn</li>
        <li>Pydantic</li>
    </ul>
    <p>Install the dependencies using pip:</p>
    <pre><code>pip install fastapi uvicorn pydantic</code></pre>

    <h2>Project Structure</h2>
    <pre><code>
project/
│
├── data.json             # The JSON file containing the data (must be provided)
├── main.py               # FastAPI backend code
├── README.md             # Project documentation
    </code></pre>

    <h2>How to Run</h2>
    <ol>
        <li>Clone the repository or copy the <code>main.py</code> file and <code>data.json</code> to your local machine.</li>
        <li>Install the dependencies using the following command:</li>
        <pre><code>pip install fastapi uvicorn pydantic</code></pre>
        <li>Start the FastAPI server with the following command:</li>
        <pre><code>uvicorn main:app --reload</code></pre>
        <li>This will run the FastAPI server on <code>http://127.0.0.1:8000</code>.</li>
        <li>Once the server is running, you can access the following API endpoints.</li>
    </ol>

    <h2>API Endpoints</h2>
    <ul>
        <li><span class="endpoint">/api/operators</span> - Get a list of unique operators</li>
        <li><span class="endpoint">/api/operatorGameTypes</span> - Get a list of unique operator game types</li>
        <li><span class="endpoint">/api/slateNames</span> - Get a list of unique slate names</li>
        <li><span class="endpoint">/api/players</span> - Get a list of players, optionally filtered by various parameters</li>
    </ul>

    <h2>Example Requests</h2>
    <h3>Get List of Operators</h3>
    <pre><code>GET http://127.0.0.1:8000/api/operators</code></pre>
    <p>Response:</p>
    <pre><code>["Operator1", "Operator2", "Operator3"]</code></pre>

    <h3>Get List of Game Types for an Operator</h3>
    <pre><code>GET http://127.0.0.1:8000/api/operatorGameTypes?operator=Operator1</code></pre>
    <p>Response:</p>
    <pre><code>["GameType1", "GameType2"]</code></pre>

    <h3>Get List of Slate Names for an Operator and Game Type</h3>
    <pre><code>GET http://127.0.0.1:8000/api/slateNames?operator=Operator1&operatorGameType=GameType1</code></pre>
    <p>Response:</p>
    <pre><code>["SlateName1", "SlateName2"]</code></pre>

    <h3>Get List of Players (Paginated)</h3>
    <pre><code>GET http://127.0.0.1:8000/api/players?operator=Operator1&operatorGameType=GameType1&slateName=SlateName1&page=1&limit=10</code></pre>
    <p>Response:</p>
    <pre><code>
[
    {
        "playerId": 1,
        "operatorPlayerName": "Player1",
        "position": "Forward",
        "team": "TeamA",
        "salary": 50000,
        "fantasyPoints": 25.5,
        "projectedOwnership": 0.75
    },
    {
        "playerId": 2,
        "operatorPlayerName": "Player2",
        "position": "Guard",
        "team": "TeamB",
        "salary": 45000,
        "fantasyPoints": 20.3,
        "projectedOwnership": 0.65
    }
]
    </code></pre>
</body>
</html>
