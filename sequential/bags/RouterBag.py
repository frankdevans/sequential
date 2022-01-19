from typing import List
from dataclasses import dataclass
from sequential.types import _TOKENS

from ..types import clause
from .clause import ClauseBag

from .clause import generate_clause_bag
from ..assemblers.StatementAssembler import StatementAssembler



@dataclass(frozen = True)
class _ClauseSpan:

	clause : clause
	idx_mark : int
	idx_end : int
	tokens : _TOKENS


@dataclass(frozen = True)
class RouterBag():

	tokens : _TOKENS

	_clauses = {f"C_{name}" : member for (name,member) in clause.__members__.items()}


	@property
	def n_tokens(self)-> int: return len(self.tokens)

	def get_token_clause(self, idx:int) -> clause:
		token = self.tokens[idx]
		return self._clauses.get(token.type, clause.NULL)

	@property
	def clause_spans(self) -> List[_ClauseSpan]:
		marks = [
			idx for (idx, token) in enumerate(self.tokens)
			if (token.type in self._clauses)
		]
		ends = [*marks[1:], self.n_tokens]
		spans = [
			_ClauseSpan(
				clause = self.get_token_clause(idx = mark),
				idx_mark = mark,
				idx_end = end,
				tokens = self.tokens[(mark + 1) : end]
			) for (mark,end) in zip(marks, ends)
		]
		return spans

	@property
	def clause_sequence(self) -> List[clause]: 
		return [span.clause for span in self.clause_spans]

	@property
	def clause_bags(self) -> List[ClauseBag]:
		return [
			generate_clause_bag(clause = span.clause, tokens = span.tokens)
			for span in self.clause_spans
		]
	
	@property
	def handoff_assembler(self) -> StatementAssembler:
		field_clauses = {clause.WITH, clause.QUERY, clause.UNION}
		
		bags = self.clause_bags
		bags_with = [bag for bag in bags if (bag.clause is clause.WITH)]
		bags_query = [bag for bag in bags if (bag.clause is clause.QUERY)]
		bags_union = [bag for bag in bags if (bag.clause is clause.UNION)]
		bags_clauses = [bag for bag in bags if not (bag.clause in field_clauses)]

		params = {
			'CLAUSES' : bags_clauses,
			'UNION' : bags_union,
			**({'WITH':bags_with[0]} if (len(bags_with) > 0) else {}),
			**({'QUERY':bags_query[0]} if (len(bags_query) > 0) else {}),
		}
		
		assembler = StatementAssembler(**params)
		return assembler