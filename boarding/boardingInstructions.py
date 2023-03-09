from typing import List

from boarding.bos import BoardingCard


class BoardingInstructionsService:
    def __init__(self) -> None:
        pass

    def get_boarding_instructions(self, boarding_cards: List[BoardingCard]):
        # Sort the boarding cards
        sorted_cards = self.__sort_boarding_cards(boarding_cards)

        # Generate the journey description
        journey_description = self.__generate_journey_description(sorted_cards)

        return journey_description

    def __sort_boarding_cards(
        self, boarding_cards: List[BoardingCard]
    ) -> List[BoardingCard]:
        # Determine starting point and ending point
        start = None
        end = None
        destinations = set()
        for card in boarding_cards:
            destinations.add(card.destination)
            if card.origin not in destinations:
                start = card
        for card in boarding_cards:
            if card.destination not in destinations:
                end = card

        # Perform topological sort
        sorted_cards = []
        visited = set()
        self.__dfs(start, visited, sorted_cards, boarding_cards)

        # Reverse the list to get the correct order
        sorted_cards.reverse()

        return sorted_cards

    def __generate_journey_description(
        self, sorted_cards: List[BoardingCard]
    ) -> List[str]:

        # generate the journey description
        journey_description = []
        for i in range(len(sorted_cards)):
            card = sorted_cards[i]
            if i == 0:
                journey_description.append(
                    f"Take {card.transportation} from {card.origin} to {card.destination}. Sit in seat {card.seat}."
                )
            else:
                prev_card = sorted_cards[i - 1]
                journey_description.append(
                    f"From {prev_card.destination}, take {card.transportation} to {card.destination}."
                )
                if card.gate:
                    journey_description.append(f"Gate {card.gate}, seat {card.seat}.")
                else:
                    journey_description.append(f"No seat assignment.")
                if card.baggage_drop:
                    journey_description.append(f"Baggage drop at {card.baggage_drop}.")
                else:
                    journey_description.append(
                        f"Baggage will be automatically transferred from your last leg."
                    )
        journey_description.append("You have arrived at your final destination.")

        # join the journey description and return the result
        return "\n".join(journey_description)

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
