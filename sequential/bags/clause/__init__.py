from sequential.types import _TOKENS
from sequential.types import clause
from .BaseClauseBag import BaseClauseBag as ClauseBag

from .NULLClauseBag import NULLClauseBag
from .FROMClauseBag import FROMClauseBag
from .SELECTClauseBag import SELECTClauseBag

from .WHEREClauseBag import WHEREClauseBag
from .LIMITClauseBag import LIMITClauseBag
from .ORDERClauseBag import ORDERClauseBag
from .GROUPClauseBag import GROUPClauseBag
from .HAVINGClauseBag import HAVINGClauseBag
from .CALCClauseBag import CALCClauseBag

from .UNIONClauseBag import UNIONClauseBag
from .WITHClauseBag import WITHClauseBag
from .QUERYClauseBag import QUERYClauseBag



BAGS = {
	clause.FROM : FROMClauseBag,
	clause.SELECT : SELECTClauseBag,
	clause.WHERE : WHEREClauseBag,

	clause.LIMIT : LIMITClauseBag,
	clause.ORDER : ORDERClauseBag,
	clause.GROUP : GROUPClauseBag,
	clause.HAVING : HAVINGClauseBag,
	clause.CALC : CALCClauseBag,

	clause.UNION : UNIONClauseBag,
	clause.WITH : WITHClauseBag,
	clause.QUERY : QUERYClauseBag,
}


def generate_clause_bag(clause:clause, tokens:_TOKENS) -> ClauseBag:
	return BAGS.get(clause, ClauseBag)(clause=clause, tokens=tokens)