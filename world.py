from models import *

class World:
    current_ship = 0
    count_ship = 0
    BTN_ONE = 49
    BTN_FIVE = 53
    score_check = [1, 5, 15, 30, 40]
    
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.ship = [Ship(self, 700, 500, 0)]
        self.star = Star(self, 400, 400, 0)
        self.score = 0
        self.game_status = True
  
    def animate(self, delta):
        if self.game_status:
            for ship in self.ship:
                ship.animate(delta)
                if ship.hit(self.star, 30) and ship.number == self.star.number:
                    self.score += 1
                    if self.count_ship < 4 and self.score == self.score_check[self.count_ship]:
                        self.generate_ship()
                    self.star.random_location()

    def generate_ship(self):
        self.count_ship += 1
        self.ship.append(Ship(self, random.randrange(int(self.width/3), int(self.width*2/3)), random.randrange(int(self.height/3), int(self.height*2/3)),self.count_ship))
        
    def on_key_press(self, key, key_modifiers):
        if self.BTN_ONE <= key <= self.BTN_FIVE:
            if self.count_ship >= key - self.BTN_ONE:
                self.current_ship = key - self.BTN_ONE
        elif arcade.key.LEFT <= key <= arcade.key.DOWN:
            self.ship[self.current_ship].switch_direction(key - arcade.key.LEFT)
                
    def is_game_end(self, ship):
        if ship.y <= 5 or ship.y >= self.height-5 or ship.x <= 5 or ship.x >= self.width-5:
            return True
        for index, ship_loop in enumerate(self.ship):
            if ship.hit(ship_loop, 40) and index != ship.number:
                return True
                