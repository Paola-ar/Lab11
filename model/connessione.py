from dataclasses import dataclass

@dataclass
class Connessione:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int

    def __repr__(self):
        return f" {self.id}, {self.id_rifugio1}, {self.id_rifugio2}"

    def __str__(self):
        return f"{self.id}, {self.id_rifugio1}, {self.id_rifugio2}"

    def __hash__(self):
        return hash(f"{self.id}, {self.id_rifugio1}, {self.id_rifugio2}")