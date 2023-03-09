import unittest

from typing import List
from unittest.mock import MagicMock

from boarding.boardingInstructions import BoardingInstructionsService, BoardingCard


class TestBoardingInstructionsService(unittest.TestCase):
    def setUp(self) -> None:
        self.boarding_cards = [
            BoardingCard(
                origin="A",
                destination="B",
                transportation="flight",
                gate="1",
                seat="A1",
                baggageDrop="2",
            ),
            BoardingCard(
                origin="B",
                destination="C",
                transportation="train",
                seat="B1",
            ),
            BoardingCard(
                origin="C",
                destination="D",
                transportation="bus",
                seat="C1",
                baggageDrop="automatic",
            ),
        ]
        self.boarding_instructions_service = BoardingInstructionsService()

    def test_sort_boarding_cards(self):
        expected_output = [
            self.boarding_cards[0],
            self.boarding_cards[1],
            self.boarding_cards[2],
        ]
        output = self.boarding_instructions_service._BoardingInstructionsService__sort_boarding_cards(
            self.boarding_cards
        )
        self.assertListEqual(output, expected_output)

    def test_generate_journey_description(self):
        sorted_cards = [
            self.boarding_cards[0],
            self.boarding_cards[1],
            self.boarding_cards[2],
        ]
        expected_output = [
            "Take flight from A to B. Gate 1, seat A1. Baggage drop at 2.",
            "From B, take train to C. Sit in seat B1. No baggage drop.",
            "From C, take bus to D. Sit in seat C1. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination.",
        ]
        output = self.boarding_instructions_service._BoardingInstructionsService__generate_journey_description(
            sorted_cards
        )
        self.assertListEqual(output, expected_output)

    def test_get_boarding_instructions(self):
        expected_output = [
            "Take flight from A to B. Gate 1, seat A1. Baggage drop at 2.",
            "From B, take train to C. Sit in seat B1. No baggage drop.",
            "From C, take bus to D. Sit in seat C1. Baggage will be automatically transferred from your last leg.",
            "You have arrived at your final destination.",
        ]
        output = self.boarding_instructions_service.get_boarding_instructions(
            self.boarding_cards
        )
        self.assertListEqual(output, expected_output)
