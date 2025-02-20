import pytest
from main import get_cat_image

def test_get_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'url': 'https://api.thecatapi.com/v1/images/abcdef123456.jpg'
    }
    image_data = get_cat_image()
    assert image_data == {'url': 'https://api.thecatapi.com/v1/images/abcdef123456.jpg'}

def test_get_cat_image_unsuccess(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    image_data = get_cat_image()
    assert image_data == None