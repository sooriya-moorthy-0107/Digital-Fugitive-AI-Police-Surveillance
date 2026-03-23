import pygame
import sys
import os
import random


pygame.init()
pygame.mixer.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GRID_SIZE = 8
CELL_SIZE = 60
MARGIN = 10
AI_SEARCH_SPEED = 600  


GRID_WIDTH = (CELL_SIZE * GRID_SIZE) + (MARGIN * (GRID_SIZE - 1))
GRID_HEIGHT = (CELL_SIZE * GRID_SIZE) + (MARGIN * (GRID_SIZE - 1))
START_X = (SCREEN_WIDTH - GRID_WIDTH) // 2
START_Y = (SCREEN_HEIGHT - GRID_HEIGHT) // 2 + 50 


NEON_BLUE = (0, 200, 255)
NEON_RED = (255, 50, 50)
NEON_GREEN = (50, 255, 50)
NEON_YELLOW = (255, 255, 0)
DARK_BLUE = (10, 10, 30)


SOLID_GREEN = (0, 128, 0) 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AI Police Surveillance Project")
clock = pygame.time.Clock()


def load_image(name, scale=None):
    if os.path.exists(name):
        img = pygame.image.load(name)
        if scale:
            img = pygame.transform.scale(img, scale)
        return img
    return None



bg_image = load_image("police_bg.jpg", (SCREEN_WIDTH, SCREEN_HEIGHT))


if bg_image:
    bg_image.set_alpha(150) 

thief_icon = load_image("thief.png", (CELL_SIZE, CELL_SIZE))


jail_icon = load_image("jail.png", (CELL_SIZE, CELL_SIZE)) 


class Game:
    def __init__(self):
        # 0=Empty, 1=Hidden Thief, 2=Busted, 3=Checked Empty
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.phase = 1
        self.last_ai_move_time = 0
        self.ai_targets = [] 
        self.current_scan = None 
        self.update_header_text()
        
    def update_header_text(self):
        if self.phase == 1:
            self.main_text = "PHASE 1: HIDE THE THIEVES"
            self.sub_text = "Click grid to hide thieves. Press ENTER to release the AI."
            self.text_color = NEON_RED
        elif self.phase == 2:
            self.main_text = "PHASE 2: AI SCANNING..."
            self.sub_text = "The AI is searching the city grid..."
            self.text_color = NEON_BLUE

    def start_ai_phase(self):
        self.phase = 2
        self.update_header_text()
        # Generate random search order
        all_coords = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]
        random.shuffle(all_coords)
        self.ai_targets = all_coords

    def ai_step(self):
        if not self.ai_targets:
            self.sub_text = "SCAN COMPLETE."
            self.current_scan = None
            return

        # Pick next spot
        row, col = self.ai_targets.pop()
        self.current_scan = (row, col) 

        # Check spot
        if self.grid[row][col] == 1:
            self.grid[row][col] = 2 # BUSTED
            print(f"AI found thief at {row}, {col}!")
        elif self.grid[row][col] == 0:
            self.grid[row][col] = 3 # EMPTY

    def draw_background(self):
        if bg_image:
            screen.blit(bg_image, (0, 0))
        else:
            screen.fill(DARK_BLUE)
            for i in range(0, SCREEN_WIDTH, 50):
                pygame.draw.line(screen, (30, 30, 80), (i, 0), (i, SCREEN_HEIGHT))
            for i in range(0, SCREEN_HEIGHT, 50):
                pygame.draw.line(screen, (30, 30, 80), (0, i), (SCREEN_WIDTH, i))

    def draw_siren_bar(self):
        current_time = pygame.time.get_ticks()
        if (current_time // 500) % 2 == 0:
            left, right = NEON_RED, NEON_BLUE
        else:
            left, right = NEON_BLUE, NEON_RED
        pygame.draw.rect(screen, left, (0, 0, SCREEN_WIDTH//2, 20))
        pygame.draw.rect(screen, right, (SCREEN_WIDTH//2, 0, SCREEN_WIDTH//2, 20))
        pygame.draw.line(screen, WHITE, (0, 20), (SCREEN_WIDTH, 20), 2)

    def draw_grid(self):
        
        s_solid = pygame.Surface((CELL_SIZE, CELL_SIZE))
        s_solid.fill(SOLID_GREEN) 

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = START_X + col * (CELL_SIZE + MARGIN)
                y = START_Y + row * (CELL_SIZE + MARGIN)
                
                cell_value = self.grid[row][col]
                border_color = NEON_BLUE

               
                if self.phase == 2 and self.current_scan == (row, col):
                    border_color = NEON_YELLOW
                    pygame.draw.rect(screen, NEON_YELLOW, (x, y, CELL_SIZE, CELL_SIZE), 4)

                
                if cell_value == 0:
                     screen.blit(s_solid, (x, y))
                elif cell_value == 1:
                    if self.phase == 1:
                        if thief_icon: screen.blit(thief_icon, (x, y))
                        else: pygame.draw.rect(screen, NEON_RED, (x, y, CELL_SIZE, CELL_SIZE))
                    else:
                        screen.blit(s_solid, (x, y)) 
                elif cell_value == 2: 

                    if jail_icon: screen.blit(jail_icon, (x, y))
                    else: pygame.draw.rect(screen, NEON_GREEN, (x, y, CELL_SIZE, CELL_SIZE))
                    border_color = NEON_GREEN 
                elif cell_value == 3: 
                     screen.blit(s_solid, (x, y))
                     pygame.draw.circle(screen, (0, 0, 0), (x + CELL_SIZE//2, y + CELL_SIZE//2), 5)

                if self.current_scan != (row, col):
                    pygame.draw.rect(screen, border_color, (x, y, CELL_SIZE, CELL_SIZE), 2)

    def handle_click(self, pos):
        if self.phase != 1: return
        mx, my = pos
        col = (mx - START_X) // (CELL_SIZE + MARGIN)
        row = (my - START_Y) // (CELL_SIZE + MARGIN)

        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            if self.grid[row][col] == 0: self.grid[row][col] = 1
            elif self.grid[row][col] == 1: self.grid[row][col] = 0

    def draw_ui(self):
        font_large = pygame.font.SysFont("Arial", 40, bold=True)
        font_small = pygame.font.SysFont("Arial", 18)
        
        text_shadow = font_large.render(self.main_text, True, BLACK)
        text_fg = font_large.render(self.main_text, True, self.text_color)
        screen.blit(text_shadow, (START_X + 2, START_Y - 80 + 2))
        screen.blit(text_fg, (START_X, START_Y - 80))
        
        instr = font_small.render(self.sub_text, True, WHITE)
        screen.blit(instr, (START_X, START_Y - 35))

    def run(self):
        running = True
        while running:
            current_time = pygame.time.get_ticks()

            if self.phase == 2:
                if current_time - self.last_ai_move_time > AI_SEARCH_SPEED:
                    self.ai_step()
                    self.last_ai_move_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event.pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.phase == 1:
                        self.start_ai_phase()

            self.draw_background()
            self.draw_siren_bar()
            self.draw_grid()
            self.draw_ui()

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()