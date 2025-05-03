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
        if seniority is None:
            self.beliefs.append(Belief(formula, source, self.current_seniority))
            self.current_seniority *= SENIORITY_DECAY_FACTOR
        else:
            self.beliefs.append(Belief(formula, source, seniority))

    # AGM contraction: remove only beliefs whose removal breaks entailment of formula
    def contract(self, formula):
        # If formula is not currently entailed, nothing to remove
        if not self.entails(formula):
            return
        # Remove only beliefs whose removal breaks entailment of formula
        while self.entails(formula):
            for b in sorted(self.beliefs, key=lambda belief: belief.rank()):
                trial = [x for x in self.beliefs if x is not b]
                # if removing b stops entailing formula, remove it permanently
                if not self._entails_list(trial, formula):
                    print(f"Removing belief: {b.f}")
                    self.beliefs = trial
                    break
            else:
                # no single belief can break entailment: stop to avoid removing unrelated beliefs
                break

    # AGM revision (Levi identity): contract ¬formula then expand formula
    def revise(self, formula, source='expert'):
        """AGM revision: contract ¬formula, then expand."""
        self.contract(Not(formula))
        self.expand(formula, source='source')

    def entails(self, formula):
        return BeliefBase._entails_list(self.beliefs, formula)
    

    @staticmethod
    def _entails_list(beliefs, formula):
        clauses = []
        for b in beliefs:
            clauses.extend(to_cnf(b.f))
        return pl_resolution(clauses, formula)

    def __repr__(self):
        return "\n".join(repr(b) for b in sorted(self.beliefs, key=lambda B: -B.rank()))
    