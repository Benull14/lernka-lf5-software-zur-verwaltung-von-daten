from login_sperre import ist_login_gesperrt


def test_keine_fehlversuche():
    assert ist_login_gesperrt(0) is False


def test_ein_fehlversuch():
    assert ist_login_gesperrt(1) is False


def test_zwei_fehlversuche():
    assert ist_login_gesperrt(2) is False


def test_genau_drei_fehlversuche_ist_gesperrt():
    assert ist_login_gesperrt(3) is True


def test_vier_fehlversuche():
    assert ist_login_gesperrt(4) is True


def test_viele_fehlversuche():
    assert ist_login_gesperrt(10) is True
