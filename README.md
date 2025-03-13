# TheGreenRevolutionGame
Reply Hack The Code Challenge
# The Green Revolution Game Challenge

Welcome to the **Green Revolution Game Challenge**!

This challenge requires you to manage a limited budget to power buildings over many turns. At each turn, you decide which energy resources to purchase and activate so that you meet a minimum power target and earn profit. 

Each turn is defined by three numbers:
- **TM**: Minimum number of buildings that must be powered.
- **TX**: Maximum number of buildings counted toward profit.
- **TR**: Profit per building powered.

Each available resource has:
- A one-time **activation cost**.
- A **maintenance cost** every active turn.
- A fixed number of active turns before it needs a downtime.
- A **total lifespan** (active plus downtime).
- A capacity to power a set number of buildings per active turn.
- Sometimes a **special effect** that may modify global parameters (such as boosting profit or changing power thresholds).

Your solver reads an input file containing your starting budget, the resources’ parameters, and the turn specifications. It then simulates the game turn by turn: purchasing resources when needed (while keeping within the budget), accounting for maintenance costs, and calculating profit based on the number of powered buildings. The output is a schedule listing, for each turn when purchases occur, the turn number and the IDs of the purchased resources.

For a complete description of the game rules, please see [GameRules.pdf](GameRules.pdf).

## Game Flow Diagram

```mermaid
flowchart TD
    A[Start Turn]
    B[Check Current Budget]
    C[Decide to Purchase Resources?]
    D[Activate Purchased Resources]
    E[Calculate Total Power and Maintenance Costs]
    F{Is Total Power ≥ TM?}
    G[Calculate Profit: min(Power, TX) × TR]
    H[Update Budget]
    I[Proceed to Next Turn]
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F -- Yes --> G
    F -- No --> H
    G --> H
    H --> I
