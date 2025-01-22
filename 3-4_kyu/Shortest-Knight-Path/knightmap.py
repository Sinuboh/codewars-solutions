def knightmap():
    array = [[0 for _ in range(15)] for _ in range(15)]
    array[7][7] = 1

    def is_in_bounds(x, y):
        return 0 <= x <= 14 and 0 <= y <= 14

    for row in array:
        print(row)

    isComplete = False
    currentJumps = 1

    while not isComplete:
        isComplete = True
        for x, item in enumerate(array):
            for y, spot in enumerate(item):
            
                targets = [(y-2, x-1),(y-1, x-2), (y+1, x-2), (y+2, x-1), (y+2, x+1), (y+1, x+2), (y-1, x+2), (y-2, x+1)]
                
                if spot != 0:
                    for target in targets:
                        if is_in_bounds(target[1], target[0]) and spot == currentJumps:
                            if array[target[0]][target[1]] == 0:
                                array[target[0]][target[1]] = currentJumps + 1
                else:
                    isComplete = False
        currentJumps += 1
    return array

for row in knightmap():
    print(row)



