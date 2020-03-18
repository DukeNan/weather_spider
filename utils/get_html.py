def get_wether_html(result: dict):
    # 生活指数
    html_string = \
        f"<h4>今日{result['city']}天气（{result['date']} {result['week']}）</h4>" \
        f"<ul>" \
        f"<li>天气: {result['weather']}</li>" \
        f"<li>最高气温：{result['temphigh']}℃</li>" \
        f"<li>最低气温：{result['templow']}℃</li>" \
        f"<li>风力：{result['windpower']}</li>" \
        f"<li>风向：{result['winddirect']}</li>" \
        f"<li>风速：{result['windspeed']}m/s</li>" \
        f"</ul>"
    return html_string


def get_star_html(star, data):
    star_html = \
        f"<h4>今日{star}运势</h4>" \
        f"<ul>" \
        f"<li>财富指数: {data['money_star']}</li>" \
        f"<li>工作指数: {data['work_star']}</li>" \
        f"<li>爱情指数: {data['love_star']}</li>" \
        f"<li>财富指数: {data['money_star']}</li>" \
        f"<li>综合指数: {data['summary_star']}</li>" \
        f"<li>幸运色: {data['lucky_color']}</li>" \
        f"<li>贵人星座: {data['grxz']}</li>" \
        f"<li>吉利方位: {data['lucky_direction']}</li>" \
        f"<li>吉时: {data['lucky_time']}</li>" \
        f"<li>幸运数字: {data['lucky_num']}</li>" \
        f"<li>今日提醒: {data['day_notice']}</li>" \
        f"</ul>" \
        f"{data['love_txt']}</br>" \
        f"{data['work_txt']}</br>"
    return star_html