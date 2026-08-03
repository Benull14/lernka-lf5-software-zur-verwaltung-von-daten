from bibliothek import ist_primzahl


def test_zwei_ist_primzahl():
    assert ist_primzahl(2) is True


def test_drei_ist_primzahl():
    assert ist_primzahl(3) is True


def test_vier_ist_keine_primzahl():
    assert ist_primzahl(4) is False


def test_eins_ist_keine_primzahl():
    assert ist_primzahl(1) is False


def test_null_ist_keine_primzahl():
    assert ist_primzahl(0) is False


def test_negative_zahl_ist_keine_primzahl():
    assert ist_primzahl(-7) is False


def test_siebzehn_ist_primzahl():
    assert ist_primzahl(17) is True


def test_neun_ist_keine_primzahl():
    assert ist_primzahl(9) is False


def test_artikelnummer_grosse_primzahl():
    assert ist_primzahl(7919) is True


def test_artikelnummer_grosse_nicht_primzahl():
    assert ist_primzahl(8000) is False


def test_hundert_ist_keine_primzahl():
    assert ist_primzahl(100) is False


def test_zweiundneunzig_ist_keine_primzahl():
    assert ist_primzahl(91) is False
