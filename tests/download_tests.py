import cs334demo.file_download.py

   with requests_mock.Mocker() as m:
        m.get(URL+api_key+'&rpp=1', text='resp')
        requests.get(URL+api_key+'&rpp=1')
        return "hello_world"