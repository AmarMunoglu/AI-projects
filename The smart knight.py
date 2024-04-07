import numpy as np

def euclidean(p1,p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calc_moves(position:list):
    '''
    Find out where the knight will land in its 8 options
    '''
    moves = []
    rule = [[2, 1], [2,-1], [-2, 1], [-2,-1], [1, 2], [1,-2], [-1, 2], [-1,-2]]
    for i in rule:
        moves.append([i[0] + position[0],i[1] + position[1]])

    return moves

def valid_moves(position:list):
    '''
    Validate if the moves calculated are valid or in the range of the board
    '''
    moves = calc_moves(position)
    val_pos = []
    for x in moves:
        valid = True
        for j in x:
            if j not in range(0,8):
                valid = False
                break
        if valid is True:
            val_pos.append(x)

    return val_pos

def move_optimal_route(current_pos, target):
    '''
    Find every possible route and take the ones with the least moves.
    Take steps with the least distance and if its divisible by one knight move (distance which is = 2.23606797749979)
    '''
    
    vl_moves = valid_moves(current_pos)
    posNdist = {}

    for move in vl_moves:
        posNdist.update({tuple(move):euclidean(move,target)})

    posNdist = sorted(posNdist.items(), key=lambda x: x[1])
    posNdist = dict(posNdist)
    divisible_moves = {}
    
    for i in posNdist:
        if posNdist[i] % 2.23606797749979 == 0:
            divisible_moves.update({i:posNdist[i]})

    if divisible_moves == {}:
        the_move = list(posNdist.keys())[0]
        the_move = list(the_move)
    else:
        the_move = list(divisible_moves.keys())[0]
        the_move = list(the_move)

    # print(f'Divisible moves: {divisible_moves} \n Non divisible moves: {posNdist} \n The move we take is: {the_move}')
    
    return the_move
    
def main(current, target, counter = 0):
    '''
    Main recursive function that connects everything together
    '''
    if current == target:
        print(counter)
    else:
        the_next_position = move_optimal_route(current, target)
        return main(the_next_position,target,counter=counter+1)

if __name__ == "__main__":
    start_position = [5,2]
    target_position = [2,7]
    main(start_position,target_position)