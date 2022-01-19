from sequential.types import _TOKENS
from sequential.types import clause
from .BaseClauseBag import BaseClauseBag as ClauseBag
from .FROMClauseBag import FROMClauseBag
from .SELECTClauseBag import SELECTClauseBag


BAGS = {
	clause.FROM : FROMClauseBag,
	clause.SELECT : SELECTClauseBag,
}


def generate_clause_bag(clause:clause, tokens:_TOKENS) -> ClauseBag:
	return BAGS.get(clause, ClauseBag)(clause=clause, tokens=tokens)