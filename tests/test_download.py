from dotenv import load_dotenv, find_dotenv
from cs334demo import file_download
from cs334demo import customError
import os
import pytest
import requests_mock
import unittest

URL = "https://api.data.gov:443/regulations/v3/documents.json?"
load_dotenv(find_dotenv())
api_key = os.getenv("API_KEY")


class Tests(unittest.TestCase):
    def test_mock_response(self):
        with requests_mock.Mocker() as m:
            m.get(URL+api_key+'&rpp=1', json='hello world')
            response = file_download.download_file(URL, api_key)
            assert response == 'hello world'

    def test_no_api_key(self):
        with requests_mock.Mocker() as m:
            m.get(URL+''+'&rpp=1', exc=customError.IncorrectApiKey)
            with pytest.raises(customError.IncorrectApiKey):
                file_download.download_file(URL, "")

    def test_1000_calls(self):
        with requests_mock.Mocker() as m:
            m.get(URL+api_key+'&rpp=1', exc=customError.ThousandCalls)
            with pytest.raises(customError.ThousandCalls):
                file_download.download_file(URL, api_key)
