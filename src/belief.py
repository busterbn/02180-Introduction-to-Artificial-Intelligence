class Belief:
    def __init__(self, formula, priority=0, source='unknown', seniority=None):
        self.f = formula
        self.priority = priority
        self.source = source
        # Seniority score: initial beliefs default to 1.0, new ones decay externally
        self.seniority = seniority if seniority is not None else 1.0
        self.usage_count = 0
        self.complexity = self._compute_complexity()
        # Dynamic metrics placeholders; update via methods
        self.strength = 0
        self.consistency_contrib = 0

    def __repr__(self):
        return (f"Rank={self.rank():.2f} "
                f"[Pri={self.priority}] "
                f"Src={self.source} "
                f"Sen={self.seniority:.2f} "
                f"Use={self.usage_count} "
                f"Comp={self.complexity} "
                f"Str={self.strength} "
                f"Cons={self.consistency_contrib} "
                f"– {self.f}")

    def _compute_complexity(self):
        # simple count of logical operators in the formula string
        s = str(self.f)
        return sum(1 for c in s if c in ['&', '|', '~', '>', '<', '=', '!'])

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
        return seniority_score * 0.4 + source_score * 0.4 + complexity_score * 0.2

    def compute_dynamic_rank(self):
        # use placeholders; in practice update strength and consistency first
        return self.strength * 0.5 + self.usage_count * 0.3 + self.consistency_contrib * 0.2

    def rank(self):
        return self.compute_static_rank() + self.compute_dynamic_rank()