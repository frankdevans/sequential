from sequential.types import _TOKENS
from .BaseClauseBag import BaseClauseBag



class NULLClauseBag(BaseClauseBag):
	
	def sql(self, carryover:dict) -> str: return ''