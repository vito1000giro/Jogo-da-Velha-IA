from game import Game

def test_vitoria_linha():
    g = Game()
    g.board = [['X','X','X'],['O',' ','O'],[' ',' ',' ']]
    assert g.get_winner() == 'X'

def test_empate():
    g = Game()
    g.board = [['X','O','X'],['O','X','O'],['O','X','O']]
    assert g.is_terminal()
    assert g.get_winner() is None