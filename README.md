# Boarding Instructions

This is a small flask app to exposes an API to manage boarding instructions given given a list of boarding cards of a journey

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
        "Take train from Agra to Noida. Sit in seat 15AC.",
        "From Noida, take bus to Delhi Airport. No seat assignment.",
        "From Delhi Airport, take flight to Addis Ababa.Gate 74B, seat 7C.Baggage drop at ticket counter 433.",
        "From Addis Ababa, take flight to Stockholm.Gate 22, seat 7B.Baggage will be automatically transferred from your last leg.",
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