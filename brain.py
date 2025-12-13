import itertools

class Sentence:
    """
    A logical statement about a set of houses and how many thieves are in them.
    Example: {House A, House B, House C} = 1 Thief
    """
    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """ Returns the set of all cells known to be Thieves. """
        if len(self.cells) == self.count and self.count != 0:
            return self.cells
        return set()

    def known_safes(self):
        """ Returns the set of all cells known to be Safe. """
        if self.count == 0:
            return self.cells
        return set()

    def mark_mine(self, cell):
        """ Updates logic when a Thief is identified """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """ Updates logic when a House is cleared """
        if cell in self.cells:
            self.cells.remove(cell)