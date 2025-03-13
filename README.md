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

For the full details on the game rules (including special effects and resource interactions), please refer to [Gree_Revolution_Game.pdf](Gree_Revolution_Game.pdf).
