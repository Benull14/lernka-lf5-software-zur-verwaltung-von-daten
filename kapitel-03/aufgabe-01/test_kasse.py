"""Tests für die Funktion summe_liste aus dem Kassenmodul."""
import pytest
from kasse import summe_liste


def test_summe_mehrere_positive_zahlen():
    assert summe_liste([10.0, 5.50, 2.25]) == 17.75


def test_summe_einzelner_wert():
    assert summe_liste([9.99]) == 9.99


def test_summe_leere_liste():
    assert summe_liste([]) == 0.0


def test_summe_mit_ganzzahlen():
    assert summe_liste([1, 2, 3, 4]) == 10


def test_summe_mit_negativen_werten():
    assert summe_liste([20.0, -5.0, 3.5]) == 18.5


def test_summe_gibt_zahl_zurueck():
    ergebnis = summe_liste([1.5, 2.5])
    assert isinstance(ergebnis, (int, float))
