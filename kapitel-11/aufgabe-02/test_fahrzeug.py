import pytest
from fahrzeug import Fahrzeug


def test_kilometerstand_wird_bei_gueltiger_fahrt_erhoeht():
    fahrzeug = Fahrzeug("B-AB 123", 15000)
    fahrzeug.kilometerstand_erhoehen(120)
    assert fahrzeug.kilometerstand == 15120


def test_mehrere_fahrten_werden_aufsummiert():
    fahrzeug = Fahrzeug("B-AB 123", 0)
    fahrzeug.kilometerstand_erhoehen(50)
    fahrzeug.kilometerstand_erhoehen(30)
    fahrzeug.kilometerstand_erhoehen(20)
    assert fahrzeug.kilometerstand == 100


def test_negative_kilometerangabe_wird_abgelehnt():
    fahrzeug = Fahrzeug("B-AB 123", 1000)
    with pytest.raises(ValueError):
        fahrzeug.kilometerstand_erhoehen(-10)
    assert fahrzeug.kilometerstand == 1000


def test_null_kilometer_wird_abgelehnt():
    fahrzeug = Fahrzeug("B-AB 123", 500)
    with pytest.raises(ValueError):
        fahrzeug.kilometerstand_erhoehen(0)
    assert fahrzeug.kilometerstand == 500


def test_kilometerstand_bleibt_unveraendert_nach_fehlerhafter_eingabe():
    fahrzeug = Fahrzeug("M-XY 987", 20000)
    with pytest.raises(ValueError):
        fahrzeug.kilometerstand_erhoehen(-5)
    fahrzeug.kilometerstand_erhoehen(10)
    assert fahrzeug.kilometerstand == 20010
