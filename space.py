import arcade
import arcade.key

from models import World, Ship
 
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
        self.add_ship_sprite()
            
        self.star_sprite = ModelSprite('images/star.png',model=self.world.star)

 
    def on_draw(self):
        self.add_ship_sprite()
        arcade.start_render()
        self.star_sprite.draw()
        self.ship_sprite.draw()
        for ship in SpaceGameWindow.draw:
            ship.draw()
        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20)
     
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