class Cell:
    """A class for each cell of the grid"""
    def __init__(self, x, y, distance, color, number, fill_by_user):
        self.x = x
        self.y = y
        self.distance = distance
        self.color = color
        self.number = number
        self.fill_by_user = fill_by_user
    def is_over(self, pos):
        x_pos = pos[0]
        y_pos = pos[1]
        if x_pos>self.x and x_pos<self.x+self.distance:
            if y_pos>self.y and y_pos<self.y+self.distance:
                return True 
        return False


a1 = Cell(0, 0, 56, (255,255,255), None, True)
a2 = Cell(56, 0, 56, (255,255,255), None, True)
a3 = Cell(112, 0, 56, (255,255,255), None, True)
a4 = Cell(168, 0, 56, (255,255,255), None, True)
a5 = Cell(224, 0, 56, (255,255,255), None, True)
a6 = Cell(280, 0, 56, (255,255,255), None, True)
a7 = Cell(336, 0, 56, (255,255,255), None, True)
a8 = Cell(392, 0, 56, (255,255,255), None, True)
a9 = Cell(448, 0, 56, (255,255,255), None, True)
b1 = Cell(0, 56, 56, (255,255,255), None, True)
b2 = Cell(56, 56, 56, (255,255,255), None, True)
b3 = Cell(112, 56, 56, (255,255,255), None, True)
b4 = Cell(168, 56, 56, (255,255,255), None, True)
b5 = Cell(224, 56, 56, (255,255,255), None, True)
b6 = Cell(280, 56, 56, (255,255,255), None, True)
b7 = Cell(336, 56, 56, (255,255,255), None, True)
b8 = Cell(392, 56, 56, (255,255,255), None, True)
b9 = Cell(448, 56, 56, (255,255,255), None, True)
c1 = Cell(0, 112, 56, (255,255,255), None, True)
c2 = Cell(56, 112, 56, (255,255,255), None, True)
c3 = Cell(112, 112, 56, (255,255,255), None, True)
c4 = Cell(168, 112, 56, (255,255,255), None, True)
c5 = Cell(224, 112, 56, (255,255,255), None, True)
c6 = Cell(280, 112, 56, (255,255,255), None, True)
c7 = Cell(336, 112, 56, (255,255,255), None, True)
c8 = Cell(392, 112, 56, (255,255,255), None, True)
c9 = Cell(448, 112, 56, (255,255,255), None, True)
d1 = Cell(0, 168, 56, (255,255,255), None, True)
d2 = Cell(56, 168, 56, (255,255,255), None, True)
d3 = Cell(112, 168, 56, (255,255,255), None, True)
d4 = Cell(168, 168, 56, (255,255,255), None, True)
d5 = Cell(224, 168, 56, (255,255,255), None, True)
d6 = Cell(280, 168, 56, (255,255,255), None, True)
d7 = Cell(336, 168, 56, (255,255,255), None, True)
d8 = Cell(392, 168, 56, (255,255,255), None, True)
d9 = Cell(448, 168, 56, (255,255,255), None, True)
e1 = Cell(0, 224, 56, (255,255,255), None, True)
e2 = Cell(56, 224, 56, (255,255,255), None, True)
e3 = Cell(112, 224, 56, (255,255,255), None, True)
e4 = Cell(168, 224, 56, (255,255,255), None, True)
e5 = Cell(224, 224, 56, (255,255,255), None, True)
e6 = Cell(280, 224, 56, (255,255,255), None, True)
e7 = Cell(336, 224, 56, (255,255,255), None, True)
e8 = Cell(392, 224, 56, (255,255,255), None, True)
e9 = Cell(448, 224, 56, (255,255,255), None, True)
f1 = Cell(0, 280, 56, (255,255,255), None, True)
f2 = Cell(56, 280, 56, (255,255,255), None, True)
f3 = Cell(112, 280, 56, (255,255,255), None, True)
f4 = Cell(168, 280, 56, (255,255,255), None, True)
f5 = Cell(224, 280, 56, (255,255,255), None, True)
f6 = Cell(280, 280, 56, (255,255,255), None, True)
f7 = Cell(336, 280, 56, (255,255,255), None, True)
f8 = Cell(392, 280, 56, (255,255,255), None, True)
f9 = Cell(448, 280, 56, (255,255,255), None, True)
g1 = Cell(0, 336, 56, (255,255,255), None, True)
g2 = Cell(56, 336, 56, (255,255,255), None, True)
g3 = Cell(112, 336, 56, (255,255,255), None, True)
g4 = Cell(168, 336, 56, (255,255,255), None, True)
g5 = Cell(224, 336, 56, (255,255,255), None, True)
g6 = Cell(280, 336, 56, (255,255,255), None, True)
g7 = Cell(336, 336, 56, (255,255,255), None, True)
g8 = Cell(392, 336, 56, (255,255,255), None, True)
g9 = Cell(448, 336, 56, (255,255,255), None, True)
h1 = Cell(0, 392, 56, (255,255,255), None, True)
h2 = Cell(56, 392, 56, (255,255,255), None, True)
h3 = Cell(112, 392, 56, (255,255,255), None, True)
h4 = Cell(168, 392, 56, (255,255,255), None, True)
h5 = Cell(224, 392, 56, (255,255,255), None, True)
h6 = Cell(280, 392, 56, (255,255,255), None, True)
h7 = Cell(336, 392, 56, (255,255,255), None, True)
h8 = Cell(392, 392, 56, (255,255,255), None, True)
h9 = Cell(448, 392, 56, (255,255,255), None, True)
i1 = Cell(0, 448, 56, (255,255,255), None, True)
i2 = Cell(56, 448, 56, (255,255,255), None, True)
i3 = Cell(112, 448, 56, (255,255,255), None, True)
i4 = Cell(168, 448, 56, (255,255,255), None, True)
i5 = Cell(224, 448, 56, (255,255,255), None, True)
i6 = Cell(280, 448, 56, (255,255,255), None, True)
i7 = Cell(336, 448, 56, (255,255,255), None, True)
i8 = Cell(392, 448, 56, (255,255,255), None, True)
i9 = Cell(448, 448, 56, (255,255,255), None, True)



cells = [a1,a2,a3,a4,a5,a6,a7,a8,a9,
        b1,b2,b3,b4,b5,b6,b7,b8,b9,
        c1,c2,c3,c4,c5,c6,c7,c8,c9,
        d1,d2,d3,d4,d5,d6,d7,d8,d9,
        e1,e2,e3,e4,e5,e6,e7,e8,e9,
        f1,f2,f3,f4,f5,f6,f7,f8,f9,
        g1,g2,g3,g4,g5,g6,g7,g8,g9,
        h1,h2,h3,h4,h5,h6,h7,h8,h9,
        i1,i2,i3,i4,i5,i6,i7,i8,i9,]

box = [[a1,a2,a3,b1,b2,b3,c1,c2,c3],
[d1,d2,d3,e1,e2,e3,f1,f2,f3],
[g1,g2,g3,h1,h2,h3,i1,i2,i3],
[a4,a5,a6,b4,b5,b6,c4,c5,c6],
[d4,d5,d6,e4,e5,e6,f4,f5,f6],
[g4,g5,g6,h4,h5,h6,i4,i5,i6],
[a7,a8,a9,b7,b8,b9,c7,c8,c9],
[d7,d8,d9,e7,e8,e9,f7,f8,f9],
[g7,g8,g9,h7,h8,h9,i7,i8,i9]]