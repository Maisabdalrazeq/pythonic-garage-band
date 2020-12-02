
import pytest
from pythonic_garage_band.band import Band, Musician, Guitarist, Bassist, Drummer
from pythonic_garage_band import __version__



def test_version():
    assert __version__ == '0.1.0'



def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."

