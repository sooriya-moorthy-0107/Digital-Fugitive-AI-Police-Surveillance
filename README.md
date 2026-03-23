# 🚓 Digital Fugitive: AI Police Surveillance

Step into a neon-lit cyberpunk world where man and machine play the ultimate game of hide and seek. Built with Pygame, this interactive Python simulation demonstrates how an Artificial Intelligence agent uses advanced algorithms to track down hidden thieves across a sprawling city grid.

From basic brute-force searches to complex logical deduction and constraint propagation, Digital Fugitive brings AI concepts to life through dynamic visual feedback and immersive gameplay.

## 📖 How It Works

The simulation is split into two distinct phases:

1. Phase 1: The Setup (Human) – You take on the role of the Digital Fugitive. Your objective is to strategically hide your thieves across the sectors of a cyberpunk city grid.

2. Phase 2: The Hunt (AI) – The Police AI is deployed. Scanning sector by sector, it uses a variety of search algorithms and logical deduction methods (depending on the version) to pinpoint and apprehend your fugitives.


## 🧠 Core Algorithms & AI Logic

This project serves as a practical showcase for multiple AI search and deduction techniques:

* **Propositional Logic & Knowledge-Based Agents:** Much like a smart Minesweeper solver, the core AI (```agent.py``` & ```brain.py```) generates logical ```Sentence``` objects based on grid intel (e.g., ```{House A, House B} = 1 Thief```).

* **Constraint Propagation & Set-Difference:** The AI actively compares overlapping data sets to infer safe zones and target locations. For example, if ```{A, B, C} = 2``` and ```{A, B} = 1```, it immediately deduces that ```{C} = 1```.

* **Manhattan Distance Heuristics:** Calculates absolute grid-based proximity (ignoring diagonal shortcuts) to generate dynamic Heat Maps.

* **Randomized Exhaustive Search:** A baseline "blind search" algorithm used to contrast and highlight the efficiency of the smart AI models.

## ⚙️ Key Features

* **Interactive City Grid:** Manually place or remove thieves before triggering the AI sweep.

* **Dynamic Visual Feedback:**

    *  **🟨 Yellow Border:** Police Scanner actively checking a sector.

    * **🟢 Green Jail / Asset:** Fugitive successfully apprehended.

    * **⚪ Grey Dot / Translucent Cell:** Sector cleared and marked safe.

* **🔥❄️ Hot and Cold Radar:** Watch the AI "heat up" as it closes in on a target. Cleared sectors dynamically shift from Deep Blue (Cold) to Bright Red (Hot) based on their proximity to a fugitive.

* **Cyberpunk UI & Immersive Assets:** Custom icons (Police, Thieves, Jail), sleek neon aesthetics, and an atmospheric looping siren audio track.

* **Expanded Terrain Mode:** Test the AI's limits on a massive 16x16 grid requiring deep logical search patterns.

## 🛠️ Tech Stack

* **Language: Python 3.x**

* **Libraries: Pygame**

## 🚀 Getting Started

1. **Installation**

    Clone the repository to your local machine and install the required dependencies:
    ```bash
        git clone [https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git](https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git)

        cd Digital-Fugitive-AI-Police-Surveillance
    
        pip install -r requirements.txt
    ```
2. **Install requirements:**
    ```bash
    pip install pygame
    ```

3. **Run the Simulations**

    This project includes multiple iterations of the AI. Run the specific file that matches the simulation experience you want to see:

    * **The Ultimate Version (runner5.py)🌟**

        * **Logic:** Knowledge-Based Agent + Manhattan Distance Heat Map.

        * Description: The complete package. Features the massive 16x16 grid, Hot/Cold Radar visuals, audio sirens, and full image assets.

            ```bash
            python runner5.py
            ```
    * **Classic Basic Version (runner.py)**

        * **Logic:** Knowledge-Based Agent (agent.py).

        * **Description:** The original 8x8 grid utilizing simple text and colors. Perfect for analyzing the raw logical deduction algorithms.

            ```bash
            python runner.py
            ```

    * **Cyberpunk UI Version (runner2.py)**

        * **Logic: Randomized Blind Search.**

        * **Description:** Enhanced neon UI with translucent grid cells. Watch the AI randomly sweep the city without advanced memory logic.

            ```bash
            python runner2.py
            ```

    * **Immersive Assets Version (runner3.py)**

        * **Logic:** Randomized Blind Search.

        * **Description:** Includes background images, graphical icons, and looping audio with random sector scanning.

            ```bash
            python runner3.py
            ```

    * **CLI Text Version (runner4.py)**

        * **Logic:** Relative Proximity Feedback.

        * **Description:** A terminal-based "Hot and Cold" number-guessing game that demonstrates the core proximity tracking logic natively in your console.

            ```bash
            python runner4.py
            ```

## 🎮 Controls

**Left Click:** Place or remove fugitives on the grid (Phase 1).

**ENTER Key:** Deploy the Police AI and initiate the scan (Phase 2).

© sooriyamoorthy0107.