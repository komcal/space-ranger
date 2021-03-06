import arcade
import arcade.key
from models import Ship
from world import World
 
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
            self.angle = self.model.angle

    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    draw = []
    def __init__(self, width, height):
        super().__init__(width, height) 
        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(width, height)

 
    def on_draw(self):
        self.add_ship_sprite()
        self.star_sprite = ModelSprite('images/star-'+str(self.world.star.number)+'.png',model=self.world.star)
        arcade.start_render()
        self.star_sprite.draw()
        for ship in SpaceGameWindow.draw:
            ship.draw()
        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20)
        arcade.draw_text(str('CURRENT SHIP: ' + str(self.world.current_ship+1)),
                         50, self.height - 30,
                         arcade.color.WHITE, 20)
        if self.world.game_status == False:
            arcade.draw_text(str('Game Over'),
                             self.width/2 - 250, self.height/2,
                             arcade.color.WHITE, 70)
            
     
    def animate(self, delta):
        self.world.animate(delta)
         
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    
    def add_ship_sprite(self):
        for index, ship in enumerate(self.world.ship):
            if index >= len(SpaceGameWindow.draw):
                self.ship_sprite = ModelSprite('images/spaceship-'+str(index)+'.png',model=ship)
                SpaceGameWindow.draw.append(self.ship_sprite)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()