import sequential
from sequential.bags.RouterBag import RouterBag


ex = '''
FROM:
	database.table tab
WHERE:
	other_column > 25
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

# for bag in router.clause_bags:
# 	print(bag.clause.value)
# 	# for token in bag.tokens: print(token)
# 	print(bag.sql(carryover = {}))
# 	print('----------')

assembler = router.handoff_assembler
# print(assembler.has_cte)
# print(assembler.sql)



'''
NEXT
MS03: Reassemble Simple Query
+ Build structure of Query Sub-object Quarks with slots
+ Build Structure of the Field that Assembles the Quarks
'''