from pipeline import Flow
from expand_op import ExpandOp
from reduce_op import ReduceOp

class ExpandReduceFlow(Flow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.expand_op = ExpandOp()
        self.reduce_op = ReduceOp()

    def run(self, input_node):
        expand_1, expand_2 = self.expand_op.execute(input_node)
        reduce_1 = self.reduce_op.execute(expand_1, expand_2)
        return reduce_1
