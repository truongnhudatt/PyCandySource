from random import randint

class Element:
    def __init__(self):
        self.type = randint(1, 6)

    def __str__(self):
        return self.type

    def __repr__(self):
        return f"{self.type}"


class GridElement:
    def __init__(self,args):
        self.args = args
        self.scores = 0
        flag = True
        while flag:
            self.grid = [[Element() for _ in range(8)] for _ in range(8)]
            self.visited = [[0 for _ in range(len(self.grid))]
                            for _ in range(len(self.grid))]
            flag = self.setupgrid()

    def setupgrid(self):
        for i in range(len(self.grid)):
            for y in range(len(self.grid)):
                self.resetVisited()
                self.getPosRemove(i, y, self.getitem(i, y))
                if self.crush(i, y):
                    return True

    def getitem(self, i, y):
        if 0 <= i < len(self.grid) and 0 <= y < len(self.grid):
            return self.grid[i][y].type

    def move(self, i, y, k, l):
        self.swap(i, y, k, l)
        self.scores += self.action(i, y)
        self.scores += self.action(k, l)
        if not self.crush(i, y) and not self.crush(k, l):
            self.swap(i, y, k, l)
        self.scores += self.comboCrush()
        self.args.gui.label_5.setText(str(self.scores))
    def swap(self, i, y, k, l):
        if abs(i - k) + abs(y - l) == 1:
            tmp = self.getitem(i, y)
            self.setitem(i, y, self.getitem(k, l))
            self.setitem(k, l, tmp)

    def resetVisited(self):
        self.visited = [[0 for _ in range(len(self.grid))] for _x in range(len(self.grid))]

    def getPosRemove(self, x, y, value):
        if 0 <= x < 9 and 0 <= y < 9:
            if self.getitem(x, y) == value and self.visited[x][y] == 0:
                self.visited[x][y] = 1
                self.getPosRemove(x + 1, y, value)
                self.getPosRemove(x - 1, y, value)
                self.getPosRemove(x, y + 1, value)
                self.getPosRemove(x, y - 1, value)

    def action(self, i, y):
        self.resetVisited()
        score = 0
        self.getPosRemove(i, y, self.getitem(i, y))
        if self.crush(i, y):
            for point in range(len(self.visited)):
                if self.detectItem(point):
                    count = self.getAllItemRemove(point)
                    if count[1] > 0:
                        for it in reversed(range(count[1])):
                            self.setitem(it + count[0], point, randint(1, 6))
                            self.setitem(it, point, randint(1, 6))
                            score += 1
                    else:
                        for it in range(count[0]):
                            self.setitem(it, point, randint(1, 6))
                            score += 1
        return score

    def crush(self, x, y):
        sumX, sumY = 0, 0
        for p in range(len(self.visited)):
            sumX += self.visited[x][p]
            sumY += self.visited[p][y]
        return sumX > 2 or sumY > 2

    def detectItem(self, x):
        for p in range(len(self.visited)):
            if self.visited[p][x] == 1:
                return True
        return False

    def getAllItemRemove(self, x):
        count = [0, 8]
        for p in range(len(self.visited)):
            if self.visited[p][x] == 1:
                count = [count[0] + 1, min(count[1], p)]
        return count

    def comboCrush(self):
        flag = self.setupgrid()
        count, score = 0, 0
        while flag:
            for i in range(len(self.grid)):
                for y in range(len(self.grid)):
                    k = self.action(i, y)
                    if k > 0:
                        count += 1
                        k *= count
                        score += k
            flag = self.setupgrid()
        return score

    def setitem(self, i, y, value):
        self.grid[i][y].type = value