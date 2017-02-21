# import re
# str = "sjdajaskgka asgfdqqyw"
# if re.search(r "a.*a", str):
#    print("That string had at least two 'a's in it!")
# else:
#    print("No more than one 'a' found!")

import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'
