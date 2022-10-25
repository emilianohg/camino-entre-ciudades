import pygame
import sys
import game
import cities
import cities_distance

class Path:
  def __init__(self, value, distancia_recorrida):
    self.value = value
    self.distancia_recorrida = distancia_recorrida

  def __repr__(self):
    return " -- " + str(self.value) + ', '+ str(self.distancia_recorrida) + ' -- '

def goal_test(path: Path):
  current_city = path.value[-1][0]
  return current_city == goal

def distancia_recorrida(path):
    return sum(j for i, j in path)

def heuristica(child):
    return distances[child[0]]

def expand(path: Path):
    current_city = path.value[-1][0]
    path_list = path.value

    childs = graph[current_city]

    paths = []

    for child in childs:
        next_path = list(path_list)
        next_path.append(child)

        paths.append(
            Path(
                next_path,
                distancia_recorrida(next_path) + heuristica(child)
            )
        )

    return paths

def a_star_search(frontier: list):

  if (len(frontier) == 0):
    return None

  current = frontier.pop(0)

  game.draw(path=[i for i, j in current.value])

  if goal_test(current):
    return current

  off_spring = expand(current)

  for node in off_spring:
      frontier.insert(0, node)

  frontier.sort(key=lambda x:x.distancia_recorrida)

  return a_star_search(frontier)

city_start = 'Arad'
city_end = 'Bucharest'

start = cities.get_number_by_city(city_start)
goal = cities.get_number_by_city(city_end)

distances = [i for i in cities_distance.distance_to_bucharest.values()]

print('El programa inicia en ' + city_start + '(' + str(start) + ')')
print('Busca llegar a ' + city_end + '(' + str(goal) + ')')

graph = cities_distance.get_resume_matrix()

frontier = [ Path([(start, 0)], cities_distance.distance_to_bucharest[city_start]) ]

path = a_star_search(frontier)
path_finded = [i for i, j in path.value]

if (path == None):
    print('No existe camino de ' + city_start + ' a ' + city_end)
else:
    print('Camino encontrado: ' + str(path_finded))
    print('Camino encontrado: ' + str(cities.get_path_cities(path_finded)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    game.draw(path=path_finded)

pygame.quit()