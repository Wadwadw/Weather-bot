import requests as re
import bs4


def parce(city='павлоград'):
    URL = 'https://sinoptik.ua/погода-' + city
    page = re.get(URL)
    wth = bs4.BeautifulSoup(page.text, "html.parser")

    description = [div['title'] for div in wth.find_all('div', title=True)]
    result = [f'Погода в городе {city} на 7 дней\n']
    n=-1
    for i in range(1,8):
        n+=1
        try:
            min = wth.select("div > .temperature > .min > span")
            min_text = min[n].getText()
            max = wth.select("div > .temperature > .max > span")
            max_text = max[n].getText()
            day_1 = wth.select(".day-link")
            day_1_text = day_1[n].getText()
            day_of_month_1 = wth.select("div > .date")
            day_of_month_1_text = day_of_month_1[n].getText()
            month = wth.select("div > .month")
            month_text = month[n].getText()
            desc = description[n]
            result.append(str(day_1_text + ' ' + day_of_month_1_text + ' ' + month_text + ': температура от '
                              + min_text + ' до ' + max_text + '. ' + desc + '.' + '\n'))
        except IndexError:
            result = ['Вы ввели город не правильно попробуйте ещё раз']

    return result


