import math
import random

import pygame
import itertools

def getPathDistance(places : list):
    #Given a list of x,y coordinates return the distance it would take to go to each coordinate
    # in order and then back to the start.
    dist = 0
    return dist


def full_TSP(places : list):
    #Check the distance of all possible different paths one could take over a set of x,y coordiantes
    #and return the path with the shotest distance
    #Print out the number of distance calculations you had to do.

    bestRoute = []
    calculations = 0

    print(f"there were {calculations} calculations for full TSP")
    return bestRoute

def hueristic_TSP(places : list):
    #Perform a hueristic calculation for traveling salesman.
    #For each node find the closest node to it and assume it is next node then repeat until you have your path.
    #Return the path. andprint out the number of distance calculations you did.


    calculations = 0

    print(f"there were {calculations} calculations for hueristic TSP")
    return []

def generatePermutations(places : list):
    # a function that given a list will return all possible permutations of the list.
    return list(itertools.permutations(places))


def getDistance(spot1, spot2):
    #Given two coordinates in a plane return the distance between those two points.
    dist = math.sqrt((spot1[0] - spot2[0]) ** 2 + (spot2[1] - spot2[1]) ** 2)
    return dist


def generate_RandomCoordinates(n):
    #Creates a list of random coordinates
    newPlaces = []
    for i in range(n):
        newPlaces.append([random.randint(10,790),random.randint(10,590)])
    return newPlaces

places = [[80,75],[100,520],[530,300],[280,200],[350,150],[700,120],[400,500]]


def DrawExample(places):
    #Draws the TSP showcase to the screen.
    TSP = full_TSP(places.copy())
    Hueristic = hueristic_TSP(places.copy())
    # Initialize Pygame
    pygame.init()
    print(TSP)
    print(Hueristic)
    # Set up the game window
    screen = pygame.display.set_mode((800, 800))
    # Game loop
    running = True
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render('Hello, Pygame!', True, (0, 0, 0))
    text_surface.set_colorkey((0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.center = (300, 700)  # Center the text on the screen
    # Arguments: text string, antialias boolean (True for smooth edges), text color, optional background color
    text_surface = font.render('Hello, Pygame!', True, (255, 255, 255))  # White text
    while running:
        screen.fill((255,255,255))
        for i in range(len(TSP)-1):
            pygame.draw.line(screen,(255,0,0),(TSP[i][0],TSP[i][1]),(TSP[i+1][0],TSP[i+1][1]),width = 8)
        if len(TSP) >=1:pygame.draw.line(screen, (255, 0, 0), (TSP[0][0], TSP[0][1]), (TSP[-1][0], TSP[-1][1]),width =8)
        for i in range(len(Hueristic) - 1):
            pygame.draw.line(screen, (0, 0, 255), (Hueristic[i][0], Hueristic[i][1]), (Hueristic[i + 1][0], Hueristic[i + 1][1]), width=4)
        if len(Hueristic) >=1:pygame.draw.line(screen, (0, 0, 255), (Hueristic[0][0], Hueristic[0][1]), (Hueristic[-1][0], Hueristic[-1][1]), width=4)
        for spot in places:
            pygame.draw.circle(screen, (0,0,0),(spot[0],spot[1]), 10)
        text_surface = font.render('Red is full TSP Blue is Heuristic', True, (0, 0, 0))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    # Quit Pygame

DrawExample(places)
#DrawExample(generate_RandomCoordinates(5))# DO NOT run more than 9 or 10
pygame.quit()
