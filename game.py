import copy

class Game:
    def __init__(self):
        # Tabuleiro 3x3: ' ' vazio, 'X' ou 'O'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Jogador atual: 'X' começa por padrão
        self.current_player = 'X'

    # --- cópias do estado (usadas por MinMax e MonteCarlo) ---
    def copy(self):
        """Retorna uma cópia profunda do objeto Game (compatível com agentes)."""
        return copy.deepcopy(self)

    def clone(self):
        """Alias para copy() — alguns trechos usam clone() em vez de copy()."""
        return self.copy()

    # --- movimentos e validações ---
    def get_valid_moves(self):
        """Retorna lista de tuplas (linha, coluna) disponíveis."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def apply_move(self, move):
        """
        Aplica um movimento (i, j) no tabuleiro e altera current_player.
        Espera-se que o caller tenha verificado que o movimento é válido.
        """
        i, j = move
        if self.board[i][j] != ' ':
            raise ValueError(f"Posição {move} já ocupada")
        self.board[i][j] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        """Desfaz o último movimento (útil para MinMax que usa apply/undo)."""
        i, j = move
        self.board[i][j] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    # --- fim de jogo e vencedor ---
    def get_winner(self):
        """
        Retorna 'X' ou 'O' se houver vencedor, ou None caso contrário.
        Não diferencia empate — empate é detectado pelo is_terminal + nenhum vencedor.
        """
        # Checa linhas
        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

        # Checa colunas
        for j in range(3):
            if self.board[0][j] != ' ' and self.board[0][j] == self.board[1][j] == self.board[2][j]:
                return self.board[0][j]

        # Diagonais
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def is_terminal(self):
        """
        Retorna True se o jogo acabou (vitória ou empate).
        Empate quando não há movimentos válidos e get_winner() é None.
        """
        if self.get_winner() is not None:
            return True
        if len(self.get_valid_moves()) == 0:
            return True
        return False

    # --- utilitários de exibição ---
    def print_board(self):
        """Imprime o tabuleiro no terminal de forma legível."""
        for i in range(3):
            print(' ' + ' | '.join(self.board[i]))
            if i < 2:
                print('---+---+---')

    def __str__(self):
        """Retorno string para debugging rápido."""
        rows = []
        for i in range(3):
            rows.append(' '.join(self.board[i]))
        return '\n'.join(rows)