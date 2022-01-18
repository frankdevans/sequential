from sly import Lexer



class SequentialLexer(Lexer):
	tokens = {
		C_FROM, C_SELECT, C_WHERE, C_HAVING, C_LIMIT, C_WITH, C_UNION, 
		C_GROUP, C_ORDER, C_QUERY, C_CALC,
		OP_DISTINCT, OP_INSPECT, OP_CASE, OP_ALIAS_BIND, OP_YIELDS,
		F_TERNARY,
		LINE_BREAK, COMMA, PASSTHROUGH,
	}

	ignore = ' \t'


	# ----- Token Rules: Clause Designators -----
	C_FROM = r'FROM:|from:'
	C_SELECT = r'SELECT:|select:'
	C_WHERE = r'WHERE:|where:'
	C_HAVING = r'HAVING:|having:'
	C_LIMIT = r'LIMIT:|limit:'
	C_WITH = r'WITH:|with:'
	C_UNION = r'UNION:|union:'
	C_GROUP = r'GROUP:|group:'
	C_ORDER = r'ORDER:|order:'
	C_QUERY = r'QUERY:|query:'
	C_CALC = r'CALC:|calc:'
	
	# ----- Token Rules: Operators -----
	OP_DISTINCT = r'DISTINCT'
	OP_INSPECT = r'INSPECT'
	OP_CASE = r'CASE\s'
	OP_ALIAS_BIND = r'->'
	OP_YIELDS = r'=>'

	# ----- Token Rules: Functionality -----
	F_TERNARY = r'\(.+\)\s+\?\s+\(.+\)\s+\:\s+\(.+\)'  # Matches: (expr) ? (expr) : (expr)

	COMMA = r','
	LINE_BREAK = r'\n'
	PASSTHROUGH = r'[^,\s\n]+'