import arcade

class Chef(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = None
        self.set_location(200, 90)
        self.player_list = None
        self.player = None
        
        self.setup()
        
        self.sprite_list = arcade.SpriteList()
        #self.sprite_list.append (self.chef)
        #self.sprite_list.append (self.counter)
    

    
    def setup(self):
       
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedTimeBasedSprite()
        self.player.textures = [] 

        self.player.textures.append(arcade.load_texture("Images/lion.png", x=0, y=0, width=512, height=256))
        self.player.textures.append(arcade.load_texture("Images/lion.png", x=512, y=0, width=512, height=256))
        self.player.textures.append(arcade.load_texture("Images/lion.png", x=0, y=256, width=512, height=256))
        
        #x_pos = 0s
        #y_pos = 0

        #for x in range(8):
            #if x % 2 == 0:
                #x_pos == 0
            #else:
                #x_pos = 512
            #if x % 8 in [2, 4, 8]:
                #y_pos += 256
            #self.player.textures.append(arcade.load_textures("Images/cook.png", x=x_pos, y=y_pos, width=2126, height=4370))
            
        
       
        #self.chef = arcade.Sprite("Images/Chef.png", 0.03)
        #self.chef2 = arcade.Sprite("Images/Chef2.png", 0.03)
        #self.counter = arcade.Sprite("Images/Counter.png", 0.08)
        
        #self.player.center_x = 480
        #self.player.center_y = 450

        self.player.center_x = 1280 // 2
        self.player.center_y = 720 // 2


        #for i in range (2): 
            #self.chef.textures.append(arcade.load_texture("Images/Chef.png", x=i*100, y=0, width= 100, height=100))

        self.player_list.append(self.player)
        
    def on_draw(self):
        arcade.start_render()
        #arcade.draw_lrwh_rectangle_textured(0,0,1024,600, self.bg)
        self.player_list.draw()
        #self.chef2.draw()
        #self.player_list.draw()
        #self.counter.draw()

    def on_update(self, delta_time):
        self.player_list.update_animation()
            

#def main():
Chef(1280, 720, "Dinnerdash")

    #window.setup()
arcade.run()



if __name__ == "__main__":
    main()