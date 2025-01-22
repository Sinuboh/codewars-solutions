progression = {"RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP", "UP": "RIGHT"}
traversal = {"RIGHT": (0, 1), "DOWN": (1, 0), "LEFT": (0, -1), "UP": (-1, 0)}

def add_coord(x, y, dx, dy):
    return x + dx, y + dy

def is_in_bounds(x, y, size):
    return 0 <= x <= size - 1 and 0 <= y <= size - 1

def spiralize(size):
    array = [[0 for i in range(size)] for j in range(size)]
    x, y = 0, 0
    dy, dx  = 0, 1
    currentDirection = "RIGHT"

    array[y][x] = 1

    bumpCounter = 0

    while bumpCounter <= 4:
        dx = traversal[currentDirection][1]
        dy = traversal[currentDirection][0]

        targetCoordinateX, targetCoordinateY = add_coord(x, y, dx, dy)
        extraCoordinateX, extraCoordinateY = add_coord(targetCoordinateX, targetCoordinateY, dx, dy)

        if(not is_in_bounds(targetCoordinateX, targetCoordinateY, size)):
            currentDirection = progression[currentDirection]
            continue

        if(is_in_bounds(extraCoordinateX, extraCoordinateY, size) and array[extraCoordinateY][extraCoordinateX] == 1):
            currentDirection = progression[currentDirection]
            bumpCounter += 1
            continue
        else:
            bumpCounter = 0
        
        upBoundX, upBoundY = add_coord(targetCoordinateX, targetCoordinateY, 0, -1)
        downBoundX, downBoundY = add_coord(targetCoordinateX, targetCoordinateY, 0, 1)
        leftBoundX, leftBoundY = add_coord(targetCoordinateX, targetCoordinateY, -1, 0)
        rightBoundX, rightBoundY = add_coord(targetCoordinateX, targetCoordinateY, 1, 0)

        for boundX, boundY in [(upBoundX, upBoundY), (downBoundX, downBoundY), (leftBoundX, leftBoundY), (rightBoundX, rightBoundY)]:
            if(is_in_bounds(boundX, boundY, size) and not (boundX == x and boundY == y) and array[boundY][boundX] == 1):
                return(array)

        array[targetCoordinateY][targetCoordinateX] = 1

        x, y = targetCoordinateX, targetCoordinateY
    return(array)