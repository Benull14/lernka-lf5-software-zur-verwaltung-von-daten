from fahrzeug import Fahrzeug


def test_fahrzeugdaten_anzeigen_liefert_string():
    fahrzeug = Fahrzeug("VW", "Golf", 2020, "M-AB 1234", 45000)
    ergebnis = fahrzeug.fahrzeugdaten_anzeigen()
    assert isinstance(ergebnis, str)


def test_fahrzeugdaten_anzeigen_enthaelt_alle_werte():
    fahrzeug = Fahrzeug("VW", "Golf", 2020, "M-AB 1234", 45000)
    ergebnis = fahrzeug.fahrzeugdaten_anzeigen()
    assert "VW" in ergebnis
    assert "Golf" in ergebnis
    assert "2020" in ergebnis
    assert "M-AB 1234" in ergebnis
    assert "45000" in ergebnis


def test_fahrzeugdaten_anzeigen_hat_erwartetes_format():
    fahrzeug = Fahrzeug("Opel", "Corsa", 2018, "K-XY 987", 78000)
    ergebnis = fahrzeug.fahrzeugdaten_anzeigen()
    erwartet = (
        "Marke: Opel\n"
        "Modell: Corsa\n"
        "Baujahr: 2018\n"
        "Kennzeichen: K-XY 987\n"
        "Kilometerstand: 78000 km"
    )
    assert ergebnis == erwartet


def test_fahrzeugdaten_anzeigen_mit_anderen_werten():
    fahrzeug = Fahrzeug("Audi", "A4", 2022, "B-CD 456", 5000)
    ergebnis = fahrzeug.fahrzeugdaten_anzeigen()
    erwartet = (
        "Marke: Audi\n"
        "Modell: A4\n"
        "Baujahr: 2022\n"
        "Kennzeichen: B-CD 456\n"
        "Kilometerstand: 5000 km"
    )
    assert ergebnis == erwartet
