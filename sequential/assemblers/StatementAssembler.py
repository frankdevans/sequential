from typing import Union, List
from dataclasses import dataclass
from ..bags.clause import (
	ClauseBag,
	NULLClauseBag,
	UNIONClauseBag,
	WITHClauseBag,
	QUERYClauseBag,
)

from sequential.types import clause


FALLBACK = NULLClauseBag(clause = clause.NULL, tokens = tuple())


@dataclass(frozen = True)
class StatementAssembler:

	CLAUSES : List[ClauseBag]
	UNION : List[UNIONClauseBag]
	WITH : Union[WITHClauseBag, NULLClauseBag] = FALLBACK
	QUERY : Union[QUERYClauseBag, NULLClauseBag] = FALLBACK


	@property
	def has_cte(self) -> bool: return (self.WITH.n_tokens > 0)

	@property
	def has_unions(self) -> bool: return (len(self.UNION) > 0)