from bibliothek import liste_umkehren


def test_mehrere_paketnummern():
    eingabe = ["P1001", "P1002", "P1003", "P1004"]
    erwartet = ["P1004", "P1003", "P1002", "P1001"]
    assert liste_umkehren(eingabe) == erwartet


def test_leere_liste():
    assert liste_umkehren([]) == []


def test_einzelnes_element():
    assert liste_umkehren(["P2000"]) == ["P2000"]


def test_zwei_elemente():
    assert liste_umkehren(["A", "B"]) == ["B", "A"]


def test_originalliste_bleibt_unveraendert():
    original = ["P1", "P2", "P3"]
    kopie_original = original.copy()
    liste_umkehren(original)
    assert original == kopie_original


def test_zahlen_in_liste():
    eingabe = [10, 20, 30, 40, 50]
    erwartet = [50, 40, 30, 20, 10]
    assert liste_umkehren(eingabe) == erwartet


def test_gibt_neue_liste_zurueck():
    original = ["P1", "P2", "P3"]
    ergebnis = liste_umkehren(original)
    assert ergebnis is not original
