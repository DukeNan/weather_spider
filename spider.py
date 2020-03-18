from settings import APP_CODE, ApiHost, Star
import requests


class Spider:
    app_code = APP_CODE
    headers = {
        'Authorization': f'APPCODE {app_code}'
    }

    def get_data(self, url, headers):
        return requests.get(url=url, headers=headers).json()

    def crawl_weather(self, city):
        host = ApiHost.Weather.value
        url = f'{host}/weather/query?city={city}'
        data = self.get_data(url=url, headers=self.headers)
        return data

    def crawl_constellation(self, constellation):
        host = ApiHost.StarLucky.value
        url = f'{host}/star?star={constellation}'
        data = self.get_data(url=url, headers=self.headers)
        return data


if __name__ == '__main__':
    from pprint import pprint
    s = Spider()
    data = s.crawl_constellation(Star.Juxie.value)
    pprint(data['showapi_res_body']['day'])
