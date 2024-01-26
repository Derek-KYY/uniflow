import unittest
from reduce_op import ReduceOp
from node import Node

class TestReduceOp(unittest.TestCase):
    def test_reduce_op(self):

        expand_1 = Node("expand_1", {"1": "2", "3": "4"})
        expand_2 = Node("expand_2", {"5": "6", "7": "8"})
        reduce_op = ReduceOp()


        reduce_1 = reduce_op.execute(expand_1, expand_2)


        self.assertEqual(reduce_1.value_dict, {"1": "2", "3": "4", "5": "6", "7": "8"})

if __name__ == '__main__':
    unittest.main()
