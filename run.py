from spider import Spider
from utils.send_email import SendMail
from utils.get_html import get_wether_html, get_star_html
from settings import SEND_LIST
from cached import get_star_lucky, get_weather, update_star_lucky, update_weather


class Send:

    def __init__(self):
        self.spider = Spider()
        self.mail = SendMail()

    def get_weather_data(self, city):
        data = get_weather(city)
        if data:
            return data
        data = self.spider.crawl_weather(city)['result']
        update_weather(city, data)
        return data

    def get_star_data(self, star):
        data = get_star_lucky(star)
        if data:
            return data
        data = self.spider.crawl_constellation(star)['showapi_res_body']['day']
        update_star_lucky(star, data)
        return data

    def get_html(self, weather_data, star, star_data):
        weather_html = get_wether_html(weather_data)
        star_html = get_star_html(star, star_data)
        return f"<html>{weather_html + star_html}</html>"

    def run(self):
        for item in SEND_LIST:
            weather_data = self.get_weather_data(item['city'])
            star = item['star']
            star_data = self.get_star_data(item['star_en'])
            html_str = self.get_html(weather_data=weather_data, star=star, star_data=star_data)
            self.mail.send_email('天气预报', [item['email']], html_str)



if __name__ == '__main__':
    send = Send()
    send.run()

