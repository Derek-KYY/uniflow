class ReduceOp(Op):
    def __init__(self, merge_function=None):
        self.merge_function = merge_function

    def execute(self, expand_1: Node, expand_2: Node) -> Node:

        if self.merge_function:
            return self.merge_function(expand_1, expand_2)


        merged_value_dict = {**expand_1.value_dict, **expand_2.value_dict}


        reduce_1 = Node(name="reduce_1", value_dict=merged_value_dict)

        return reduce_1
