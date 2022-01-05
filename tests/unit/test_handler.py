import json

import pytest

from taxi_rate import app

def test_is_taxi_rate():
    assert app.is_taxi_rate(1500) == 610
    assert app.is_taxi_rate(2200) == 770 

