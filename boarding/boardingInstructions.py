from typing import List

from .bos import BoardingCard


class BoardingInstructionsService:
    def __init__(self) -> None:
        pass

    def get_boarding_instructions(self, boarding_cards: List[BoardingCard]):

        # Get the origins and destinations
        origins, destinations = self.__get_origins_destinations(boarding_cards)

        # Sort the boarding cards
        sorted_cards = self.__sort_boarding_cards(boarding_cards, origins, destinations)

        # Generate the journey description
        journey_description = self.__generate_journey_description(sorted_cards)

        # Check for directed cyclic graph
        if self.__is_connected(origins, destinations):
            comments = "This is a connected graph, output is complete"
        else:
            comments = "This is not a connected graph, output can be inaccurate"

        return journey_description, comments

    def __get_origins_destinations(self, boarding_cards: List[BoardingCard]) -> set:
        """
        Get the origins and destinations from the boarding cards.
        """
        origins = set()
        destinations = set()
        for card in boarding_cards:
            origins.add(card.origin)
            destinations.add(card.destination)
        return origins, destinations

    def __sort_boarding_cards(
        self, boarding_cards: List[BoardingCard], origins: set, destinations: set
    ) -> List[BoardingCard]:
        """
        Algorithm: Topological Sort
        Assumes the input in the form of a directed acyclic graph(DAG).
        1. Determine the starting point by finding the card with no origin.
        2. Perform a depth first search on the graph.
        3. Reverse the list to get the correct order.
        O(V + E) time complexity (V = number of vertices, E = number of edges or number of boarding cards n)
        """

        # Determine starting point
        start = None
        for card in boarding_cards:
            if card.origin not in destinations:
                start = card
                break

        # Perform topological sort
        sorted_cards = []
        visited = set()
        self.__dfs(start, visited, sorted_cards, boarding_cards)

        # Reverse the list to get the correct order
        sorted_cards.reverse()

        return sorted_cards

    def __dfs(
        self,
        card: BoardingCard,
        visited: set,
        sorted_cards: List[BoardingCard],
        boarding_cards: List[BoardingCard],
    ):
        visited.add(card)
        for next_card in boarding_cards:
            if next_card not in visited and next_card.origin == card.destination:
                self.__dfs(next_card, visited, sorted_cards, boarding_cards)

        sorted_cards.append(card)

    def __is_connected(self, origins: set, destinations: set) -> bool:
        """
        Determine if the given set of origins and destinations is connected.
        """
        return (
            len(origins)
            == len(destinations)
            == len(set.union(origins, destinations)) - 1
        )

    def __generate_journey_description(
        self, sorted_cards: List[BoardingCard]
    ) -> List[str]:
        """
        Generate the journey description from the sorted boarding cards.
        This is a simple implementation;
        ideally we have to create templates as static inputs of fetching from a database.
        Like fetch baggageDrop type etc.
        """
        journey_description = []
        for i in range(len(sorted_cards)):
            description = ""
            card = sorted_cards[i]
            if i == 0:
                description = description + (
                    f"Take {card.transportation} from {card.origin} to {card.destination}."
                )
            else:
                prev_card = sorted_cards[i - 1]
                description = description + (
                    f"From {prev_card.destination}, take {card.transportation} to {card.destination}."
                )
            if card.gate and card.seat:
                description = description + (f" Gate {card.gate}, seat {card.seat}.")
            elif card.seat and not card.gate:
                description = description + (f" Sit in seat {card.seat}.")
            else:
                description = description + (f" No seat assignment.")
            if card.baggageDrop:
                if card.baggageDrop == "automatic":
                    description = description + (
                        f" Baggage will be automatically transferred from your last leg."
                    )
                else:
                    description = description + (
                        f" Baggage drop at {card.baggageDrop}."
                    )

            journey_description.append(description)

        journey_description.append("You have arrived at your final destination.")

        return journey_description
