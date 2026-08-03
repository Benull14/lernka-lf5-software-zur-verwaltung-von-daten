class Fahrzeug:
    """Repräsentiert ein Fahrzeug im Fuhrpark einer Werkstatt."""

    def __init__(self, kennzeichen: str, kilometerstand: int = 0) -> None:
        self.kennzeichen = kennzeichen
        self.kilometerstand = kilometerstand

    def kilometerstand_erhoehen(self, gefahrene_km: int) -> None:
        """Erhöht den Kilometerstand um die gefahrenen Kilometer.

        Gibt nichts zurück (None).
        """
        raise NotImplementedError("TODO")
