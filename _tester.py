import sequential
from sequential.bags.RouterBag import RouterBag


ex = '''
FROM:
	database.table tab
SELECT:
	column_name, other_column
'''

lex = sequential.lexers.SequentialLexer()
# print(type(lex))
# print(lex.tokens)

tokens = lex.tokenize(ex)

# for token in tokens: 
# 	print(token)
# 	print(token.type, type(token.type))

router = RouterBag(tokens = tuple(tokens))
# print(router.n_tokens)
# print(router.clause_sequence)

for bag in router.clause_bags:
	print(bag.clause.value)
	for token in bag.tokens:
		print(token)