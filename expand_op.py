class ExpandOp(Op):
    def __init__(self, split_function=None):
        self.split_function = split_function

    def execute(self, root: Node) -> Tuple[Node, Node]:

        if self.split_function:
            return self.split_function(root)


        value_dict = root.value_dict
        n = len(value_dict)
        keys = list(value_dict.keys())


        value_dict_1 = {k: value_dict[k] for k in keys[:n // 2]}
        value_dict_2 = {k: value_dict[k] for k in keys[n // 2:]}


        expand_1 = Node(name="expand_1", value_dict=value_dict_1)
        expand_2 = Node(name="expand_2", value_dict=value_dict_2)

        return expand_1, expand_2
