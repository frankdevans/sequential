from sequential.types import _TOKENS
from .BaseClauseBag import BaseClauseBag



class SELECTClauseBag(BaseClauseBag):

	_ignore = {'LINE_BREAK'}
	_markup = {}
	

	@property
	def tokens_render(self) -> _TOKENS:
		return tuple([
			token for token in self.tokens 
			if (token.type not in self._ignore)
		])
	
	def sql(self, carryover:dict) -> str:
		columns = [
			self._markup.get(token.type, token.value)
			for token in self.tokens_render
		]
		quark = f"SELECT {' '.join(columns)}"
		return quark