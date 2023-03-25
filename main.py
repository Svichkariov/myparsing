import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


number = int(input("Введите номер магазина: "))
quantity_comments = int(input('Введите необходимое количество комментариев: '))
page = int(input('Введите количество страниц поиска: ')) + 1
star = list(map(int, input('введите кол-во звезд: ').split()))
response_to_comment = int(input("введите 1 - если нужер ответ продавца, 2 - если НЕ нужен ответ продавца: "))
search_star = {1: '— Жуть!', 2: '— Ниже среднего', 3: '— Средне', 4: '— Хорошо', 5: '— Отлично!'}
parameters = []
store_name = {
    1: 'https://936.shop.onliner.by/reviews',
    2: 'https://707.shop.onliner.by/reviews',
    3: 'https://197.shop.onliner.by/reviews',
    4: 'https://585.shop.onliner.by/reviews',
    5: 'https://3886.shop.onliner.by/reviews'
}



def information_about_the_store():
    url = f'{store_name[number]}'
    response = requests.get(url=url, headers=headers)
    bs = BeautifulSoup(response.text, "lxml")
    store = bs.find("h1", class_="catalog-form__title catalog-form__title_base catalog-form__title_nocondensed catalog-form__title_condensed-additional").text.strip()
    rating = bs.find("div", class_="catalog-grade__digit").text.strip()
    total_reviews = bs.find("div", class_="catalog-form__description catalog-form__description_other catalog-form__description_base").text.strip()
    print(f"{store}")
    print( f'{store_name[number]}')
    print(f"Рейтинг по отзывам за последний год: {rating}")
    print(f"{total_reviews}")



def get_comments():
    if response_to_comment == 1:
        parameters.append('с ответом продавца')

    for i in star:
        for j in search_star:
            if i == j:
                parameters.append(search_star[i])


    n = 1
    for x in range(1,page):
        if parameters[0] == 'с ответом продавца':
            url = f'{store_name[number]}?has_reply=1&page={x}'
        else:
            url = f'{store_name[number]}?page={x}'
        response = requests.get(url=url, headers=headers)
        bs = BeautifulSoup(response.text, "lxml")
        titles = bs.find_all("div", class_="catalog-form__reviews-unit")



        for title in titles:
            comment_star = title.find("span", class_="catalog-form__rating-count").text.strip()
            for argument in parameters:
                if comment_star == argument and n <= quantity_comments:
                    comment = title.find("div", class_="catalog-form__description catalog-form__description_primary catalog-form__description_base-alter catalog-form__description_condensed-default catalog-form__description_multiline").text.strip()
                    print(f"{n} - {comment_star} - {comment}")
                    if parameters[0] == 'с ответом продавца':
                        answer_seller = title.find("div", class_="catalog-form__comment").text.strip()
                        print(f"{answer_seller}")
                    print("__________________________________________________________________")
                    n += 1
        if n-1 == quantity_comments:
            break


    if n < quantity_comments:
        print(f'Поиск завершен, найдено коментариев: {n-1}, для достижения необходимого количества комментариев ({quantity_comments}) необходимо изменить параметры поиска.')
    elif n-1 == quantity_comments:
        print(f'Поиск завершен, найдено коментариев: {n-1}')


def main():
    information_about_the_store()
    get_comments()


if __name__ == '__main__':
    main()

