import requests 
import requests_mock

def download_file(URL, api_key):
   
    data = requests.get(url=URL+api_key+'&rpp=1')
    document = data.json()
    print(document)


def main():
    result = download_file('https://api.data.gov:443/regulations/v3/documents.json?', 'api_key=4gjeexkg1ALM85CaC2c51Y9D7ieo2BdOLIKQY2mS')
    print(result)

if __name__ == "__main__":
    main()