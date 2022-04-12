def anime(request):
    import requests
    import re

    from bs4 import BeautifulSoup


    # Аниме которое будет парситься
    list_anime = [
            'Мир отомэ-игр — это тяжёлый мир для мобов',
            'Госпожа Кагуя: в любви как на войне',
            'Рыцарь-скелет вступает в параллельный мир',
            'Мемуары Ванитаса',
            'Восхождение героя щита 2 сезон',
            'Дэаймон',
            'Игра друзей',
            'Бёрди винг: История гольфисток',
            'Перестану быть героем',
            'Тусовщик Кунмин',
            'Клан девяти',
            'Непостижимая Ахарэн',
            'Величайший Повелитель Демонов перерождается как типичное ничтожество'
    ]
    urls_site_naruto = 'https://naruto-base.su/novosti/drugoe_anime_ru'
    url_naruto_base = 'https://naruto-base.su/'
    # Количество страниц, которое будет просматривать код
    pages = 13

    puk = {}
    def data_scrapping(link, *args, **params):
        # Функция возвращающая данные из заданной страницы с заданными параметрами
        data = requests.get(link)
        data_insert = data.text
        borsch = BeautifulSoup(data_insert, 'lxml')
        element_borsch = borsch.findAll(args, params)
        return element_borsch

    # Функция возвращающая ссылку на последнюю серию аниме по названию в заголовке файла, заданному в параметрах
    def data_last_element_anime(id=None):
        for i in range(pages):
            anime_ID = [link['href'] for link in (data_scrapping(urls_site_naruto + "?page" + str(i + 1), 'a')) if
                        id in link.get_text()]
            if len(anime_ID) == 0:
                pass
            else:
                link_anime = url_naruto_base + anime_ID[0]
                # Поиск ссылки на последний эпизод аниме с сабами и без на портале Sibnet
                #last_episode_sub = data_scrapping(link_anime, 'a', id='ep6')
                last_episode = data_scrapping(link_anime, 'a', id="ep14")
                #result_sub = re.search(r'\d{7}', str(last_episode_sub))[0]
                result_dub = re.search(r'\d{7}', str(last_episode))[0]
                link_name_and_element_anime = data_scrapping(link_anime, 'h1')[0].text
                #link_result_sub = 'https://video.sibnet.ru/shell.php?videoid=' + result_sub
                link_result_dub = 'https://video.sibnet.ru/shell.php?videoid=' + result_dub
                puk[link_name_and_element_anime] = link_result_dub
                break

    def last_series_anime():
        for anime in list_anime:
            data_last_element_anime(id=anime)
        return puk
    city_info = {
                 'puk': last_series_anime,
                 }

    context = {
        'info': city_info,
    }


    return render(request, 'pyss/anime.html', context)


