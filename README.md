# 🚓 AI Police Surveillance Project

A Python simulation where an AI agent systematically searches a city grid to find hidden thieves. Built using **Pygame**.

## 📖 About the Project
This project simulates a "Hide and Seek" scenario between a human user and an Artificial Intelligence.
1.  **Phase 1 (Human):** You act as the criminal mastermind, hiding thieves in a city grid.
2.  **Phase 2 (AI):** The AI takes over, scanning the grid sector-by-sector to locate the hidden thieves.

## ⚙️ Features
* **Interactive Grid:** Click to place/remove thieves.
* **AI Search Logic:** The AI uses a randomized search algorithm with memory to avoid checking the same spot twice.
* **Visual Feedback:**
    * 🟨 **Yellow Border:** AI currently scanning.
    * 🟢 **Green Jail:** Thief caught!
    * ⚪ **Grey Dot:** Sector clear.
* **Dynamic UI:** Phase-based text updates and neon aesthetic.

## 🛠️ Built With
* **Python 3.x**
* **Pygame**

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sooriya-moorthy-0107/AI-Police-Surveillance.git](https://github.com/sooriya-moorthy-0107/AI-Police-Surveillance.git)
    ```
2.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
3.  **Run the game:**
    ```bash
    python runner.py
    ```

## 🎮 Controls
* **Left Click:** Toggle Thief placement (Phase 1 only).
* **ENTER Key:** Finish hiding and start the AI simulation.