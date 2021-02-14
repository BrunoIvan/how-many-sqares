import unittest
from VertexStore import VertexStore

class VertexStoreTest(unittest.TestCase):

    def test_VerticesListDefined(self):
        self.assertIsNotNone(VertexStore().getVertices())


if __name__ == '__main__':
    unittest.main()