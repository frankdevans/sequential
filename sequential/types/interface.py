from enum import Enum


class clause(Enum):

	FROM = 'FROM'
	SELECT = 'SELECT'
	
	WHERE = 'WHERE'
	LIMIT = 'LIMIT'
	ORDER = 'ORDER'
	GROUP = 'GROUP'
	HAVING = 'HAVING'
	CALC = 'CALC'
	
	UNION = 'UNION'
	WITH = 'WITH'
	QUERY = 'QUERY'
	
	NULL = '_'