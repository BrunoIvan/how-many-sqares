from src.main.models.Vertex import Vertex

""" Store of vertices used to represent connected sqares """
class VertexStore():

    def __init__(self):
        self.vertices = [Vertex(0, 0), Vertex(1, 0), Vertex(2, 0), Vertex(3, 0), Vertex(1, 0), Vertex(1, 1), Vertex(1, 2), Vertex(3, 0), Vertex(3, 3)]

    def getVertices(self):
        return self.vertices