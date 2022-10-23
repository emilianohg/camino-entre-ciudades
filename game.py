import pygame

import cities

pygame.init()
pygame.display.set_caption('Ciudades de Rumania')

size = [886, 540]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.image.load('images/ciudades.png')
font = pygame.font.Font('fonts/roboto/Roboto-Medium.ttf', 18)

width_city = 18

COLOR_GRAY = (100, 100, 100)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (100, 255, 100)
COLOR_RED = (255, 100, 100)

def draw_city(city, color):
    pygame.draw.rect(screen, (color[0]-50, color[1]-50, color[2]-50), city.get_rect())
    pygame.draw.rect(screen, color, city.get_inner_rect())


def draw_text(text, x, y):
    text = font.render(text, True, COLOR_BLACK)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    screen.blit(text, textRect)

def draw(**kwargs):
    screen.fill([255, 255, 255])
    #screen.blit(background, [0, 0])

    pygame.draw.rect(screen, COLOR_RED, (300, 50, 18, 18))
    draw_text('Ciudad visitada', 330, 48)

    pygame.draw.rect(screen, COLOR_GREEN, (300, 80, 18, 18))
    draw_text('Camino actual', 330, 78)

    for connection in cities.get_connections():
        pygame.draw.line(
            screen,
            COLOR_GRAY,
            [connection.start[0], connection.start[1]],
            [connection.end[0], connection.end[1]],
            3
        )

    for city in cities.get_coordinates():
        pygame.draw.rect(screen, COLOR_BLACK, city.get_rect())
        pygame.draw.rect(screen, COLOR_GRAY, city.get_inner_rect())
        draw_text(city.name, city.text_position[0], city.text_position[1])

    visited = []
    current_path = []
    for key, value in kwargs.items():
        if key == 'visited':
            for position, i in enumerate(value):
                if i == 1:
                    visited.append(
                        cities.coordinates[cities.cities_list[position]]
                    )
        if key == 'path':
            for position in value:
                current_path.append(
                    cities.coordinates[cities.cities_list[position]]
                )

    for pos, city in enumerate(current_path):
        if (pos == 0):
            continue

        before_city = current_path[pos - 1]

        pygame.draw.line(
            screen,
            COLOR_GREEN,
            [before_city.get_center()[0], before_city.get_center()[1]],
            [city.get_center()[0], city.get_center()[1]],
            3
        )

    for city_visited in visited:
        draw_city(city_visited, COLOR_RED)

    for city in current_path:
        draw_city(city, COLOR_GREEN)


    pygame.display.flip()
    pygame.time.wait(500)


