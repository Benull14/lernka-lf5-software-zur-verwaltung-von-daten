import pytest

from bibliothek import rabattsatz_ermitteln


def test_standard_niedriger_umsatz():
    assert rabattsatz_ermitteln(100.0, "Standard") == 0.0


def test_standard_mittlerer_umsatz():
    assert rabattsatz_ermitteln(500.0, "Standard") == 0.05


def test_standard_hoher_umsatz():
    assert rabattsatz_ermitteln(2000.0, "Standard") == 0.10


def test_standard_knapp_unter_grenze():
    assert rabattsatz_ermitteln(1999.99, "Standard") == 0.05


def test_premium_niedriger_umsatz():
    assert rabattsatz_ermitteln(100.0, "Premium") == 0.05


def test_premium_mittlerer_umsatz():
    assert rabattsatz_ermitteln(500.0, "Premium") == 0.10


def test_premium_hoher_umsatz():
    assert rabattsatz_ermitteln(2000.0, "Premium") == 0.15


def test_umsatz_null_standard():
    assert rabattsatz_ermitteln(0.0, "Standard") == 0.0


def test_umsatz_null_premium():
    assert rabattsatz_ermitteln(0.0, "Premium") == 0.05


def test_negativer_umsatz_wirft_fehler():
    with pytest.raises(ValueError):
        rabattsatz_ermitteln(-50.0, "Standard")


def test_unbekannte_kundengruppe_wirft_fehler():
    with pytest.raises(ValueError):
        rabattsatz_ermitteln(1000.0, "Gold")


def test_kundengruppe_gross_kleinschreibung_wird_ignoriert():
    assert rabattsatz_ermitteln(1000.0, "standard") == 0.05
    assert rabattsatz_ermitteln(1000.0, "PREMIUM") == 0.10
