import arcade
import arcade.key

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
    
    def __init__(self, world, x, y):
        self.world = world
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        self.direction = Ship.DIR_DOWN
        self.angle = Ship.ANGLE[3]
 
    def switch_direction(self, direction):
        if (self.direction == Ship.DIR_LEFT and direction != Ship.DIR_RIGHT) or (self.direction == Ship.DIR_UP and direction != Ship.DIR_DOWN) or (self.direction == Ship.DIR_DOWN and direction != Ship.DIR_UP) or (self.direction == Ship.DIR_RIGHT and direction != Ship.DIR_LEFT):
            self.direction = direction
            self.angle = Ship.ANGLE[direction]
        
    def animate(self, delta):
        if self.direction == Ship.DIR_LEFT:
            if self.x > 5:
                self.x -= 5
        if self.direction == Ship.DIR_RIGHT:
            if self.x < self.world.width:
                self.x += 5
        if self.direction == Ship.DIR_UP:
            if self.y < self.world.height:
                self.y += 5
        if self.direction == Ship.DIR_DOWN:
            if self.y > 5:
                self.y -= 5
            
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.ship = Ship(self, 100, 700)
        self.gold = Gold(self, 300, 300)
        self.score = 0
  
    def animate(self, delta):
        self.ship.animate(delta)
        
        if self.ship.hit(self.gold, 20):
            self.gold.random_location()
            self.score += 1
        
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.switch_direction(0)
        if key == arcade.key.UP:
            self.ship.switch_direction(1)
        if key == arcade.key.RIGHT:
            self.ship.switch_direction(2)
        if key == arcade.key.DOWN:
            self.ship.switch_direction(3)
            
class Gold(Model):
    def __init__(self, world, x, y):
        self.world = world
        super().__init__(world, x, y, 0)
        self.x = x
        self.y = y
        
    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)