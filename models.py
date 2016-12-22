import arcade
import arcade.key
import random

from random import randint


class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
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
        self.world = world
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        self.number = number
        self.direction = random.randrange(4)
        self.angle = Ship.ANGLE[self.direction]
 
    def switch_direction(self, direction):
        # if (self.direction == Ship.DIR_LEFT and direction != Ship.DIR_RIGHT) or (self.direction == Ship.DIR_UP and direction != Ship.DIR_DOWN) or (self.direction == Ship.DIR_DOWN and direction != Ship.DIR_UP) or (self.direction == Ship.DIR_RIGHT and direction != Ship.DIR_LEFT):
            self.direction = direction
            self.angle = Ship.ANGLE[direction]
        
    def animate(self, delta):
        if self.world.is_end_game(self):
            print('game end.')
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
            
class World:
    current_ship = 0
    count_ship = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.ship = [Ship(self, 700, 500, 0)]
        self.star = Star(self, 300, 300)
        self.score = 0
  
    def animate(self, delta):
        for ship in self.ship:
            ship.animate(delta)
            if ship.hit(self.star, 30):
                self.star.random_location()
                self.score += 1
                if self.count_ship < 4 and self.score % 5 == 0:
                    self.count_ship += 1
                    self.ship.append(Ship(self, random.randrange(int(self.width/3), int(self.width*2/3)), random.randrange(int(self.height/3), int(self.height*2/3)),self.count_ship))

        
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship[self.current_ship].switch_direction(0)
        if key == arcade.key.UP:
            self.ship[self.current_ship].switch_direction(1)
        if key == arcade.key.RIGHT:
            self.ship[self.current_ship].switch_direction(2)
        if key == arcade.key.DOWN:
            self.ship[self.current_ship].switch_direction(3)
        if key >= 49 and key <= 53:
            if self.count_ship >= key - 49:
                self.current_ship = key - 49
                
    def is_end_game(self, ship):
        if ship.y <= 5 or ship.y >= self.height-5 or ship.x <= 5 or ship.x >= self.width-5:
            return True
        for index, ship_loop in enumerate(self.ship):
            if ship.hit(ship_loop, 40) and index != ship.number:
                return True
                
class Star(Model):
    def __init__(self, world, x, y):
        self.world = world
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        
    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)