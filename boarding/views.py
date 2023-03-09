from typing import List
from flask.views import View
from flask import request, jsonify, make_response

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
            response = make_response(
                jsonify({"instructions": None, "comments": str(e), "status": "error"}),
                400,
            )
            return response
        boarding_cards = BoardingCardsSchema.get_card_objects(serialized_data)
        instructions, comments = self.service.get_boarding_instructions(boarding_cards)
        response = make_response(
            jsonify(
                {
                    "instructions": instructions,
                    "comments": comments,
                    "status": "success",
                }
            ),
            200,
        )

        return response
