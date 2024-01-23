# import pytest

# @pytest.fixture

# def input_value():
#     input = 9
#     return input

# def test_divisible_by_3(input_value):
#     assert input_value % 3 == 0

# def test_divisible_by_6(input_value):
#     assert input_value % 6 == 0

import pytest
from api import fetch_data_from_api

def test_fetch_data_from_api(mock):
    api_url = "https://run.mocky.io/v3/a2fa8bc6-d43d-410f-97a7-7025ca8b792f"
    expected_data = {"key" :"value"}

    mock_get = mock.patch("requests.get")
    mock_get.return_value.json.return_value = expected_data

    result = fetch_data_from_api(api_url)

    assert result == expected_data
