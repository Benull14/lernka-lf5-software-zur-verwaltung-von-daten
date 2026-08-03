import pytest

from bibliothek import berechne_durchschnitt


def test_einfacher_durchschnitt_ohne_note_sechs():
    noten = [1.0, 2.0, 3.0, 4.0]
    ergebnis = berechne_durchschnitt(noten)
    assert ergebnis == pytest.approx(2.5)


def test_letzte_note_wird_beruecksichtigt():
    # Regression: die letzte Note in der Liste darf nicht ignoriert werden
    noten = [1.0, 1.0, 1.0, 6.0]
    ergebnis = berechne_durchschnitt(noten)
    # Note 6 zaehlt nur halb: (1 + 1 + 1 + 3) / 4 = 1.5
    assert ergebnis == pytest.approx(1.5)


def test_note_sechs_wird_nur_halb_gewichtet():
    noten = [6.0, 6.0, 2.0, 2.0]
    ergebnis = berechne_durchschnitt(noten)
    # (3 + 3 + 2 + 2) / 4 = 2.5
    assert ergebnis == pytest.approx(2.5)


def test_einzelne_note_ohne_sonderregel():
    noten = [4.0]
    ergebnis = berechne_durchschnitt(noten)
    assert ergebnis == pytest.approx(4.0)


def test_einzelne_note_sechs_mit_sonderregel():
    noten = [6.0]
    ergebnis = berechne_durchschnitt(noten)
    assert ergebnis == pytest.approx(3.0)


def test_summe_startet_korrekt_bei_null():
    # Regression: ein falscher Startwert der Summe wuerde das Ergebnis verfaelschen
    noten = [0.0, 0.0, 0.0, 0.0]
    ergebnis = berechne_durchschnitt(noten)
    assert ergebnis == pytest.approx(0.0)


def test_leere_liste_wirft_fehler():
    with pytest.raises(ValueError):
        berechne_durchschnitt([])


def test_gemischte_kommazahlen():
    noten = [2.5, 3.5, 1.0]
    ergebnis = berechne_durchschnitt(noten)
    assert ergebnis == pytest.approx((2.5 + 3.5 + 1.0) / 3)
