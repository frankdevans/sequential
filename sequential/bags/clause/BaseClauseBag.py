from sequential.types import _TOKENS
from dataclasses import dataclass

from sequential.types import clause


@dataclass(frozen = True)
class BaseClauseBag:
	
	clause : clause
	tokens : _TOKENS


	@property
	def print_tokens(self) -> None:
		for token in self.tokens: print(token)
		return
	
	@property
	def n_tokens(self) -> int: return len(self.tokens)


	def sql(self, carryover:dict) -> str:
		xm = 'This is the base class, and does not transpile to SQL. Something is wrong.'
		raise ValueError(xm)