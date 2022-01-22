import pkg_resources



class _helpers:
	@staticmethod
	def querybank(path:str) -> str:
		return pkg_resources.resource_string(__name__, path).decode('UTF-8')



class Test_SingleQuark:
	
	def test_pulse(self): assert True

	
	def test_from_select(self):
		query = _helpers.querybank('/queries/')
		
		# r = pkg_resources.resource_string(__name__, 'queries/simple/from_select_where.seq')

		# assert(r == 'TODO')
		assert True


		return









# import sqlvalidator
# query = assembler.sql
# analyzed = sqlvalidator.parse(query)
# print(analyzed.is_valid())

'''
Remaining
- Build single test query checker shell
- Build conversion function at module base
- Attach validator and conversion function to test
'''