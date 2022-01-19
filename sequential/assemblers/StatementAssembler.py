from typing import Union, List, Tuple
from dataclasses import dataclass
from ..bags.clause import (
	ClauseBag,
	NULLClauseBag,
	UNIONClauseBag,
	WITHClauseBag,
	QUERYClauseBag,
)

from sequential.types import clause
from .QuarkAssembler import QuarkAssembler


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

	@property
	def break_down_cte(self): pass  # TODO

	@property
	def has_clause_overlap(self)-> bool:
		u_clauses = set([cb.clause.value for cb in self.CLAUSES])
		n_clauses = len(self.CLAUSES)
		return (n_clauses > len(u_clauses))

	@property
	def break_into_quarks(self) -> Tuple[QuarkAssembler]:
		if self.has_clause_overlap:
			xm = 'Not Implemented Yet, stick with the single cases for now.'
			raise NotImplementedError(xm)
		
		params = {bag.clause.value : bag for bag in self.CLAUSES}
		assembler = QuarkAssembler(**params)
		return (assembler,)
	
	@property
	def sql(self) -> str:
		quarks = self.break_into_quarks
		assembled = '\n'.join([quark.sql for quark in quarks])
		return assembled