def get_computer_move(their_moves, your_moves):
    r_count = their_moves.count('r')
    s_count = their_moves.count('s')
    p_count = their_moves.count('p')
    if r_count <= s_count and r_count <= p_count:
        your_moves.append('p')
        return 'p'
    elif p_count <= r_count and p_count <= s_count:
        your_moves.append('s')
        return 's'
    elif s_count <= r_count and s_count <= p_count:
        your_moves.append('r')
        return 'r'
    

def history(their_moves, your_moves):
    print(format('PLayer Moves:', '<20') + 'Computer Moves:' + format('\n-----', '<21') + '-----')
    i = 0
    for move in their_moves:
        print(format(move, '<20') + your_moves[i])
        i += 1
