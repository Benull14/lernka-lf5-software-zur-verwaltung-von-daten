import pytest
from bibliothek import durchschnitt


def test_durchschnitt_mehrere_werte():
    zahlen = [10, 20, 30, 40]
    assert durchschnitt(zahlen) == pytest.approx(25.0)


def test_durchschnitt_ein_wert():
    zahlen = [42]
    assert durchschnitt(zahlen) == pytest.approx(42.0)


def test_durchschnitt_mit_kommazahlen():
    zahlen = [5.5, 6.5, 8.0]
    assert durchschnitt(zahlen) == pytest.approx(6.666666666666667)


def test_durchschnitt_mit_null_bestellungen():
    zahlen = [0, 0, 0, 10]
    assert durchschnitt(zahlen) == pytest.approx(2.5)


def test_durchschnitt_leere_liste_wirft_fehler():
    with pytest.raises(ValueError):
        durchschnitt([])


def test_durchschnitt_realistisches_szenario():
    # Bestellzahlen einer Arbeitswoche im Lager
    bestellungen_pro_tag = [120, 135, 98, 150, 142]
    assert durchschnitt(bestellungen_pro_tag) == pytest.approx(129.0)
