from models import *

class World:
    current_ship = 0
    count_ship = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.ship = [Ship(self, 700, 500, 0)]
        self.star = Star(self, 300, 300)
        self.score = 0
        self.game_status = True
  
    def animate(self, delta):
        if self.game_status:
            for ship in self.ship:
                ship.animate(delta)
                if ship.hit(self.star, 30):
                    self.star.random_location()
                    self.score += 1
                    if self.count_ship < 4 and self.score % 5 == 0:
                        self.generate_ship()

    def generate_ship(self):
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
                
    def is_game_end(self, ship):
        if ship.y <= 5 or ship.y >= self.height-5 or ship.x <= 5 or ship.x >= self.width-5:
            return True
        for index, ship_loop in enumerate(self.ship):
            if ship.hit(ship_loop, 40) and index != ship.number:
                return True
                