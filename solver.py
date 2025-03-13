#!/usr/bin/env python3
import sys

# Définition d'une classe pour représenter une ressource
class Resource:
    def __init__(self, id, RA, RP, RW, RM, RL, RU, RTr, RE=None):
        self.id = id      # Identifiant de la ressource
        self.RA = RA      # Coût d'activation
        self.RP = RP      # Coût périodique (maintenance)
        self.RW = RW      # Nombre de tours d'activité consécutifs
        self.RM = RM      # Nombre de tours de repos requis après activité
        self.RL = RL      # Durée de vie totale (en tours)
        self.RU = RU      # Nombre de bâtiments alimentés par tour actif
        self.RTr = RTr    # Type d'effet (A, B, C, D, E, X)
        self.RE = RE      # Intensité de l'effet, si applicable

# Classe pour représenter un tour de jeu
class Turn:
    def __init__(self, TM, TX, TR):
        self.TM = TM  # Seuil minimum de bâtiments alimentés
        self.TX = TX  # Seuil maximum (plafond) pour le calcul du profit
        self.TR = TR  # Profit unitaire par bâtiment alimenté

def parse_input():
    """
    Lit l’instance depuis sys.stdin.
    Format attendu :
      - Ligne 1 : D R T
      - Lignes 2 à R+1 : description des ressources, 
           format : RI RA RP RW RM RL RU RTr [RE]
      - Lignes R+2 à R+T+1 : description des tours,
           format : TM TX TR
    """
    lines = sys.stdin.read().strip().splitlines()
    if not lines:
        return None, None, None
    header = lines[0].split()
    D = int(header[0])
    R = int(header[1])
    T = int(header[2])
    resources = []
    for i in range(1, R+1):
        parts = lines[i].split()
        rid = int(parts[0])
        RA = int(parts[1])
        RP = int(parts[2])
        RW = int(parts[3])
        RM = int(parts[4])
        RL = int(parts[5])
        RU = int(parts[6])
        RTr = parts[7]
        RE = int(parts[8]) if len(parts) > 8 else None
        resources.append(Resource(rid, RA, RP, RW, RM, RL, RU, RTr, RE))
    turns = []
    for i in range(R+1, R+1+T):
        parts = lines[i].split()
        TM = int(parts[0])
        TX = int(parts[1])
        TR = int(parts[2])
        turns.append(Turn(TM, TX, TR))
    return D, resources, turns

def simulate_game(D, resources, turns):
    """
    Simule le jeu tour par tour de façon simplifiée.
    L'approche ici est heuristique :
      - À chaque tour, on calcule le nombre total de bâtiments alimentés par les ressources "actives"
      - Si ce total est inférieur au seuil minimum (TM) du tour, on tente d'acheter une ressource
        parmi celles abordables (choix basé sur le ratio RU/RA).
      - On calcule le profit du tour (si TM est atteint) en utilisant min(total alimenté, TX)*TR.
      - On met à jour le budget en ajoutant le profit et en soustrayant les coûts de maintenance.
    
    Pour simplifier, une fois achetée, une ressource est considérée active pour tous les tours suivants.
    Le planning d’achats est enregistré sous forme d’une liste de tuples (tour, [list of resource IDs achetées]).
    """
    purchase_schedule = []
    current_budget = D
    active_resources = []  # Liste des ressources actuellement actives
    for t, turn in enumerate(turns):
        # Calculer le nombre total de bâtiments alimentés et le coût de maintenance ce tour
        buildings_fed = sum(r.RU for r in active_resources)
        maintenance_cost = sum(r.RP for r in active_resources)
        
        # Si le seuil minimum n'est pas atteint, tenter d'acheter une ressource rentable
        if buildings_fed < turn.TM:
            candidate = None
            best_ratio = 0
            for r in resources:
                if r.RA <= current_budget:
                    ratio = r.RU / r.RA if r.RA > 0 else 0
                    if ratio > best_ratio:
                        best_ratio = ratio
                        candidate = r
            if candidate:
                # Achat d'une copie de la ressource candidate
                current_budget -= candidate.RA
                active_resources.append(candidate)
                purchase_schedule.append((t, [candidate.id]))
                # Mise à jour immédiate des compteurs
                buildings_fed += candidate.RU
                maintenance_cost += candidate.RP
        
        # Calcul du profit : si le seuil minimum est atteint, le profit = min(total alimenté, TX) * TR
        if buildings_fed >= turn.TM:
            profit = min(buildings_fed, turn.TX) * turn.TR
        else:
            profit = 0
        
        # Mise à jour du budget : profit moins le coût de maintenance
        current_budget += profit - maintenance_cost

        # Pour suivi pédagogique (optionnel) : affichez l'état du tour
        # print(f"Turn {t}: Budget={current_budget}, Buildings fed={buildings_fed}, Profit={profit}, Maintenance={maintenance_cost}")

    return purchase_schedule

def main():
    D, resources, turns = parse_input()
    if D is None:
        return
    schedule = simulate_game(D, resources, turns)
    # Affichage du planning d’achats au format requis : "t R_t RI1 RI2 ..."
    for turn, purchases in schedule:
        print(f"{turn} {len(purchases)} " + " ".join(str(rid) for rid in purchases))

if __name__ == "__main__":
    main()
