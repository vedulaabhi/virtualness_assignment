# Boarding Instructions

This is a small flask app which exposes an API to manage boarding instructions given a list of boarding cards of a journey.

## Assumptions
API assumes that the boarding cards given form a DAG (Directed Acyclic Graph) and that the graph is connected. If the graph is not connected, the API will return a success with a message indicating that the graph is not connected. In that case, the API will return a list of connected subgraphs.

## API Contract
The API exposes a single endpoint `/boardingInstructions` which accepts a POST request with a JSON body containing a list of boarding cards. The API will return a JSON response with the boarding instructions.
body:
```
{
    "boardingCards": [
        {
            "origin": "Madrid",
            "destination": "Barcelona",
            "transportation": "train",
            "seat": "45B",
            "gate": "45B",
            "baggageDrop": "auto"
        },
        {
            "origin": "Gerona Airport",
            "destination": "Stockholm",
            "transportation": "flight",
            "seat": "3A",
            "gate": "45B",
            "baggageDrop": "auto"
        },
        {
            "origin": "Stockholm",
            "destination": "New York JFK",
            "transportation": "flight",
            "seat": "7B",
            "gate": "22",
            "baggageDrop": "auto"
        },
        {
            "origin": "Barcelona",
            "destination": "Gerona Airport",
            "transportation": "airport bus"
        }
    ]
}
```
response:
```
{
    "comments": "This is a connected graph, output is complete",
    "instructions": [
        "Take train from Madrid to Barcelona. Gate 45B, seat 45B. Baggage drop at auto.",
        "From Barcelona, take airport bus to Gerona Airport. No seat assignment.",
        "From Gerona Airport, take flight to Stockholm. Gate 45B, seat 3A. Baggage drop at auto.",
        "From Stockholm, take flight to New York JFK. Gate 22, seat 7B. Baggage drop at auto.",
        "You have arrived at your final destination."
    ],
    "status": "success"
}
```

### Mandatory fields
The API expects the following fields in the boarding cards:
* source
* destination
* transportation

### Optional fields
The API expects the following fields in the boarding cards:
* seat
* gate
* baggage
* transportationNumber

## Running the app
To run the app, you need to have python 3.6 installed. Follow below steps to run the app:
* create virtual environment using `python3 -m venv venv`
* activate virtual environment using `source venv/bin/activate`
* install dependencies using `pip install -r requirements.txt`
* run the app using `python app.py`
* the app will be running on port 8080 by default

once the server is running, you can send a POST request to the endpoint `/boardingInstructions` with the body as mentioned above.
curl sample:
```curl --location 'localhost:8080/boardingInstructions' \
--header 'Content-Type: application/json' \
--data '{
    "boardingCards": [
        {
            "origin": "Madrid",
            "destination": "Barcelona",
            "transportation": "train",
            "seat": "45B",
            "gate": "45B",
            "baggageDrop": "auto"
        },
        {
            "origin": "Gerona Airport",
            "destination": "Stockholm",
            "transportation": "flight",
            "seat": "3A",
            "gate": "45B",
            "baggageDrop": "auto"
        },
        {
            "origin": "Stockholm",
            "destination": "New York JFK",
            "transportation": "flight",
            "seat": "7B",
            "gate": "22",
            "baggageDrop": "auto"
        },
        {
            "origin": "Barcelona",
            "destination": "Gerona Airport",
            "transportation": "airport bus"
        }
    ]
}'
```
Plase feel free to update the input JSON body to test the API with different inputs.
## Running the tests
To run the tests, you need to have python 3.6 installed. Once the virtual environment is activated, run the following command:
`python run_tests.py`
