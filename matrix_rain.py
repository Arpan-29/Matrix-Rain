import pygame
import random

pygame.init()
screenWidth = 1000
screenHeight = 600
win = pygame.display.set_mode((screenWidth, screenHeight ))
pygame.display.set_caption("Matrix Rain")

pygame.font.init()
symbol_size = 20
font = pygame.font.SysFont("comicsansms", symbol_size)
symbol_list = 'QWERTYUIOPASDFGHJKLZXCVBNM[]|;:",./<>?`~1234567890-=!@#$%^&*()_+'
# symbol_list = '\u030a\u030b'
print('\u030a\u030b')

class Stream :
    def __init__(self, x) :
        self.x = x
        self.symbols = []
        self.number_of_symbols = random.randint(3, screenWidth // symbol_size)
        self.rain_speed = random.randint(1, 3)

    def init_symbols(self) :
        height = random.randint(2, 20)
        for i in range(self.number_of_symbols) :
            y = -(i + height) * symbol_size
            self.symbols.append(Symbol(self.x, y))

        dc_green = 254 // self.number_of_symbols
        dc_blue = 89 // self.number_of_symbols
        i = 0
        for symbol in self.symbols :
            symbol.set_color((0, 255 - i * dc_green, 90 - i * dc_blue))
            i += 1

        prob_of_change_color = 1
        if random.random() < prob_of_change_color :
            r = random.randint(0, self.number_of_symbols // 2)
            self.symbols[r].change_color()

    def draw(self) :
        for symbol in self.symbols :
            text = font.render(symbol.value, True, symbol.color)
            win.blit(text, (symbol.x, symbol.y))

    def rain(self) :
        for symbol in self.symbols :
            symbol.y += self.rain_speed
            
            if frame_count % (symbol.change_speed) == 0 :
                symbol.change_value()

    def reached_bottom(self) :
        if self.symbols[self.number_of_symbols - 1].y > screenHeight :
            self.symbols = []
            self.init_symbols()

class Symbol :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        self.value = ''
        self.color = (0, 255, 90)
        self.change_speed = random.randint(5, 100)
    
    def change_value(self) :
        r = random.randint(0, len(symbol_list) - 1)
        self.value = symbol_list[r]

    def set_color(self, color) :
        self.color =  color

    def change_color(self) :
        self.color = (255,255,255) 

number_of_streams = screenWidth // symbol_size
streams = []
for i in range(number_of_streams) :
    streams.append(Stream(i * symbol_size))
    
for stream in streams :
    stream.init_symbols()

pause = False
frame_count = 0
run = True
while run :

    pygame.time.delay(10)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        pygame.time.delay(100)
        pause = not pause

    if not pause :
        win.fill(0)

        for stream in streams :
            stream.rain()
            stream.draw()
            stream.reached_bottom()

        pygame.display.update()
        frame_count += 1

pygame.quit()