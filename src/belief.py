from formula_ast import Not, And, Or, Implies, Bicond

FACTOR_SENIORITY = 0.5
FACTOR_SOURCE = 0.5
FACTOR_COMPLEXITY = 0.3

class Belief:
    def __init__(self, formula, source='unknown', seniority=None):
        self.f = formula
        # Static ranking
        self.seniority = seniority if seniority is not None else 1.0
        self.trustworthiness = source
        self.complexity = self._compute_complexity()
        self.static_rank = self.compute_static_rank()

    def __repr__(self):
        return (f"Priority: {self.rank():.2f} |"
                # f"Sen={self.seniority:.2f} "
                # f"trustworthiness={self.trustworthiness} "
                # f"complexity={self.complexity:.2f} "
                # f"static_rank={self.static_rank:.2f} "
                f" {self.f}")

    def _compute_complexity(self):
        """
        Count logical operators by traversing the formula AST.
        """
        def count_ops(node):
            # Negation node counts as one operator + recurse
            if isinstance(node, Not):
                return 1 + count_ops(node.f)
            # Binary operators count as one + recurse on both sides
            if isinstance(node, (And, Or, Implies, Bicond)):
                return 1 + count_ops(node.left) + count_ops(node.right)
            # Atom or any other leaf: no operators here
            return 0

        return count_ops(self.f)

    def compute_static_rank(self):
        trust_map = {'observation': 1.0, 'heard': 0.5}
        source_score = trust_map.get(self.trustworthiness, 0.1)
        return self.seniority * FACTOR_SENIORITY \
                + source_score * FACTOR_SOURCE \
                + self.complexity * FACTOR_COMPLEXITY

    def rank(self):
        self.priority = self.compute_static_rank()
        return self.priority