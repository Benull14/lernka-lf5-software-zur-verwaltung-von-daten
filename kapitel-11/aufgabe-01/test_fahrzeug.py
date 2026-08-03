"""Tests für den Konstruktor der Klasse Fahrzeug."""

import pytest

from fahrzeug import Fahrzeug


def test_konstruktor_setzt_kennzeichen():
    fahrzeug = Fahrzeug("B-AB 1234", "Volkswagen", 15000)
    assert fahrzeug._kennzeichen == "B-AB 1234"


def test_konstruktor_setzt_marke():
    fahrzeug = Fahrzeug("B-AB 1234", "Volkswagen", 15000)
    assert fahrzeug._marke == "Volkswagen"


def test_konstruktor_setzt_kilometerstand():
    fahrzeug = Fahrzeug("B-AB 1234", "Volkswagen", 15000)
    assert fahrzeug._kilometerstand == 15000


def test_konstruktor_gibt_none_zurueck():
    ergebnis = Fahrzeug.__init__(
        Fahrzeug.__new__(Fahrzeug), "M-CD 5678", "BMW", 50000
    )
    assert ergebnis is None


def test_negativer_kilometerstand_wirft_fehler():
    with pytest.raises(ValueError):
        Fahrzeug("B-XY 5678", "Audi", -100)


def test_verschiedene_fahrzeuge_sind_unabhaengig():
    fahrzeug1 = Fahrzeug("B-AB 1234", "Volkswagen", 15000)
    fahrzeug2 = Fahrzeug("M-CD 5678", "BMW", 50000)

    assert fahrzeug1._kennzeichen != fahrzeug2._kennzeichen
    assert fahrzeug1._marke != fahrzeug2._marke
    assert fahrzeug1._kilometerstand != fahrzeug2._kilometerstand


def test_kilometerstand_null_ist_erlaubt():
    fahrzeug = Fahrzeug("K-NW 9999", "Opel", 0)
    assert fahrzeug._kilometerstand == 0
