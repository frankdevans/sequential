from sequential.types import clause
from .BaseClauseBag import BaseClauseBag as ClausBag
from .FROMClauseBag import FROMClauseBag
from .SELECTClauseBag import SELECTClauseBag


BAGS = {
	clause.FROM : FROMClauseBag,
	clause.SELECT : SELECTClauseBag,
}


def generate_clause_bag(clause:clause) -> ClausBag: return BAGS.get(clause, ClausBag)