import pytest

from bibliothek import tarifzone_ermitteln


def test_nahzone_untere_grenze():
    assert tarifzone_ermitteln(0) == "Nahzone"


def test_nahzone_innerhalb():
    assert tarifzone_ermitteln(25.5) == "Nahzone"


def test_nahzone_obere_grenze():
    assert tarifzone_ermitteln(50) == "Nahzone"


def test_mittelzone_knapp_ueber_grenze():
    assert tarifzone_ermitteln(50.01) == "Mittelzone"


def test_mittelzone_innerhalb():
    assert tarifzone_ermitteln(120) == "Mittelzone"


def test_mittelzone_obere_grenze():
    assert tarifzone_ermitteln(200) == "Mittelzone"


def test_fernzone_knapp_ueber_grenze():
    assert tarifzone_ermitteln(200.01) == "Fernzone"


def test_fernzone_weit_entfernt():
    assert tarifzone_ermitteln(1500) == "Fernzone"


def test_negative_distanz_wirft_fehler():
    with pytest.raises(ValueError):
        tarifzone_ermitteln(-10)
