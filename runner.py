from game import Game
from agents import RandomAgent, MonteCarloAgent, MinMaxAgent

class MatchManager:
    def __init__(self):
        self.score = {'X': 0, 'O': 0, 'empates': 0}
        self.games_played = 0

    def play_game(self, agente_X, agente_O, humano_joga='X', mostrar=True):
        game = Game()
        while not game.is_terminal():
            player = game.current_player
            if player == humano_joga:
                # Jogada humana
                while True:
                    try:
                        print("\nSeu turno! Digite linha e coluna (0, 1 ou 2).")
                        linha = int(input("Linha: "))
                        coluna = int(input("Coluna: "))
                        if (linha, coluna) in game.get_valid_moves():
                            move = (linha, coluna)
                            break
                        else:
                            print("❌ Movimento inválido, tente novamente.")
                    except ValueError:
                        print("❌ Entrada inválida, use números 0, 1 ou 2.")
            else:
                # Jogada do agente
                agente = agente_X if player == 'X' else agente_O
                move = agente.select_move(game, player)
                print(f"\n🤖 IA ({player}) jogou {move}")

            game.apply_move(move)
            if mostrar:
                game.print_board()

        winner = game.get_winner()
        self.games_played += 1

        if winner:
            print(f"\n🏆 Vitória do {winner}!")
            self.score[winner] += 1
        else:
            print("\n🤝 Empate!")
            self.score['empates'] += 1

        print(f"\nPlacar: {self.score}")
        return winner


if __name__ == "__main__":
    manager = MatchManager()

    while True:
        print("\nSelecione o modo de dificuldade:")
        print("1 - Fácil (Random)")
        print("2 - Intermediário (Monte Carlo)")
        print("3 - Difícil (Min-Max)")

        while True:
            modo = input("Modo (1, 2 ou 3): ").strip()
            if modo == "1":
                agente = RandomAgent()
                print("🔹 Modo selecionado: Fácil (Random)\n")
                break
            elif modo == "2":
                agente = MonteCarloAgent()
                print("🔹 Modo selecionado: Intermediário (Monte Carlo)\n")
                break
            elif modo == "3":
                agente = MinMaxAgent()
                print("🔹 Modo selecionado: Difícil (Min-Max)\n")
                break
            else:
                print("❌ Opção inválida! Escolha 1, 2 ou 3.")

        lado = input("Você quer ser X ou O? ").strip().upper()
        if lado not in ['X', 'O']:
            lado = 'X'

        if lado == 'X':
            manager.play_game(agente_X=None, agente_O=agente, humano_joga='X')
        else:
            manager.play_game(agente_X=agente, agente_O=None, humano_joga='O')

        novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if novamente != 's':
            print("\n🏁 Encerrando o jogo. Até a próxima!")
            break