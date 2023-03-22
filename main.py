import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


star = list(map(int, input('введите кол-во звезд: ').split()))
response_to_comment = int(input("введите 1 - если нужер ответ продавца, 2 - если НЕ нужен ответ продавца: "))
search_star = {1: '— Жуть!', 2: '— Ниже среднего', 3: '— Средне', 4: '— Хорошо', 5: '— Отлично!'}
quantity_comments = int(input('Введите необходимое количество комментариев: '))
parameters = []
page = int(input('Введите количество страниц поиска: ')) + 1


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
            url = f'https://936.shop.onliner.by/reviews?has_reply=1&page={x}'
        else:
            url = f'https://936.shop.onliner.by/reviews?page={x}'
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


    if n < quantity_comments:
        print(f'Поиск завершен, найдено коментариев: {n-1}, для достижения необходимого количества комментариев ({quantity_comments}) необходимо увеличть количество страниц поиска.')
    elif n == quantity_comments:
        print(f'Поиск завершен, найдено коментариев: {n-1}')


def main():
    get_comments()


if __name__ == '__main__':
    main()



















# page = int(input('Введите количество страниц поиска: ')) + 1
# def get_comments():
#     if response_to_comment == 1:
#         parameters.append('с ответом продавца')
#
#     for i in star:
#         for j in search_star:
#             if i == j:
#                 parameters.append(search_star[i])
#
#
#
#     n = 1
#     for x in range(1,page):
#         url = f'https://936.shop.onliner.by/reviews?page={x}'
#         response = requests.get(url=url, headers=headers)
#         bs = BeautifulSoup(response.text, "lxml")
#         titles = bs.find_all("div", class_="catalog-form__reviews-unit")
#
#         for title in titles:
#             comment_star = title.find("span", class_="catalog-form__rating-count").text.strip()
#             for argument in parameters:
#                 if comment_star == argument:
#                     # answer_pr = title.find("div", class_="catalog-form__description catalog-form__description_primary catalog-form__description_base-additional catalog-form__description_font-weight_semibold catalog-form__description_condensed-default").text.strip()
#                     comment = title.find("div", class_="catalog-form__description catalog-form__description_primary catalog-form__description_base-alter catalog-form__description_condensed-default catalog-form__description_multiline").text.strip()
#                     # answer = title.find("div", class_="catalog-form__comment").text.strip()
#                     print(f"{n} - {comment_star} - {comment}")
#                     print("__________________________________________________________________")
#                     n += 1
#
# def main():
#     get_comments()