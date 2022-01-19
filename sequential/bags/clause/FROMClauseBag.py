from sequential.types import _TOKENS
from .BaseClauseBag import BaseClauseBag



class FROMClauseBag(BaseClauseBag):

	_ignore = {'LINE_BREAK'}
	
	@property
	def tokens_render(self) -> _TOKENS:
		return tuple([
			token for token in self.tokens 
			if (token.type not in self._ignore)
		])
	
	def sql(self, carryover:dict) -> str:
		render_tokens = [
			'FROM',
			*[token.value for token in self.tokens_render]
		]
		quark = ' '.join(render_tokens)
		return quark