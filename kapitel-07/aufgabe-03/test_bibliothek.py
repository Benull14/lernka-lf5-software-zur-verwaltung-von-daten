import pytest

from bibliothek import zaehle_versuche


def test_erfolg_beim_dritten_versuch():
    verbindungsversuche = [False, False, True]
    assert zaehle_versuche(verbindungsversuche) == 3


def test_erfolg_beim_ersten_versuch():
    verbindungsversuche = [True]
    assert zaehle_versuche(verbindungsversuche) == 1


def test_erfolg_nach_mehreren_fehlschlaegen():
    verbindungsversuche = [False, False, False, False, True]
    assert zaehle_versuche(verbindungsversuche) == 5


def test_weitere_versuche_nach_erfolg_werden_ignoriert():
    verbindungsversuche = [False, True, False, True]
    assert zaehle_versuche(verbindungsversuche) == 2


def test_keine_erfolgreiche_verbindung_wirft_fehler():
    verbindungsversuche = [False, False, False]
    with pytest.raises(ValueError):
        zaehle_versuche(verbindungsversuche)


def test_leere_liste_wirft_fehler():
    verbindungsversuche = []
    with pytest.raises(ValueError):
        zaehle_versuche(verbindungsversuche)
