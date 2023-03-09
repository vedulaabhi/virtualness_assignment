from typing import List
from flask.views import View
from flask import request, jsonify

from boarding.boardingInstructions import BoardingInstructionsService
from boarding.serializer import BoardingCardsSchema


class BordingInstructionsView(View):
    methods = ["POST"]

    def __init__(self) -> None:
        self.service = BoardingInstructionsService()

    def dispatch_request(self):
        data = request.json
        try:
            serialized_data = BoardingCardsSchema().load(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

        boarding_cards = BoardingCardsSchema.get_card_objects(serialized_data)
        instructions = self.service.get_boarding_instructions(boarding_cards)
        result = {"instructions": instructions}
        return jsonify(result)
