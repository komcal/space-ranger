import arcade
import arcade.key
import random

from random import randint


class Model:
    def __init__(self, world, x, y, angle, number):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
        self.number = number
    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)
        
class Ship(Model):
    DIR_LEFT = 0
    DIR_UP = 1
    DIR_RIGHT = 2
    DIR_DOWN = 3
    ANGLE = [90, 0, -90, 180]
    SPEED = 3
    
    def __init__(self, world, x, y, number):
        super().__init__(world, x, y, 0, number)
        self.direction = random.randrange(4)
        self.angle = Ship.ANGLE[self.direction]
 
    def switch_direction(self, direction):
            self.direction = direction
            self.angle = Ship.ANGLE[direction]
        
    def animate(self, delta):
        if self.world.is_game_end(self):
            self.world.game_status = False
        else:
            if self.direction == Ship.DIR_LEFT:
                if self.x > Ship.SPEED:
                    self.x -= Ship.SPEED
            if self.direction == Ship.DIR_RIGHT:
                if self.x < self.world.width:
                    self.x += Ship.SPEED
            if self.direction == Ship.DIR_UP:
                if self.y < self.world.height:
                    self.y += Ship.SPEED
            if self.direction == Ship.DIR_DOWN:
                if self.y > Ship.SPEED:
                    self.y -= Ship.SPEED
            
class Star(Model):
    def __init__(self, world, x, y, number):
        super().__init__(world, x, y, 0, number)
        
    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)
        self.number = random.randrange(self.world.count_ship + 1)
