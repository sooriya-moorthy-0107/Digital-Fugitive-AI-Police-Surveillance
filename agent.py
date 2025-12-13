import random
from brain import Sentence

class MinesweeperAI:
    """
    The Detective Agent that tracks safe houses and thieves.
    """
    def __init__(self, height=8, width=8):
        self.height = height
        self.width = width
        self.moves_made = set()
        self.mines = set() # Identified Thieves
        self.safes = set() # Safe Houses
        self.knowledge = [] # List of logical sentences

    def mark_mine(self, cell):
        if cell in self.mines: return
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        if cell in self.safes: return
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """ 
        Main Logic Loop: 
        1. Add new clue.
        2. Deduce new facts using Set Difference.
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # 1. Identify neighbors
        cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell: continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if (i, j) not in self.safes and (i, j) not in self.moves_made:
                        if (i, j) in self.mines:
                            count -= 1
                        else:
                            cells.add((i, j))

        # 2. Add new sentence to brain
        new_sentence = Sentence(cells, count)
        self.knowledge.append(new_sentence)

        # 3. Constraint Propagation (The "Thinking" Loop)
        changed = True
        while changed:
            changed = False
            
            safes = set()
            mines = set()
            for sentence in self.knowledge:
                safes = safes.union(sentence.known_safes())
                mines = mines.union(sentence.known_mines())

            if safes or mines:
                changed = True
                for safe in safes: self.mark_safe(safe)
                for mine in mines: self.mark_mine(mine)

            self.knowledge = [s for s in self.knowledge if s.cells]

            # The Advanced Logic: Set Difference
            new_inferences = []
            for s1 in self.knowledge:
                for s2 in self.knowledge:
                    if s1 == s2: continue
                    if s2.cells.issubset(s1.cells):
                        new_cells = s1.cells - s2.cells
                        new_count = s1.count - s2.count
                        new_inferences.append(Sentence(new_cells, new_count))
            
            for s in new_inferences:
                if s not in self.knowledge:
                    self.knowledge.append(s)
                    changed = True

    def make_safe_move(self):
        for cell in self.safes:
            if cell not in self.moves_made and cell not in self.mines:
                return cell
        return None

    def make_random_move(self):
        possible_moves = []
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) not in self.moves_made and (i, j) not in self.mines:
                    possible_moves.append((i, j))
        
        if not possible_moves: return None
        return random.choice(possible_moves)