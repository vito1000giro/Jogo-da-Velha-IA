import random
import copy
import math

class Agent:
    def select_move(self, game, player):
        raise NotImplementedError


# ===========================
# FÁCIL - Jogadas aleatórias
# ===========================

class RandomAgent(Agent):
    def select_move(self, game, player):
        moves = game.get_valid_moves()
        return random.choice(moves)


# ======================================
# INTERMEDIÁRIO - Algoritmo Monte Carlo
# ======================================

class MonteCarloAgent(Agent):
    def __init__(self, simulations=200):
        self.simulations = simulations  # número de simulações por jogada

    def simulate(self, game, player):
        simulated_game = copy.deepcopy(game)
        while not simulated_game.is_terminal():
            moves = simulated_game.get_valid_moves()
            move = random.choice(moves)
            simulated_game.apply_move(move)
        return simulated_game.get_winner()

    def select_move(self, game, player):
        moves = game.get_valid_moves()
        best_move = None
        best_score = -1

        for move in moves:
            wins = 0
            for _ in range(self.simulations):
                simulated_game = copy.deepcopy(game)
                simulated_game.apply_move(move)
                winner = self.simulate(simulated_game, player)
                if winner == player:
                    wins += 1

            win_rate = wins / self.simulations
            if win_rate > best_score:
                best_score = win_rate
                best_move = move

        return best_move


# ============================
# DIFÍCIL - Algoritmo Min-Max 
# ============================

class MinMaxAgent(Agent):
    def select_move(self, game, player):
        """Escolhe a melhor jogada usando o algoritmo Min-Max com poda alfa-beta."""
        best_score = -math.inf
        best_move = None

        for move in game.get_valid_moves():
            new_game = game.copy()
            new_game.apply_move(move)
            score = self.minmax(new_game, False, player, -math.inf, math.inf)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minmax(self, game, is_maximizing, player, alpha, beta):
        # Se o jogo terminou, retorna pontuação final
        if game.is_terminal():
            winner = game.get_winner()
            if winner == player:
                return 1    # vitória
            elif winner is None:
                return 0    # empate
            else:
                return -1   # derrota

        if is_maximizing:
            max_eval = -math.inf
            for move in game.get_valid_moves():
                new_game = game.copy()
                new_game.apply_move(move)
                eval = self.minmax(new_game, False, player, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in game.get_valid_moves():
                new_game = game.copy()
                new_game.apply_move(move)
                eval = self.minmax(new_game, True, player, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval1