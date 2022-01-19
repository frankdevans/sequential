from enum import Enum


class clause(Enum):

	FROM = 'FROM'
	SELECT = 'SELECT'
	WHERE = 'WHERE'
	HAVING = 'HAVING'
	LIMIT = 'LIMIT'
	WITH = 'WITH'
	UNION = 'UNION'
	GROUP = 'GROUP'
	ORDER = 'ORDER'
	QUERY = 'QUERY'
	CALC = 'CALC'
	NULL = '_'