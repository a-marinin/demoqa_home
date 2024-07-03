# def test_example():
#     a = 1
#     assert a in [2, 3, 4]



import re
match = re.search(r'(\d+/\d+/\d+)', 'The date is 11/12/98')
match.group(1)
