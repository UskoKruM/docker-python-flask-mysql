class Position():

    def __init__(self, id: int, name: str, basichourlypay: float, active: bool = True) -> None:
        self.id = id
        self.name = name
        self.basichourlypay = basichourlypay
        self.active = active

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'basichourlypay': self.basichourlypay,
            'active': self.active
        }
