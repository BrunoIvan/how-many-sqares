from src.store.VertexStore import VertexStore
import unittest

class VertexStoreTest(unittest.TestCase):

    def testVerticesListDefined(self):
        self.assertIsNotNone(VertexStore().getVertices())
