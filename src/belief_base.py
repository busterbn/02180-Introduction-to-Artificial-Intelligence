# --- 5. Belief base ---------------------------------------------------------
# BeliefBase supports expansion, contraction, and AGM revision

from belief import Belief
from formula_ast import Not
from cnf import to_cnf
from resolution import pl_resolution

SENIORITY_DECAY_FACTOR = 0.95

class BeliefBase:
    # AGM expansion: add new belief without checking consistency
    def __init__(self):
        self.beliefs = []  # list of Belief
        self.current_seniority = 1.0 * SENIORITY_DECAY_FACTOR

    # AGM expansion: add new belief without checking consistency
    def expand(self, formula, source='observation', seniority=None):
        """AGM expansion: add new belief with metadata."""
        self.beliefs.append(Belief(formula, source, seniority))
        # self.compute_priorities()

    # AGM contraction: remove lowest-priority beliefs until formula is no longer entailed
    def contract(self, formula):
        """
        Priority‐based contraction: remove low‐priority beliefs
        until formula is no longer entailed.
        """
        # if not entailed, nothing to do
        if not self.entails(formula):
            return
        # sort beliefs ascending by rank
        for b in sorted(self.beliefs, key=lambda B: B.rank()):
            # try removing b
            trial = [x for x in self.beliefs if x is not b]
            if not BeliefBase._entails_list(trial, formula):
                # removing b makes formula no longer entailed: keep it removed
                self.beliefs = trial
                return self.contract(formula)  # might need to remove more
        # if we get here, we couldn't unknot entailment
        # leaving base empty
        self.beliefs = []

    # AGM revision (Levi identity): contract ¬formula then expand formula
    def revise(self, formula, source='expert'):
        """AGM revision: contract ¬formula, then expand."""
        self.contract(Not(formula))
        self.expand(formula, source='expert', seniority=self.current_seniority)

    def entails(self, formula):
        return BeliefBase._entails_list(self.beliefs, formula)
    
    # def compute_priorities(self):
    #     for belief in self.beliefs:
    #         belief.compute_strength(self)
    #         belief.compute_consistency_contrib(self)

    @staticmethod
    def _entails_list(beliefs, formula):
        clauses = []
        for b in beliefs:
            clauses.extend(to_cnf(b.f))
        return pl_resolution(clauses, formula)

    def __repr__(self):
        return "\n".join(repr(b) for b in sorted(self.beliefs, key=lambda B: -B.rank()))
    

    