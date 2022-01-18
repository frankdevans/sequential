from typing import Tuple
from dataclasses import dataclass
from sly.lex import Token

from sequential.types import clause


@dataclass(frozen = True)
class BaseClauseBag:
	
	clause : clause
	tokens : Tuple[Token]


	@property
	def n_tokens(self) -> int: return len(self.tokens)

	def sql(self, carryover:dict) -> str:
		xm = 'This is the base class, and does not transpile to SQL. Something is wrong.'
		raise ValueError(xm)