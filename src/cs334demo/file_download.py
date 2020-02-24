import requests
from dotenv import load_dotenv, find_dotenv
import os;


def download_file(URL, api_key):
    data = requests.get(url=URL+api_key+'&rpp=1')
    document = data.json()
    print(document)
    return document


def main():
    load_dotenv(find_dotenv())
    api_key = os.getenv("API_KEY")

    result = download_file('https://api.data.gov:443/regulations/v3/documents.json?', 'api_key=' + api_key)
    print(result)


if __name__ == "__main__":
    main()
