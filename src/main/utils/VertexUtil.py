import functools
from src.main.models.Vertex import Vertex

""" Util operations for vertices """
class VertexUtils:

    @staticmethod
    def getMaxXVertex(vertices:list[Vertex]):
        return functools.reduce(lambda a, b : (a if a.x > b.x else b), vertices, Vertex(0, 0))

    @staticmethod
    def getMaxYVertex(vertices:list[Vertex]):
        return functools.reduce(lambda a, b : (a if a.y > b.y else b), vertices, Vertex(0, 0))
    
    @staticmethod
    def existVertex(vertices:list[Vertex], x:int, y:int):
        return any((vertex.x == x and vertex.y == y) for vertex in vertices)
    
    def existsAnSqare(self, vertex:Vertex, sqareLength:int, vertices:list[Vertex]):
        sqareXLength, sqareYLength = vertex.x + sqareLength, vertex.y + sqareLength
        existHorizontal = self.existVertex(vertices, sqareXLength, vertex.y)
        existVertical = self.existVertex(vertices, vertex.x, sqareYLength)
        existDiagonal = self.existVertex(vertices, sqareXLength, sqareYLength)
        return existHorizontal and existVertical and existDiagonal

    def countSqaresPerVertex(self, vertex:Vertex, maxX:int, maxY:int, vertices:list[Vertex]):
        maxVertexSqare = maxX if maxX <= maxY else maxY
        sqareMatches = list(map(lambda i: self.existsAnSqare(vertex, i, vertices), range(1, maxVertexSqare + 1)))
        return functools.reduce(lambda a, b : a + b, list(map(lambda match: 1 if match else 0, sqareMatches)), 0)

    def countSqares(self, vertices:list[Vertex]):
        maxX = self.getMaxXVertex(vertices).x
        maxY = self.getMaxYVertex(vertices).y
        sqaresPerVertex = list(map(lambda it: self.countSqaresPerVertex(it, maxX, maxY, vertices), vertices))

        return functools.reduce(lambda a, b : a + b or 0, sqaresPerVertex, 0)
