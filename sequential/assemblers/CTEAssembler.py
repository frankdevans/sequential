from dataclasses import dataclass
from ..bags.clause import WITHClauseBag, QUERYClauseBag



@dataclass(frozen = True)
class CTEAssembler:

	WITH : WITHClauseBag
	QUERY : QUERYClauseBag