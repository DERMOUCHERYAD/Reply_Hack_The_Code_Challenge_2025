# The Green Revolution Game Challenge

Welcome to the **Green Revolution Game Challenge**!

## What Is the Challenge?

Imagine you have a small budget and you need to power a set of buildings over many rounds (or turns). In each round, you're given:

- **A minimum number of buildings that must be powered** (to get any profit).
- **A maximum limit on the number of buildings that count for profit.**
- **A profit value for every building you successfully power.**

You have several types of energy resources you can buy. Each resource costs money to purchase and has ongoing costs to keep it working. It can power a certain number of buildings for a few rounds before it needs a break or stops working entirely. Some resources even have special effects that might boost your profit or change how many buildings you can power.

Your goal is to make smart choices about which resources to buy and when—so you always meet the minimum required, maximize your profit, and never run out of money.

## What Does the Solver Do?

Your solver is a computer program that helps you decide, turn by turn, what to buy and when. Here's a simple overview:

1. **Reads the Game Data:**  
   It takes an input file that tells it your starting budget, details about each resource (like cost, how many buildings it powers, etc.), and the rules for each round (minimum, maximum, and profit per building).

2. **Simulates Each Turn:**  
   For every turn, the solver:
   - Checks how many buildings are being powered by the resources you already own.
   - Compares that number to the required minimum.
   - If you’re below the minimum, it decides to purchase more resources, choosing those that give you the best “bang for your buck.”
   - It then calculates the turn's profit (and subtracts maintenance costs) so that the remaining money becomes your new budget for the next turn.

3. **Produces a Purchase Plan:**  
   The program outputs a schedule showing, for each turn when you make a purchase, what you bought. Each output line tells you:
   - The turn number.
   - How many items were bought that turn.
   - The IDs of the resources purchased.

## In Short

- **The Challenge:**  
  Manage a limited budget to power buildings over many rounds by buying energy resources with different costs, lifespans, and power outputs.

- **The Solver:**  
  A program that simulates each round, checks if you're meeting your power requirements, and decides which resources to buy to maximize profit without overspending. It then outputs a simple list of your buying decisions turn by turn.

For the full details on the game rules (including special effects and resource interactions), please refer to [Green_Revolution_Game.pdf](Green_Revolution_Game.pdf).

## About the Solver Code:
This Python-based solver uses a heuristic, turn-by-turn simulation approach to tackle the Green Revolution Game Challenge. Here’s a quick overview of how it works:

1.   **Input Parsing:**
The solver reads an input file containing your starting budget, resource definitions, and turn specifications. It extracts details such as activation and maintenance costs, resource lifespans, and the profit rules for each turn.

2.   **Turn Simulation:**
For each turn, the solver simulates the active resources to determine how many buildings are being powered and calculates the associated maintenance costs. If the production is below the minimum required (TM), it makes purchase decisions.

3.   **Purchase Decisions:**
When production is insufficient, the solver uses a greedy strategy to buy the resource with the best efficiency (defined by the ratio of buildings powered per cost) that is affordable. These purchases boost the overall production for the turn.

4.   **Budget Update & Profit Calculation:**
The solver calculates the turn’s profit using the formula:
Profit =min(Total Powered,𝑇𝑋)×𝑇𝑅
and updates the budget by subtracting activation and maintenance costs and adding the profit.

5.   **Output Generation:**
Only turns where purchases are made are recorded. The output file lists the turn number, the number of resources bought, and the IDs of those resources.

This simple, greedy approach ensures that the solver consistently meets the minimum requirements each turn while trying to maximize profit without overspending. Although heuristic in nature, it produces a valid purchase schedule under the challenge’s constraints.


## How to Run the Solver

1. **Prepare your input file:**  
   Edit `input.txt` with the instance you wish to solve.

2. **Run the solver:**  
-For example, in a Unix-like shell or CMD:
   ```bash
   python3 solver.py < input.txt > output.txt
-In PowerShell, you might use:
   ```bash
  Get-Content input.txt | python3 solver.py > output.txt
```
-Check the output:
The file output.txt will contain your purchase schedule. Each line is formatted as:



