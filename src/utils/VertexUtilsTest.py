from src.models.Vertex import Vertex
from src.utils.VertexUtils import VertexUtils
import unittest

class TestVertexUtils(unittest.TestCase):

    def testCountNoSqares(self):
        vertices = [Vertex(0, 0)]
        self.assertEqual(VertexUtils().countSqares(vertices), 0)

    def testCountOneSqare(self):
        vertices = [Vertex(0, 0), Vertex(0, 1), Vertex(1, 0), Vertex(1, 1)]
        self.assertEqual(VertexUtils().countSqares(vertices), 1)

    def testCountSqaresWithRepeatedVertices(self):
        vertices = [Vertex(0, 0), Vertex(0, 0), Vertex(1, 0), Vertex(1, 1)]
        self.assertEqual(VertexUtils().countSqares(vertices), 0)

    def testCountSqareWithRectangle(self):
        vertices = [Vertex(0, 0), Vertex(0, 1), Vertex(2, 0), Vertex(1, 2)]
        self.assertEqual(VertexUtils().countSqares(vertices), 0)

    def testCountTwoSqares(self):
        vertices = [Vertex(0, 0), Vertex(0, 1), Vertex(1, 0), Vertex(1, 1), Vertex(0, 2), Vertex(2, 0), Vertex(2, 2)]
        self.assertEqual(VertexUtils().countSqares(vertices), 2)

    def testCountNoVertices(self):
        vertices = []
        self.assertEqual(VertexUtils().countSqares(vertices), 0)
