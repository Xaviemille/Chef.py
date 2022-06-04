import arcade


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.center_window()

# Cook animation
        self.cook = arcade.AnimatedTimeBasedSprite("images/cook.png", image_x=0, image_y=0,
                                                  image_width=1063, image_height=1456)

        # loading the frames individually
        # frame 1
        texture = arcade.load_texture("images/cook.png", x=0, y=0, width=1063, height=1456)
        self.cook.frames.append(arcade.AnimationKeyframe(tile_id=0, duration=50, texture=texture))

        # frame 2
        texture = arcade.load_texture("images/cook.png", x=1063, y=0, width=1063, height=1456)
        self.cook.frames.append(arcade.AnimationKeyframe(tile_id=1, duration=50, texture=texture))

        # frame 3
        texture = arcade.load_texture("images/cook.png", x=0, y=1456, width=1063, height=1456)
        self.cook.frames.append(arcade.AnimationKeyframe(tile_id=2, duration=50, texture=texture))

        
        # cook position
        self.cook.scale = 0.5
        self.cook.center_x = 640
        self.cook.center_y = 360

    def on_draw(self):
        arcade.start_render()
        self.cook.draw()

    def on_update(self, delta_time: float):
        self.cook.update_animation()


win = GameWindow(1280, 720, "Game Window")
arcade.run()
