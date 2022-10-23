import pygame
import sys
import game
import cities

def goal_test(path: list):
  current_node = path[-1]
  return current_node == goal

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

def breadth_first_search(frontier: list):

  if (len(frontier) == 0):
    return None

  current = frontier.pop(0)

  game.draw(visited=visited, path=current)

  if goal_test(current):
    return current

  off_spring = expand(current)

  for node in off_spring:
      frontier.append(node)

  return breadth_first_search(frontier)


city_start = 'Arad'
city_end = 'Bucharest'

start = cities.get_number_by_city(city_start)
goal = cities.get_number_by_city(city_end)
visited = [0] * len(cities.cities_list)

print('El programa inicia en ' + city_start + '(' + str(start) + ')')
print('Busca llegar a ' + city_end + '(' + str(goal) + ')')

graph = cities.get_resume_matrix()

frontier = [[start]]

path = breadth_first_search(frontier)

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