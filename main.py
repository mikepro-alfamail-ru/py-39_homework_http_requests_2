from ya_token import ya_token
import requests
import json
import os

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_name = os.path.split(file_path)[-1]
        self.apiurl = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path=/netology_hmwrk'

    def get_upload_url(self):
        auth = {
            'Authorization': f'OAuth {ya_token}'
        }
        response = requests.get(f'{self.apiurl}/{self.file_name}&overwrite=true', headers=auth)
        # print(response.text)
        return json.loads(response.text).get('href')

    def upload(self):
        upload_url = self.get_upload_url()
        if upload_url:
            with open(self.file_path, 'rb') as file:
                response = requests.put(upload_url, data=file)
            return response.status_code
        else:
            return 'Ошибка'

if __name__ == '__main__':
    uploader = YaUploader('e:\\my_folder\\file.txt')
    result = uploader.upload()
    if result == 201:
        print(f'Сервер ответил - {result}, значит все ок')
    else:
        print(result)
