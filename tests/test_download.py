from dotenv import load_dotenv, find_dotenv
import os;
from cs334demo import file_download
import requests_mock
URL = "https://api.data.gov:443/regulations/v3/documents.json?"
load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")


def test_mock_response():
    with requests_mock.Mocker() as m:
        m.get(URL+api_key+'&rpp=1', json='hello world')
        response = file_download.download_file(URL, api_key)
        assert response == 'hello world'
