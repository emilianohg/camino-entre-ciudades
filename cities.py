class Connection:
    def __init__(self, start: (int, int), end: (int, int)):
        self.start = start
        self.end = end

class City:
    def __init__(self, name, position: (int, int), text_position: (int, int)):
        self.name = name
        self.position = position
        self.text_position = text_position
        self.border_size = 3
        self.width = 18

    def get_center(self):
        return (self.position[0] + self.width / 2, self.position[1] + self.width / 2)

    def get_rect(self):
        return (self.position[0], self.position[1], self.width, self.width)

    def get_inner_rect(self):
        return (
            self.position[0] + self.border_size,
            self.position[1] + self.border_size,
            self.width - self.border_size * 2,
            self.width - self.border_size * 2
        )

coordinates = {
    'Arad': City('Arad', (56, 146), (10, 144)),
    'Zerind': City('Zerind', (86, 80), (108, 92)),
    'Sibiu': City('Sibiu', (248, 204), (266, 186)),
    'Timisoara': City('Timisoara', (60, 280), (80, 274)),
    'Oradea': City('Oradea', (122, 16), (144, 12)),
    'Fagaras': City('Fagaras', (412, 216), (398, 192)),
    'Rimnicu Vilcea': City('Rimnicu Vilcea', (290, 280), (310, 264)),
    'Lugoj': City('Lugoj', (180, 332), (202, 332)),
    'Bucharest': City('Bucharest', (568, 420), (576, 444)),
    'Pitesti': City('Pitesti', (436, 352), (420, 328)),
    'Craiova': City('Craiova', (324, 484), (300, 506)),
    'Mehadia': City('Mehadia', (186, 400), (208, 396)),
    'Giurgiu': City('Giurgiu', (524, 512), (548, 512)),
    'Urziceni': City('Urziceni', (662, 380), (662, 402)),
    'Drobeta': City('Drobeta', (178, 466), (108, 464)),
    'Vaslui': City('Vaslui', (746, 220), (768, 228)),
    'Hirsova': City('Hirsova', (786, 380), (810, 382)),
    'Iasi': City('Iasi', (688, 120), (714, 126)),
    'Eforie': City('Eforie', (834, 474), (820, 500)),
    'Neamt': City('Neamt', (576, 70), (556, 48)),
}

neighboring_cities = {
  'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
  'Zerind': ['Arad', 'Oradea'],
  'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
  'Timisoara': ['Arad', 'Lugoj'],
  'Oradea': ['Zerind', 'Sibiu'],
  'Fagaras': ['Sibiu', 'Bucharest'],
  'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
  'Lugoj': ['Timisoara', 'Mehadia'],
  'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
  'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
  'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Drobeta'],
  'Mehadia': ['Lugoj', 'Drobeta'],
  'Giurgiu': ['Bucharest'],
  'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
  'Drobeta': ['Mehadia', 'Craiova'],
  'Vaslui': ['Urziceni', 'Iasi'],
  'Hirsova': ['Urziceni', 'Eforie'],
  'Iasi': ['Vaslui', 'Neamt'],
  'Eforie': ['Hirsova'],
  'Neamt': ['Iasi']
}

def get_coordinates():
    return [i for i in coordinates.values()]

def get_connections():
    connections = []
    for start_city in coordinates.keys():
        for end_city in neighboring_cities[start_city]:
            connections.append(
                Connection(coordinates[start_city].get_center(), coordinates[end_city].get_center())
            )
    return connections

cities_list = list(dict.keys(neighboring_cities))

def get_number_by_city(name: str) -> int:
  return cities_list.index(name)

def get_path_cities(path):
  return list(map(lambda pos: cities_list[pos], path))

def get_resume_matrix():
  total_cities = len(cities_list)
  matrix = []
  for index, city_name in enumerate(cities_list):
    matrix.append([])
    for city_connected in neighboring_cities[city_name]:
      matrix[index].append(get_number_by_city(city_connected))

  return matrix
