import unittest
from expand_op import ExpandOp
from node import Node

class TestExpandOp(unittest.TestCase):
    def test_expand_op(self):

        input_node = Node("root", {"1": "2", "3": "4", "5": "6", "7": "8"})
        expand_op = ExpandOp()


        expand_1, expand_2 = expand_op.execute(input_node)


        self.assertEqual(expand_1.value_dict, {"1": "2", "3": "4"})
        self.assertEqual(expand_2.value_dict, {"5": "6", "7": "8"})

if __name__ == '__main__':
    unittest.main()
