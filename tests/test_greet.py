import pytest

from example import greet


def test_greet_saluda_al_nombre_recortado():
    assert greet("  Ana ") == "Hola, Ana!"


def test_greet_rechaza_un_nombre_vacio():
    with pytest.raises(ValueError):
        greet("   ")
