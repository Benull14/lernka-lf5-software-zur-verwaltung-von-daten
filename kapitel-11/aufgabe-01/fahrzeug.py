"""Modul für die Klasse Fahrzeug aus der Werkstattverwaltung."""


class Fahrzeug:
    """Repräsentiert ein Fahrzeug, das in der Werkstatt aufgenommen wird."""

    def __init__(self, kennzeichen: str, marke: str, kilometerstand: int) -> None:
        """Legt die Startwerte eines neu aufgenommenen Fahrzeugs fest.

        Args:
            kennzeichen: Das amtliche Kennzeichen des Fahrzeugs.
            marke: Die Marke des Fahrzeugs.
            kilometerstand: Der aktuelle Kilometerstand des Fahrzeugs.

        Returns:
            None
        """
        raise NotImplementedError("TODO")
