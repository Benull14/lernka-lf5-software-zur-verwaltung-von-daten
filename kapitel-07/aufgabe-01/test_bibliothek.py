import pytest

from bibliothek import summe_liste


def test_summe_mehrere_werte():
    bestellwerte = [19.99, 5.50, 100.0]
    assert summe_liste(bestellwerte) == pytest.approx(125.49)


def test_summe_leere_liste():
    assert summe_liste([]) == 0


def test_summe_einzelner_wert():
    assert summe_liste([42.5]) == pytest.approx(42.5)


def test_summe_mit_ganzzahlen():
    bestellwerte = [10, 20, 30]
    assert summe_liste(bestellwerte) == pytest.approx(60)


def test_summe_mit_negativen_werten():
    bestellwerte = [50.0, -10.0, 5.0]
    assert summe_liste(bestellwerte) == pytest.approx(45.0)
