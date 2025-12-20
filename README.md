# 🚓 Digital Fugitive: AI Police Surveillance

A Python simulation where an AI agent systematically searches a city grid to find hidden thieves. Built using **Pygame**.

## 📖 About the Project
This project simulates a "Hide and Seek" scenario between a human user and an Artificial Intelligence.
1.  **Phase 1 (Human):** You act as the **Digital Fugitive**, hiding thieves in a cyberpunk city grid.
2.  **Phase 2 (AI):** The **Police AI** takes over, scanning the grid sector-by-sector to locate the fugitives.

## ⚙️ Features
* **Interactive Grid:** Click to place/remove thieves.
* **Smart AI Logic:** The police agent uses randomized search algorithms with state memory to track cleared sectors.
* **Visual Feedback:**
    * 🟨 **Yellow Border:** Police Scanner active.
    * 🟢 **Green Jail:** Fugitive apprehended.
    * ⚪ **Grey Dot:** Sector clear.
* **Cyberpunk UI:** Neon aesthetics and thematic overlays.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** Pygame

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git](https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git)
    ```
2.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
3.  **Run the simulation:**
    ```bash
    python runner3.py
    ```

## 🎮 Controls
* **Left Click:** Place/Remove Fugitives (Phase 1).
* **ENTER Key:** Initiate Police Scan (Phase 2).
