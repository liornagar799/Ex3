import math
class NodeDataImpl:

    #constructor
    def __init__(self, _key: int = -1, _Location: tuple = None) -> None:
        self._key = _key
        self._Location = _Location
        self._Weight = math.inf
        self._Info = ""
        self._Tag = 0
        self.edge_out = 0
        self.edge_in = 0

    #Convert NODE to STR
    def __str__(self) -> str:
        return f"{self._key}: |edges out| {self.edge_out} |edges in| {self.edge_in}"

    # Convert NODE to STR
    def __repr__(self) -> str:
        return f"{self._key}: |edges out| {self.edge_out} |edges in| {self.edge_in}"

    # get Key of node
    def getKey(self):
        return self._key

    # get Location of node
    def getLocation(self):
        return self._Location

    # set Location of node
    def setLocation(self, p: tuple):
        self._Location = p

    # get Weight of node
    def getWeight(self):
        return self._Weight

    # set Weight of node
    def setWeight(self, w: float):
        self._Weight = w

    # get Info of node
    def getInfo(self):
        return self._Info

    # set Info of node
    def setInfo(self, s: str):
        self._Info = s

    # get Tag of node
    def getTag(self):
        return self._Tag

    # set Tag of node
    def setTag(self, t: int):
        self._Tag = t
