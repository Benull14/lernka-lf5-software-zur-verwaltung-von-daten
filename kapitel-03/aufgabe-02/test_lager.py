import pytest
from lager import maximum


def test_maximum_mehrere_werte():
    assert maximum([12, 45, 3, 78, 22]) == 78


def test_maximum_negative_werte():
    assert maximum([-5, -12, -3, -40]) == -3


def test_maximum_ein_element():
    assert maximum([100]) == 100


def test_maximum_gleiche_werte():
    assert maximum([10, 10, 10]) == 10


def test_maximum_float_werte():
    assert maximum([5.5, 2.3, 9.9, 4.4]) == 9.9


def test_maximum_leere_liste_fehler():
    with pytest.raises(ValueError):
        maximum([])
