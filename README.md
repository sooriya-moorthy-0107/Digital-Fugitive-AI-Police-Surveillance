<h1>🚓 Digital Fugitive: AI Police Surveillance</h1>

A Python simulation where an AI agent systematically searches a city grid to find hidden thieves. Built using Pygame, this project showcases various Artificial Intelligence techniques including logical deduction, constraint propagation, domain reduction, and dynamic visual feedback.

<h2><b>📖 About the Project<b></h2>

This project simulates a "Hide and Seek" scenario between a human user and an Artificial Intelligence.
<br>
<ol>
<li><b>Phase 1 (Human):</b> You act as the Digital Fugitive, hiding thieves in a cyberpunk city grid.</li>
<br>
<li><b> Phase 2 (AI):</b> The Police AI takes over, scanning the grid sector-by-sector to locate the fugitives. Depending on the version you run, the AI uses different algorithms to hunt down the targets.</li>
</ol>

<h2><b> 🧠 Core Algorithms & AI Logic</b> </h2>
<ul>
This project explores multiple approaches to search and deduction:
<li>
<b>Propositional Logic & Knowledge-Based Agents:</b> The core AI (agent.py & brain.py) treats the grid like a Minesweeper board. It creates logical Sentence objects (e.g., {House A, House B} = 1 Thief).
</li><br>
<li>
<b>Constraint Propagation & Set-Difference:</b> The AI compares overlapping logical sentences. If {A, B, C} = 2 and {A, B} = 1, the AI deduces {C} = 1.
</li><br>
<li>
<b>Constraint Satisfaction Problem (CSP) / Domain Reduction:</b> The Hot & Cold AI (agent_hc.py) starts with the entire grid as possible candidates and intersects sets to eliminate impossible locations based on exact distance signals.
</li><br>
<li>
<b>Manhattan Distance / Heuristics:</b> Used to calculate grid-based proximity (Heat Maps) without diagonal shortcuts.
</li><br>
<li>
<b>Randomized Exhaustive Search:</b> A baseline "blind search" algorithm used in early iterations to compare against the smart AI.
</li><br>
</ul>
**⚙️ Features**

**Interactive Grid:** Click to place/remove thieves before initiating the AI scan.

**Visual Feedback:**

**🟨 Yellow Border:** Police Scanner active.

**🟢 Green Jail / Asset:** Fugitive apprehended.

**⚪ Grey Dot / Translucent Cell:** Sector clear.

**Cyberpunk UI & Immersive Assets:** Custom graphical assets (Police, Thieves, Jail), neon aesthetics, and atmospheric background sirens.

**🔥❄️ Hot and Cold Radar:** The AI dynamically colors cleared sectors on a spectrum from Deep Blue (Cold) to Bright Red (Hot) based on proximity.

**Expanded Terrain:** Play on a massive 16x16 grid that forces the AI to execute deeper logical search patterns.

**🛠️ Tech Stack**

**Language:** Python 3.x

**Library:** Pygame

**🚀 How to Run**

**Clone the repository:**
```Bash
git clone [https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git](https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git)
cd Digital-Fugitive-AI-Police-Surveillance
```

**Install requirements:**
```bash
pip install pygame
```

**Run the simulations (Choose your version):**

**The Ultimate Version (runner5.py) 🌟**

**Logic Used:** Knowledge-Based Agent (Propositional Logic, Set-Difference) + Manhattan Distance calculations for the Heat Map.

**Description:** Combines everything: 16x16 Large Grid, Hot/Cold Radar visuals, Audio Sirens, and Image Assets.
```bash
python runner5.py
```

**Classic Basic Version (runner.py)**

**Logic Used:** Knowledge-Based Agent (agent.py). Base Minesweeper-style logic.

**Description:** The original 8x8 grid using text and basic colors. Focuses purely on the base logical deduction algorithms.
```bash
python runner.py
```

**Cyberpunk UI Version (runner2.py)**

**Logic Used:** Randomized Blind Search (Brute Force Exhaustive Search).

**Description:** Enhanced neon UI with transparent grids. The AI randomly scans the city without advanced memory logic.
```bash
python runner2.py
```

**Immersive Assets Version (runner3.py)**

**Logic Used:** Randomized Blind Search.

**Description:** Features background images, thief/police icons, and looping audio with random sector scanning.
```bash
python runner3.py
```

**CLI Text Version (runner4.py)**

**Logic Used:** Relative Proximity Feedback (comparing historical distance states).

**Description:** A terminal-based "Hot and Cold" number guessing game demonstrating the core proximity tracking logic without Pygame.
```bash
python runner4.py
```

**🎮 Controls**

**Left Click:** Place/Remove Fugitives (Phase 1).

**ENTER Key:** Initiate Police Scan & Radar (Phase 2).