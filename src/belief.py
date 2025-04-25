from formula_ast import Not, And, Or, Implies, Bicond

FACTOR_SENIORITY = 0.4
FACTOR_SOURCE = 0.4
FACTOR_COMPLEXITY = 0.2

class Belief:
    def __init__(self, formula, source='unknown', seniority=None):
        self.f = formula
        # Static ranking
        self.source = source
        self.complexity = self._compute_complexity()
        self.seniority = seniority if seniority is not None else 1.0
        self.static_rank = self.compute_static_rank()
        # Dynamic ranking
        self.usage_count = 0
        self.strength = 0
        self.consistency_contrib = 0
        # Now that seniority and other attributes are set, compute initial priority
        self.priority = 0

    def __repr__(self):
        return (f"Rank={self.rank():.2f} "
                f"[Pri={self.priority:.2f}] "
                # f"Src={self.source} "
                f"Sen={self.seniority:.2f} "
                f"Use={self.usage_count} "
                f"Comp={self.complexity} "
                f"Str={self.strength} "
                f"Cons={self.consistency_contrib} "
                f"– {self.f}")

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

    def update_usage(self):
        self.usage_count += 1

    def compute_strength(self, belief_base):
        # placeholder: count how many other beliefs entail this one
        count = 0
        for b in belief_base.beliefs:
            if b is not self and belief_base.entails(self.f):
                count += 1
        self.strength = count
        return self.strength

    def compute_consistency_contrib(self, belief_base):
        # placeholder: 1 if removal causes inconsistency, else 0
        original = belief_base.beliefs
        belief_base.beliefs = [b for b in original if b is not self]
        # check if empty base still consistent (trivially true) – real logic here
        contrib = 0
        # restore
        belief_base.beliefs = original
        self.consistency_contrib = contrib
        return self.consistency_contrib

    def compute_static_rank(self):
        seniority_score = self.seniority
        # source trustworthiness mapping
        trust_map = {'observation': 1.0, 'expert': 0.8, 'hypothesis': 0.5, 'inference': 0.3}
        source_score = trust_map.get(self.source, 0.1)
        # simplicity: fewer operators → higher score
        complexity_score = 1 / (1 + self.complexity)
        # weighted combination
        return seniority_score * FACTOR_SENIORITY \
                + source_score * FACTOR_SOURCE \
                + complexity_score * FACTOR_COMPLEXITY

    def compute_dynamic_rank(self):
        # use placeholders; in practice update strength and consistency first
        return self.strength * 0.5 + self.usage_count * 0.3 + self.consistency_contrib * 0.2

    def rank(self):
        self.priority = self.compute_static_rank() + self.compute_dynamic_rank()
        return self.priority