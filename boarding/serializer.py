from marshmallow import Schema, fields
from boarding.bos import BoardingCard


class BoardingCardSchema(Schema):
    transportation = fields.Str(required=True)
    transportation_number = fields.Str(required=False, allow_none=True)
    origin = fields.Str(required=True)
    destination = fields.Str(required=True)
    seat = fields.Str(required=False, allow_none=True)
    gate = fields.Str(required=False, allow_none=True)
    baggage_drop = fields.Str(required=False, allow_none=True)


class BoardingCardsSchema(Schema):
    boarding_cards = fields.Nested(BoardingCardSchema, many=True, required=True)

    @staticmethod
    def get_card_objects(data):
        return [
            BoardingCard(
                card.get("transportation"),
                card.get("transportation_number"),
                card.get("origin"),
                card.get("destination"),
                card.get("seat"),
                card.get("gate"),
                card.get("baggage_drop"),
            )
            for card in data["boarding_cards"]
        ]