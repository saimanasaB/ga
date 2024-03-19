import gambit

def run_game(player1_strategy, player2_strategy):
    game = gambit.Game.from_matrix(player1_strategy, player2_strategy)
    solver = gambit.nash.ExternalEnumMixedSolver()
    solution = solver.solve(game)
    return game, solution
