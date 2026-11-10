import time


class PerformanceMonitor:

    def __init__(self):
        self.start_time = time.perf_counter()
        self.total_moves = 0
        self.total_scanned = 0
        self.safe_houses = 0
        self.detected_thieves = 0

    def record_move(self):
        self.total_moves += 1

    def record_scan(self):
        self.total_scanned += 1

    def record_safe_house(self):
        self.safe_houses += 1

    def record_thief(self):
        self.detected_thieves += 1

    def get_execution_time(self):
        return round(time.perf_counter() - self.start_time, 3)

    def display_report(self):
        print("\n========== AI PERFORMANCE REPORT ==========")
        print("Total Moves:", self.total_moves)
        print("Houses Scanned:", self.total_scanned)
        print("Safe Houses:", self.safe_houses)
        print("Thieves Identified:", self.detected_thieves)
        print("Execution Time:", self.get_execution_time(), "seconds")
        print("============================================")


if __name__ == "__main__":
    monitor = PerformanceMonitor()

    monitor.record_move()
    monitor.record_scan()
    monitor.record_safe_house()

    monitor.display_report()