class Fahrzeug:
    """Repraesentiert ein Fahrzeug im Fuhrpark einer Werkstatt."""

    def __init__(self, marke: str, modell: str, baujahr: int, kennzeichen: str, kilometerstand: int) -> None:
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kennzeichen = kennzeichen
        self.kilometerstand = kilometerstand

    def fahrzeugdaten_anzeigen(self) -> str:
        """Gibt alle Fahrzeugdaten als einheitlich formatierten String zurueck."""
        raise NotImplementedError("TODO")
