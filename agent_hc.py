import random

class HotColdAI:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.visited = set()
        # Start by assuming the fugitive could be anywhere
        self.candidates = set((r, c) for r in range(height) for c in range(width))

    def add_signal(self, cell, distance):
        self.visited.add(cell)
        
        # Eliminate candidates that are NOT at the measured distance
        still_possible = set()
        for r, c in self.candidates:
            if abs(r - cell[0]) + abs(c - cell[1]) == distance:
                still_possible.add((r, c))
        
        self.candidates = self.candidates.intersection(still_possible)

    def choose_move(self):
        # Prefer a candidate that hasn't been visited
        options = list(self.candidates - self.visited)
        if options:
            return random.choice(options)
        
        # Fallback to any unvisited cell if candidates are empty (shouldn't happen)
        all_cells = set((r, c) for r in range(self.height) for c in range(self.width))
        remaining = list(all_cells - self.visited)
        return random.choice(remaining) if remaining else None