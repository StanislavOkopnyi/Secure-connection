class DataCenter:
    """Класс города с дата центром"""
    def __init__(self, num_city: str, type_dat_centr: str):
        self.num_city = num_city
        self.type_dat_centr = type_dat_centr
        self.pairs = []
        self.ways = []

    def find_pairs(self, dict_dat_centr: dict): #работает
        """Находит к одному городу все возможные пары, используя словарь,
           где ключ номер города, значение тип дата-центра"""
        for key, value in dict_dat_centr.items():
            if not self.num_city == key and not self.type_dat_centr == value:
                self.pairs.append(key)
        pass

    def find_suitable_start(self, all_connect: list):
        """Находит соединения с которых можно начать
           Использует номер города, из которого будет соединение проводится и
           список из всех возможных соединений"""
        for connect in all_connect:
            if self.num_city == connect[0]:
                self.ways.append([connect, ])
            elif self.num_city == connect[1]:
                self.ways.append([[connect[1], connect[0], connect[2]], ])

    def find_suitable_continue(self, all_connect: list):
        """Продолжает поиск возможных путей, используется после функции find_suitable_start
           Отсекает варианты путей, которые были уже пройдены
           Принимает список с возможными соединениями"""
        suitable_connections = []

        for way in self.ways:
            last_connection = way[-1]
            last_city = last_connection[1]

            for part_of_way in way:
                try:
                    all_connect.remove(part_of_way)
                    all_connect.remove([[part_of_way[1],part_of_way[0], part_of_way[2]]])
                except ValueError:
                    pass

            for connect in all_connect:
                if last_city == connect[0]:
                    new_way = way + [connect]
                    suitable_connections.append(new_way)
                elif last_city == connect[1]:
                    new_way = way + [[connect[1], connect[0], connect[2]]]
                    suitable_connections.append(new_way)

        self.ways = suitable_connections

    def find_quick_connection(self):
        """Выясняет имеются ли соединения между последним городом в цепочке
           и городом с подходящим дата-центром"""
        def save_answer(way):
            """Выводит ответ в файл OUTPUT.txt
                На второй строчке путь"""
            first_city = self.num_city
            right_way = way
            last_connection = right_way[-1]
            last_city = last_connection[1]
            price = 0
            for connection in way:
                price += int(connection[2])
            with open("OUTPUT.txt", "w") as file:
                file.write(f"{first_city} {last_city} {price}"
                           + f"\n{way}")

        for pair in self.pairs:
            for way in self.ways:
                last_way = way[-1]
                if pair == last_way[1]:
                    save_answer(way)
    pass
