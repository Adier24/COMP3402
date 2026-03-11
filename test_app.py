from app_test import saludar

def test_saludar():
    assert saludar("Ana") == "Hola, Ana"