import pytest

from bibliothek import maximum


def test_mehrere_werte():
    messwerte = [72.5, 88.1, 65.3, 91.7, 80.0]
    assert maximum(messwerte) == 91.7


def test_einzelner_wert():
    assert maximum([42.0]) == 42.0


def test_hoechster_wert_am_anfang():
    messwerte = [99.9, 50.0, 60.0, 70.0]
    assert maximum(messwerte) == 99.9


def test_hoechster_wert_am_ende():
    messwerte = [10.0, 20.0, 30.0, 100.0]
    assert maximum(messwerte) == 100.0


def test_negative_werte():
    messwerte = [-5.0, -12.3, -1.0, -20.0]
    assert maximum(messwerte) == -1.0


def test_gleiche_werte():
    messwerte = [55.5, 55.5, 55.5]
    assert maximum(messwerte) == 55.5


def test_leere_liste_wirft_fehler():
    with pytest.raises(ValueError):
        maximum([])
