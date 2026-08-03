from bibliothek import zaehle_wenn


def test_keine_ueberschreitung():
    sensorwerte = [10.0, 15.5, 20.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 100)
    assert anzahl == 0


def test_alle_ueberschreiten():
    sensorwerte = [150.0, 200.0, 120.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 100)
    assert anzahl == 3


def test_teilweise_ueberschreitung():
    sensorwerte = [45.0, 78.0, 99.9, 100.1, 55.0, 120.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 100)
    assert anzahl == 2


def test_leere_liste():
    sensorwerte = []
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 100)
    assert anzahl == 0


def test_grenzwert_exakt_nicht_ueberschritten():
    sensorwerte = [100.0, 100.0, 100.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 100)
    assert anzahl == 0


def test_andere_bedingung_negative_werte():
    sensorwerte = [-5.0, 3.2, -1.0, 0.0, -10.5]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x < 0)
    assert anzahl == 3


def test_bedingung_gleichheit():
    sensorwerte = [0.0, 1.0, 0.0, 2.0, 0.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x == 0.0)
    assert anzahl == 3


def test_einzelner_wert_erfuellt():
    sensorwerte = [999.9]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 500)
    assert anzahl == 1


def test_einzelner_wert_erfuellt_nicht():
    sensorwerte = [10.0]
    anzahl = zaehle_wenn(sensorwerte, lambda x: x > 500)
    assert anzahl == 0
