<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Fugitive: AI Police Surveillance</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 850px;
            margin: 0 auto;
            padding: 30px 20px;
            background-color: #f9f9f9;
        }
        .container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        h1, h2, h3 {
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
        }
        h1 {
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-top: 0;
        }
        p {
            margin-bottom: 1em;
        }
        ul, ol {
            margin-bottom: 1.5em;
            padding-left: 25px;
        }
        li {
            margin-bottom: 0.5em;
        }
        strong {
            color: #1a252f;
        }
        code {
            font-family: ui-monospace, SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
            background-color: #f0f0f0;
            padding: 0.2em 0.4em;
            border-radius: 4px;
            font-size: 0.9em;
            color: #e83e8c;
        }
        pre {
            background-color: #282c34;
            color: #abb2bf;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
            margin-bottom: 1.5em;
        }
        pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
            font-size: 0.9em;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚓 Digital Fugitive: AI Police Surveillance</h1>

        <p>A Python simulation where an AI agent systematically searches a city grid to find hidden thieves. Built using <strong>Pygame</strong>, this project showcases various Artificial Intelligence techniques including logical deduction, constraint propagation, domain reduction, and dynamic visual feedback.</p>

        <h2>📖 About the Project</h2>
        <p>This project simulates a "Hide and Seek" scenario between a human user and an Artificial Intelligence.</p>
        <ol>
            <li><strong>Phase 1 (Human):</strong> You act as the <strong>Digital Fugitive</strong>, hiding thieves in a cyberpunk city grid.</li>
            <li><strong>Phase 2 (AI):</strong> The <strong>Police AI</strong> takes over, scanning the grid sector-by-sector to locate the fugitives. Depending on the version you run, the AI uses different algorithms to hunt down the targets.</li>
        </ol>

        <h2>🧠 Core Algorithms & AI Logic</h2>
        <p>This project explores multiple approaches to search and deduction:</p>
        <ul>
            <li><strong>Propositional Logic & Knowledge-Based Agents:</strong> The core AI (<code>agent.py</code> & <code>brain.py</code>) treats the grid like a Minesweeper board. It creates logical <code>Sentence</code> objects (e.g., <code>{House A, House B} = 1 Thief</code>).</li>
            <li><strong>Constraint Propagation & Set-Difference:</strong> The AI compares overlapping logical sentences. If <code>{A, B, C} = 2</code> and <code>{A, B} = 1</code>, the AI deduces <code>{C} = 1</code>.</li>
            <li><strong>Constraint Satisfaction Problem (CSP) / Domain Reduction:</strong> The Hot & Cold AI (<code>agent_hc.py</code>) starts with the entire grid as possible candidates and intersects sets to eliminate impossible locations based on exact distance signals.</li>
            <li><strong>Manhattan Distance / Heuristics:</strong> Used to calculate grid-based proximity (Heat Maps) without diagonal shortcuts.</li>
            <li><strong>Randomized Exhaustive Search:</strong> A baseline "blind search" algorithm used in early iterations to compare against the smart AI.</li>
        </ul>

        <h2>⚙️ Features</h2>
        <ul>
            <li><strong>Interactive Grid:</strong> Click to place/remove thieves before initiating the AI scan.</li>
            <li><strong>Visual Feedback:</strong>
                <ul>
                    <li>🟨 <strong>Yellow Border:</strong> Police Scanner active.</li>
                    <li>🟢 <strong>Green Jail / Asset:</strong> Fugitive apprehended.</li>
                    <li>⚪ <strong>Grey Dot / Translucent Cell:</strong> Sector clear.</li>
                </ul>
            </li>
            <li><strong>Cyberpunk UI & Immersive Assets:</strong> Custom graphical assets (Police, Thieves, Jail), neon aesthetics, and atmospheric background sirens.</li>
            <li><strong>🔥❄️ Hot and Cold Radar:</strong> The AI dynamically colors cleared sectors on a spectrum from Deep Blue (Cold) to Bright Red (Hot) based on proximity.</li>
            <li><strong>Expanded Terrain:</strong> Play on a massive 16x16 grid that forces the AI to execute deeper logical search patterns.</li>
        </ul>

        <h2>🛠️ Tech Stack</h2>
        <ul>
            <li><strong>Language:</strong> Python 3.x</li>
            <li><strong>Library:</strong> Pygame</li>
        </ul>

        <h2>🚀 How to Run</h2>
        <ol>
            <li><strong>Clone the repository:</strong>
<pre><code>git clone https://github.com/sooriya-moorthy-0107/Digital-Fugitive-AI-Police-Surveillance.git
cd Digital-Fugitive-AI-Police-Surveillance</code></pre>
            </li>
            <li><strong>Install requirements:</strong>
<pre><code>pip install pygame</code></pre>
            </li>
            <li><strong>Run the simulations (Choose your version):</strong>
                <ul>
                    <li><strong>The Ultimate Version (<code>runner5.py</code>)</strong> 🌟
                        <ul>
                            <li><strong>Logic Used:</strong> Knowledge-Based Agent (Propositional Logic, Set-Difference) + Manhattan Distance calculations for the Heat Map.</li>
                            <li><strong>Description:</strong> Combines everything: 16x16 Large Grid, Hot/Cold Radar visuals, Audio Sirens, and Image Assets.</li>
                        </ul>
<pre><code>python runner5.py</code></pre>
                    </li>
                    <li><strong>Classic Basic Version (<code>runner.py</code>)</strong>
                        <ul>
                            <li><strong>Logic Used:</strong> Knowledge-Based Agent (<code>agent.py</code>). Base Minesweeper-style logic.</li>
                            <li><strong>Description:</strong> The original 8x8 grid using text and basic colors. Focuses purely on the base logical deduction algorithms.</li>
                        </ul>
<pre><code>python runner.py</code></pre>
                    </li>
                    <li><strong>Cyberpunk UI Version (<code>runner2.py</code>)</strong>
                        <ul>
                            <li><strong>Logic Used:</strong> Randomized Blind Search (Brute Force Exhaustive Search).</li>
                            <li><strong>Description:</strong> Enhanced neon UI with transparent grids. The AI randomly scans the city without advanced memory logic.</li>
                        </ul>
<pre><code>python runner2.py</code></pre>
                    </li>
                    <li><strong>Immersive Assets Version (<code>runner3.py</code>)</strong>
                        <ul>
                            <li><strong>Logic Used:</strong> Randomized Blind Search.</li>
                            <li><strong>Description:</strong> Features background images, thief/police icons, and looping audio with random sector scanning.</li>
                        </ul>
<pre><code>python runner3.py</code></pre>
                    </li>
                    <li><strong>Proximity Sensing Version (<code>runner_hc.py</code>)</strong>
                        <ul>
                            <li><strong>Logic Used:</strong> Constraint Satisfaction / Domain Reduction (<code>agent_hc.py</code>).</li>
                            <li><strong>Description:</strong> Uses absolute Manhattan distance measurements to eliminate grid coordinates until only the exact location of the fugitive remains.</li>
                        </ul>
<pre><code>python runner_hc.py</code></pre>
                    </li>
                    <li><strong>CLI Text Version (<code>runner4.py</code>)</strong>
                        <ul>
                            <li><strong>Logic Used:</strong> Relative Proximity Feedback (comparing historical distance states).</li>
                            <li><strong>Description:</strong> A terminal-based "Hot and Cold" number guessing game demonstrating the core proximity tracking logic without Pygame.</li>
                        </ul>
<pre><code>python runner4.py</code></pre>
                    </li>
                </ul>
            </li>
        </ol>

        <h2>🎮 Controls</h2>
        <ul>
            <li><strong>Left Click:</strong> Place/Remove Fugitives (Phase 1).</li>
            <li><strong>ENTER Key:</strong> Initiate Police Scan & Radar (Phase 2).</li>
        </ul>
    </div>
</body>
</html>