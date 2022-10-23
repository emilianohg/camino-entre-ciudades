import cities

distance_to_bucharest = {
  'Arad': 366,
  'Zerind': 374,
  'Sibiu': 253,
  'Timisoara': 329,
  'Oradea': 380,
  'Fagaras': 178,
  'Rimnicu Vilcea': 193,
  'Lugoj': 244,
  'Bucharest': 0,
  'Pitesti': 98,
  'Craiova': 160,
  'Mehadia': 241,
  'Giurgiu': 77,
  'Urziceni': 80,
  'Drobeta': 242,
  'Vaslui': 199,
  'Hirsova': 151,
  'Iasi': 226,
  'Eforie': 151,
  'Neamt': 234
}

cities_with_distances = {
  'Arad': [('Zerind',75), ('Sibiu',140), ('Timisoara',118)],
  'Zerind': [('Arad',75), ('Oradea',71)],
  'Sibiu': [('Arad',140),('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
  'Timisoara': [('Arad',118), ('Lugoj',111)],
  'Oradea': [('Zerind',71), ('Sibiu',151)],
  'Fagaras': [('Sibiu',99), ('Bucharest',211)],
  'Rimnicu Vilcea': [('Sibiu',80), ('Pitesti',97), ('Craiova',146)],
  'Lugoj': [('Timisoara',111), ('Mehadia',70)],
  'Bucharest': [('Fagaras',211), ('Pitesti',101), ('Giurgiu',90), ('Urziceni',85)],
  'Pitesti': [('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
  'Craiova': [('Rimnicu Vilcea',146), ('Pitesti',138), ('Drobeta',120)],
  'Mehadia': [('Lugoj',70), ('Drobeta',75)],
  'Giurgiu': [('Bucharest',90)],
  'Urziceni': [('Bucharest',85), ('Vaslui',142), ('Hirsova',98)],
  'Drobeta': [('Mehadia',75), ('Craiova',120)],
  'Vaslui': [('Urziceni',142), ('Iasi',92)],
  'Hirsova': [('Urziceni',98), ('Eforie',86)],
  'Iasi': [('Vaslui',92), ('Neamt',87)],
  'Eforie': [('Hirsova',86)],
  'Neamt': [('Iasi',87)]
}

def get_resume_matrix():
  total_cities = len(cities.cities_list)
  matrix = []
  for index, city_name in enumerate(cities.cities_list):
    matrix.append([])
    for city_connected in cities_with_distances[city_name]:
      matrix[index].append((cities.get_number_by_city(city_connected[0]), city_connected[1]))

  return matrix