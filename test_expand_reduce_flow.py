import unittest
from expand_reduce_flow import ExpandReduceFlow
from node import Node

class TestExpandReduceFlow(unittest.TestCase):
    def test_expand_reduce_flow(self):

        input_node = Node("root", {"1": "2", "3": "4", "5": "6", "7": "8"})
        flow = ExpandReduceFlow()


        output_node = flow.run(input_node)


        self.assertEqual(output_node.value_dict, {"1": "2", "3": "4", "5": "6", "7": "8"})

if __name__ == '__main__':
    unittest.main()
