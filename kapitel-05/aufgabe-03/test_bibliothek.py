import pytest

from bibliothek import wert_pruefen


def test_wert_innerhalb_bereich():
    assert wert_pruefen(5.0, 0.0, 10.0) is True


def test_wert_gleich_minimum():
    assert wert_pruefen(0.0, 0.0, 10.0) is True


def test_wert_gleich_maximum():
    assert wert_pruefen(10.0, 0.0, 10.0) is True


def test_wert_unterhalb_minimum():
    assert wert_pruefen(-1.0, 0.0, 10.0) is False


def test_wert_oberhalb_maximum():
    assert wert_pruefen(10.1, 0.0, 10.0) is False


def test_negativer_bereich():
    assert wert_pruefen(-5.0, -10.0, -1.0) is True


def test_negativer_bereich_ausserhalb():
    assert wert_pruefen(-15.0, -10.0, -1.0) is False


def test_messwert_qs_temperatur_ok():
    # Praxisbeispiel: Temperaturmessung im Produktionsprozess
    assert wert_pruefen(21.5, 18.0, 25.0) is True


def test_messwert_qs_temperatur_zu_hoch():
    assert wert_pruefen(30.0, 18.0, 25.0) is False


def test_messwert_qs_druck_zu_niedrig():
    assert wert_pruefen(0.5, 1.0, 5.0) is False
