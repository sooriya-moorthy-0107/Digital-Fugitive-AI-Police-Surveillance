import pygame
import sys

# Import the Agent from your existing file
from agent import MinesweeperAI

# --- SETTINGS ---
HEIGHT = 16  
WIDTH = 16   
CELL_SIZE = 40 

# --- BASE COLORS ---
BLACK = (20, 20, 30)
WHITE = (255, 255, 255)
GRID_LINE = (50, 50, 60)
HOUSE_UNKNOWN = (80, 80, 90)        
POLICE_BLUE = (30, 144, 255)        
THIEF_RED = (220, 20, 60)           
TEXT_COLOR = (0, 0, 0)

# --- HOT AND COLD COLORS ---
HOT_COLOR = (255, 100, 100)      # Red/Orange - Very close!
WARM_COLOR = (255, 200, 100)     # Yellow/Orange - Getting warmer
COLD_COLOR = (150, 220, 255)     # Light Blue - A bit chilly
FROZEN_COLOR = (80, 130, 200)    # Deep Blue - Nowhere near a thief

def get_heat_color(cell, thieves):
    """Returns a Hot/Cold color based on distance to the nearest thief."""
    if not thieves:
        return (200, 200, 200) # Default grey if no thieves exist
        
    # Calculate Manhattan distance to the nearest thief
    min_dist = min(abs(cell[0] - t[0]) + abs(cell[1] - t[1]) for t in thieves)
    
    if min_dist <= 2:
        return HOT_COLOR
    elif min_dist <= 4:
        return WARM_COLOR
    elif min_dist <= 6:
        return COLD_COLOR
    else:
        return FROZEN_COLOR

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
    screen = pygame.display.set_mode((WIDTH*CELL_SIZE + 100, HEIGHT*CELL_SIZE + 150))
    pygame.display.set_caption("AI Police - Hot & Cold Radar")
    
    font_header = pygame.font.SysFont("arial", 24, bold=True)
    font_cell = pygame.font.SysFont("arial", 16, bold=True)
    font_small = pygame.font.SysFont("arial", 10, bold=True)

    city = CityGrid()
    ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

    revealed = set()
    lost = False
    setup_mode = True 
    
    offset_x = 50
    offset_y = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and setup_mode:
                mx, my = pygame.mouse.get_pos()
                c = (mx - offset_x) // CELL_SIZE
                r = (my - offset_y) // CELL_SIZE
                if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                    city.toggle_thief((r, c))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and setup_mode:
                    setup_mode = False
                    print("HOT/COLD RADAR ACTIVATED")

        if not setup_mode and not lost:
            pygame.time.delay(100) 
            
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

        screen.fill(BLACK)

        if setup_mode:
            t1 = font_header.render("PHASE 1: SET TRAPS", True, THIEF_RED)
            t2 = font_small.render("Click grid to hide thieves. Press ENTER to start.", True, WHITE)
            screen.blit(t1, (offset_x, 20))
            screen.blit(t2, (offset_x, 60))
        elif lost:
            t1 = font_header.render("MISSION FAILED", True, THIEF_RED)
            screen.blit(t1, (offset_x, 30))
        else:
            t1 = font_header.render("PHASE 2: RADAR TRACKING", True, WARM_COLOR)
            screen.blit(t1, (offset_x, 30))

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
                        color = (200, 200, 200)
                
                else:
                    if (r,c) in ai.mines: 
                        color = THIEF_RED
                        text = "BUSTED"
                        txt_col = WHITE
                    elif (r,c) in ai.safes and (r,c) not in revealed:
                        color = POLICE_BLUE 
                    elif (r,c) in revealed:
                        # --- HOT AND COLD FEATURE ---
                        color = get_heat_color((r, c), city.thieves)
                        intel = city.get_intel((r,c))
                        if intel > 0: text = str(intel)
                    
                    if lost and (r,c) in city.thieves:
                        color = (100, 0, 0)
                        text = "T"
                        txt_col = WHITE

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRID_LINE, rect, 2)
                
                if text:
                    f = font_small if text == "BUSTED" else font_cell
                    txt_surf = f.render(text, True, txt_col)
                    txt_rect = txt_surf.get_rect(center=rect.center)
                    screen.blit(txt_surf, txt_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()