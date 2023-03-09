from marshmallow import Schema, fields
from boarding.bos import BoardingCard


class BoardingCardSchema(Schema):
    transportation = fields.Str(required=True)
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)
    transportationNumber = fields.Str(required=False, allow_none=True)
    seat = fields.Str(required=False, allow_none=True)
    gate = fields.Str(required=False, allow_none=True)
    baggageDrop = fields.Str(required=False, allow_none=True)


class BoardingCardsSchema(Schema):
    boardingCards = fields.Nested(BoardingCardSchema, many=True, required=True)

    @staticmethod
    def get_card_objects(data):
        return [
            BoardingCard(
                transportation=card.get("transportation"),
                transportationNumber=card.get("transportationNumber"),
                origin=card.get("origin"),
                destination=card.get("destination"),
                seat=card.get("seat"),
                gate=card.get("gate"),
                baggageDrop=card.get("baggageDrop"),
            )
            for card in data["boardingCards"]
        ]
