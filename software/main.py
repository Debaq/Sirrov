import os
from types import NoneType
import pyglet
from pyglet.window import key



class game(pyglet.window.Window):
    def __init__(self):
        super(game,self).__init__(480,100,caption="control")
        self.set_location(0, 718)
        
    
    def on_key_press(self, symbol, modifiers):
        print(f"{symbol} pressed, {modifiers}")
        if symbol == key.R:
            x,y = self.get_location()
            print(f"x: {x}, y: {y}")
        #    self.horizontal -= 1

    def on_key_release(self, symbol, modifiers):
        print(f"{symbol} released")


class Eye(pyglet.window.Window):
    def __init__(self,name):
        super(Eye, self).__init__(240,240)
        self.images = self.load_images_array()

        self.label = pyglet.text.Label(name,
                          font_name='Times New Roman',
                          color=(255,0,0,255),
                          font_size=12,
                          x=10, y=30,
                          anchor_x='left', anchor_y="top")

        self.horizontal = 30
        self.vertical = 7

    def on_draw(self):
        self.clear()
        self.images[self.vertical][self.horizontal].blit(0,0)
        self.label.draw()
        

    def load_images_array(self)-> list:
        """
        Returns:
            list: List with load images
        """
        def load_images(direction, ran):
            arr_images = []
            for i in range(ran):
                L_image = []
                name_dir = 'src/img/{}/L{}/'.format(direction,i+1)
                files = os.listdir(name_dir) 
                for file in range(len(files)):
                    name_tmp= "{}{}L{}-{:04d}.png".format(name_dir,direction,i+1,file)
                    tmp_img = pyglet.resource.image(name_tmp)
                    L_image.append(tmp_img)
                arr_images.append(L_image)
            return arr_images
        arr_images = []
        for i in load_images("P",7):
            arr_images.append(i)
        for i in load_images("C",1):
            arr_images.append(i)
        for i in load_images("N",7):
            arr_images.append(i)
        return arr_images


    
        

if __name__ == '__main__':
    left = Eye("left")
    rigth = Eye("rigth")
    control = game()

    pyglet.app.run()