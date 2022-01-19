from typing import Union
from dataclasses import dataclass
from ..bags.clause import (
	NULLClauseBag,
	SELECTClauseBag,
	FROMClauseBag,
	
	WHEREClauseBag,
	LIMITClauseBag,
	ORDERClauseBag,
	GROUPClauseBag,
	HAVINGClauseBag,
	CALCClauseBag,
)

from sequential.types import clause


FALLBACK = NULLClauseBag(clause = clause.NULL, tokens = tuple())


@dataclass(frozen = True)
class QuarkAssembler:

	SELECT : SELECTClauseBag
	FROM : FROMClauseBag

	WHERE : Union[WHEREClauseBag, NULLClauseBag] = FALLBACK
	LIMIT : Union[LIMITClauseBag, NULLClauseBag] = FALLBACK
	ORDER : Union[ORDERClauseBag, NULLClauseBag] = FALLBACK
	GROUP : Union[GROUPClauseBag, NULLClauseBag] = FALLBACK
	HAVING : Union[HAVINGClauseBag, NULLClauseBag] = FALLBACK
	CALC : Union[CALCClauseBag, NULLClauseBag] = FALLBACK

	
	@property
	def sql(self) -> str:
		# TODO: resolve how the calc props are going to be handed off
		
		queue = [
			self.SELECT.sql(carryover = {}),
			self.FROM.sql(carryover = {}),
			self.WHERE.sql(carryover = {}),
		]
		query = '\n'.join(queue)
		return query