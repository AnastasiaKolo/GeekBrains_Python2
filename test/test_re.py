import re

# https://docs.python.org/3/howto/regex.html#regex-howto
# https://docs.python.org/3/library/re.html#re-syntax

file = open('listener.ora', 'r+')

listener_ora = file.read()

# options
# re.I = re.IGNORECASE Perform case-insensitive matching
# re.M = re.MULTILINE When specified, the pattern character '^' matches at
# the beginning of the string and at the beginning of each line
# re.S = re.DOTALL Make the '.' special character match any character at all,
# including a newline
# re.X = re.VERBOSE allows you to write regular expressions that look nicer and
# are more readable by allowing you to visually separate logical sections of
# the pattern and add comments
re_options = re.M + re.S + re.I + re.X


# list_re = "^(\w+?)\s?=.*?SID_DESC\s?=\s?(.+?)\).*?SID_NAME\s?=\s?(\d+?)\).* ?ORACLE_HOME\s?=\s?(.+?)\)"
# list_re = "^\.*SID_DESC\s?=\s?(.+?)\).*?SID_NAME\s?=\s?(\d+?)\).* ?ORACLE_HOME\s?=\s?(.+?)\)"
# listener_ora = "   SID_DESC = (GLOBAL_DBNAME = testdb1)(SID_NAME = testdb1)(ORACLE_HOME = /u01/app/oracle/product/10.2.0/db_1)"

# list_re = "\(\s*(?:SID_NAME)\s*=\s*\w+\s*\)"

list_re = "\(\s*(?:SID_DESC)\s*=\s*\.*\s*\)"

# find the beginning of SID_DESC
test_re = "\(\s*SID_DESC\s*=\s*\(\s*"
test1_re = "\([^()]*\)"  # find any text between ()
# find text between () where SID_NAME or ORACLE_HOME is described
# and extract name and value of the parameter
test2_re = "\(\s*(?P<name>SID_NAME|ORACLE_HOME)\s*=\s*(?P<val>[^()]*)\)"
test3_re = "\(\s*(?P<name>SID_NAME|ORACLE_HOME)\s*=\s*(?P<val>[^()\s]*)\s*\)"
test4_re = "\(\s*(?P<name>SID_NAME|ORACLE_HOME|GLOBAL_DBNAME)\s*=\s*(?P<val>[^()\s]*)\s*\)"
# find text between () where SID_DESC is described
# not ready yet!!!
test5_re = "\(\s*SID_DESC\s*=\s*(\(\s*(?P<name>SID_NAME|ORACLE_HOME|GLOBAL_DBNAME)\s*=\s*(?P<val>[^()\s]*)\s*\))"

# find specific ORACLE_SID and its parameters
test6_re = """(\(\s*SID_DESC\s*=\s* # find the beginning of SID_DESC
           \(\s*GLOBAL_DBNAME\s*=\s*testdb2\s*\)\s*
           \(\s*SID_NAME\s*=\s*testdb2\s*\)\s*
           \(\s*ORACLE_HOME\s*
           =\s*(?P<val>[^()\s]*)\s*\))
           """



# print("list_re=", re.findall(list_re, listener_ora, re_options))
print("test_re=", re.findall(test_re, listener_ora, re_options))
# print("test1_re=", re.findall(test1_re, listener_ora, re_options))
# print("test2_re=", re.findall(test2_re, listener_ora, re_options))
# print("test3_re=", re.findall(test3_re, listener_ora, re_options))
print("test4_re=", re.findall(test4_re, listener_ora, re_options))
print("test6_re=", re.findall(test6_re, listener_ora, re_options))
# print(re.match(list_re, listener_ora, re.M + re.S))
# print(re.finditer(list_re, listener_ora, re.M + re.S))

# filenames = re.findall('\w+\.(?:txt|php|css)', listener_ora)
# print(filenames)

for match in re.finditer(test6_re, listener_ora, re_options):
    t = match.groups()
    # easy_connects[t[0]] = "%s:%s/%s" % t[1:]
    print("_____________________________________")
    # print("match=", match)
    print(match.groups())
    print(match.groupdict())
    print("val='%s'" % match.group('val'))
    print("match.group(0)=", match.group(0))
    print("match.group(1)=", match.group(1))
    print("match.group(2)=", match.group(2))
    # print(match.string)

# print(easy_connects)