import os
from data_center import DataCenter


def find_cities_with_data_centers(dat_cent: list):
    """Находит города с дата-центрами и создает словарь,
       где ключ - номер города, значение - тип дата-центра"""
    dat_cent_dict = {}
    i = 0
    for center in dat_cent:
        i += 1
        if center in ["1", "2"]:
            dat_cent_dict[str(i)] = center
    return dat_cent_dict


def class_assign(dat_centr_dict: dict):
    """Создает классы городов с дата-центрами, используя словарь из функции
       find_cities_with_data_centers"""
    all_cities = []
    for key, value in dat_centr_dict.items():
        all_cities.append(DataCenter(key, value))
    return all_cities


def progon(n_of_pairs: str, dat_cent: list, all_connect: list):
    data_centers_dictionary = find_cities_with_data_centers(dat_cent)
    all_cities_dat_cntr = class_assign(data_centers_dictionary)

    for city in all_cities_dat_cntr:
        city.find_pairs(data_centers_dictionary)
        city.find_suitable_start(all_connect)
        city.find_quick_connection()

    n_of_pairs = int(n_of_pairs) - 1
    level = 1
    print(f"Уровень {level}")

    while n_of_pairs > 0:
        level += 1
        if os.path.isfile("OUTPUT.txt"):
            break
        for city in all_cities_dat_cntr:
            city.find_suitable_continue(all_connect)
            city.find_quick_connection()
        n_of_pairs -= 1
        print(f"Уровень {level}")
    else:
        with open("OUTPUT.txt", "w") as file:
            file.write("-1")
