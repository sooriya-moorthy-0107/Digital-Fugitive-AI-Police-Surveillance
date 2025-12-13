import pygame
import sys
import time

# Import the Agent
from agent import MinesweeperAI

# --- SETTINGS ---
HEIGHT = 8
WIDTH = 8
CELL_SIZE = 60

# --- COLORS (Police Theme) ---
BLACK = (20, 20, 30)
WHITE = (255, 255, 255)
GRID_LINE = (50, 50, 60)
HOUSE_UNKNOWN = (80, 80, 90)        # Dark Grey
HOUSE_CLEARED = (200, 200, 200)     # Light Grey
POLICE_BLUE = (30, 144, 255)        # AI Thinking
THIEF_RED = (220, 20, 60)           # Criminal
TEXT_COLOR = (0, 0, 0)

class CityGrid:
    def __init__(self):
        self.thieves = set()

    def toggle_thief(self, cell):
        if cell in self.thieves:
            self.thieves.remove(cell)
        else:
            self.thieves.add(cell)

    def get_intel(self, cell):
        count = 0
        for i in range(cell[0]-1, cell[0]+2):
            for j in range(cell[1]-1, cell[1]+2):
                if (i, j) == cell: continue
                if 0 <= i < HEIGHT and 0 <= j < WIDTH:
                    if (i, j) in self.thieves:
                        count += 1
        return count

def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT*CELL_SIZE + 100, WIDTH*CELL_SIZE + 150))
    pygame.display.set_caption("AI Police Surveillance Project")
    
    font_header = pygame.font.SysFont("arial", 24, bold=True)
    font_cell = pygame.font.SysFont("arial", 20, bold=True)
    font_small = pygame.font.SysFont("arial", 12, bold=True)

    city = CityGrid()
    ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

    revealed = set()
    lost = False
    setup_mode = True # Start in Setup Mode
    
    # Margin for centering
    offset_x = 50
    offset_y = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # CLICK TO HIDE THIEVES
            if event.type == pygame.MOUSEBUTTONDOWN and setup_mode:
                mx, my = pygame.mouse.get_pos()
                c = (mx - offset_x) // CELL_SIZE
                r = (my - offset_y) // CELL_SIZE
                if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                    city.toggle_thief((r, c))

            # ENTER TO START AI
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and setup_mode:
                    setup_mode = False
                    print("POLICE OPERATION STARTED")

        # --- AI AUTO-PLAY LOGIC ---
        if not setup_mode and not lost:
            pygame.time.delay(200) # Speed Control
            
            move = ai.make_safe_move()
            if move is None:
                move = ai.make_random_move()

            if move:
                if move in city.thieves:
                    lost = True
                    print(f"AMBUSH! Officer hit at {move}")
                else:
                    intel = city.get_intel(move)
                    revealed.add(move)
                    ai.add_knowledge(move, intel)

        # --- DRAWING ---
        screen.fill(BLACK)

        # Header Text
        if setup_mode:
            t1 = font_header.render("PHASE 1: SET TRAPS", True, THIEF_RED)
            t2 = font_small.render("Click grid to hide thieves. Press ENTER to start.", True, WHITE)
            screen.blit(t1, (offset_x, 20))
            screen.blit(t2, (offset_x, 60))
        elif lost:
            t1 = font_header.render("MISSION FAILED", True, THIEF_RED)
            screen.blit(t1, (offset_x, 30))
        else:
            t1 = font_header.render("PHASE 2: POLICE RAIDING", True, POLICE_BLUE)
            screen.blit(t1, (offset_x, 30))

        # Grid Drawing
        for r in range(HEIGHT):
            for c in range(WIDTH):
                rect = pygame.Rect(offset_x + c*CELL_SIZE, offset_y + r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                color = HOUSE_UNKNOWN
                text = ""
                txt_col = TEXT_COLOR

                if setup_mode:
                    if (r,c) in city.thieves:
                        color = THIEF_RED
                        text = "T"
                        txt_col = WHITE
                    else:
                        color = HOUSE_CLEARED
                
                else:
                    # AI STATES
                    if (r,c) in ai.mines: # Logically Busted
                        color = THIEF_RED
                        text = "BUSTED"
                        txt_col = WHITE
                    elif (r,c) in ai.safes and (r,c) not in revealed:
                        color = POLICE_BLUE # Safe but not visited
                    elif (r,c) in revealed:
                        color = HOUSE_CLEARED
                        intel = city.get_intel((r,c))
                        if intel > 0: text = str(intel)
                    
                    if lost and (r,c) in city.thieves:
                        color = (100, 0, 0)
                        text = "T"
                        txt_col = WHITE

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRID_LINE, rect, 2)
                
                if text:
                    if text == "BUSTED":
                        f = font_small
                    else:
                        f = font_cell
                    txt_surf = f.render(text, True, txt_col)
                    txt_rect = txt_surf.get_rect(center=rect.center)
                    screen.blit(txt_surf, txt_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()