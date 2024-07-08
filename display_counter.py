def display_score(total_score, NUM_OF_ROUNDS):
    """
        This function calculates and displays the number of games played, won, and lost.
    
        Parameters:
        total_score (int): The total score of the player, equivalent to the number of rounds won.
        NUM_OF_ROUNDS (int): The total number of rounds played.
    
        Returns:
        A tuple containing the total score, the number of rounds won, and the number of rounds lost.
    """
    rounds_won = total_score
    rounds_lost = NUM_OF_ROUNDS - total_score

    print("+------------------+-----------+------------+")
    print("|   Games Played   | Games Won | Games Lost |")
    print("+------------------+-----------+------------+")
    print(f"|      {NUM_OF_ROUNDS:^6}      |   {rounds_won:^5}   |    {rounds_lost:^5}   |")
    print("+------------------+-----------+------------+")

    return total_score, rounds_won, rounds_lost

