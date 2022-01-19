from typing import List
from dataclasses import dataclass
from sequential.types import _TOKENS

from ..types import clause
from .clause import ClauseBag

from .clause import generate_clause_bag
from ..assemblers.QueryAssembler import QueryAssembler



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
	def temp(self):
		bags = self.clause_bags
		for bag in bags: print(bag.clause, bag.n_tokens)

		params = {bag.clause.value : bag for bag in self.clause_bags}
		query = QueryAssembler(**params)
		print(query.sql)



		return