import pygame
import sys
import game
import cities
import cities_distance

def goal_test(path: list):
  current_node = path[-1]
  return current_node == goal

def evaluate(paths):
  min_city = None
  min_path = None
  for path in paths:
    next_city = path[-1]
    if min_city == None or distances[next_city] < distances[min_city]:
      min_city = next_city
      min_path = path
  return min_path

def expand(path: list):
    current_node = path[-1]

    visited[current_node] = 1

    childs = graph[current_node]

    paths = []

    for child in childs:
        if (visited[child] == 1):
            continue

        next_path = list(path)
        next_path.append(child)
        paths.append(next_path)

    return paths

def greedy_search(frontier: list):

    if (len(frontier) == 0):
        return None

    current = frontier.pop(0)

    game.draw(path=current, visited=visited)

    if goal_test(current):
        return current

    off_spring = expand(current)
    path = evaluate(off_spring)

    frontier.insert(0, path)

    return greedy_search(frontier)


city_start = 'Neamt'
city_end = 'Bucharest'

start = cities.get_number_by_city(city_start)
goal = cities.get_number_by_city(city_end)

visited = [0] * len(cities.cities_list)
distances = [i for i in cities_distance.distance_to_bucharest.values()]

print('El programa inicia en ' + city_start + '(' + str(start) + ')')
print('Busca llegar a ' + city_end + '(' + str(goal) + ')')

graph = cities.get_resume_matrix()

frontier = [[start]]
path = greedy_search(frontier)

if (path == None):
    print('No existe camino de ' + city_start + ' a ' + city_end)
else:
    print('Camino encontrado: ' + str(path))
    print('Camino encontrado: ' + str(cities.get_path_cities(path)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    game.draw(visited=visited, path=path)

pygame.quit()