import unittest
from src.main.store.VertexStore import VertexStore

class VertexStoreTest(unittest.TestCase):

    def testVerticesListDefined(self):
        self.assertIsNotNone(VertexStore().getVertices())
