import ST7789


class display:
    def __init__(self, SPI, CS):
        if SPI == 0 and CS == 0:
            self.port = 0
            self.cs = 0
            self.dc = 9
        elif SPI == 1 and CS == 0:
            self.port = 1
            self.cs = 0
            self.dc = 12
        elif SPI == 0 and CS == 1:
            self.port = 0
            self.cs = 1
            self.dc = 9

        self.height = 240
        self.width = 240
        self.rotation = 0
        self.offset_left = 0
        self.offset_top = 0
        self.spi_speed_hz = 96*1000*1000
        self.st7789 = self.create()


    def create(self):
        return ST7789.ST7789(
            height = self.height,
            width = self.width,
            rotation = self.rotation,
            port = self.port,
            cs = self.cs,
            dc = self.dc,
            spi_speed_hz = self.spi_speed_hz,
            offset_left = self.offset_left,
            offset_top = self.offset_top
        )

    def reset(self):
        self.st7789.reset()


    def test(self):
        import numpy
        image = numpy.empty((self.width, self.height, 3))
        self.st7789.display(image)
    
    def set_window(self):
        self.st7789.set_window()

    def data(self, data):
        self.st7789.data(data)