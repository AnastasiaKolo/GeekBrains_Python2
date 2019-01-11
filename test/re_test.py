import re

file = open('listener.ora', 'r+')

listener_ora = file.read()

easy_connects = {}

# list_re = "^(\w+?)\s?=.*?SID_DESC\s?=\s?(.+?)\).*?SID_NAME\s?=\s?(\d+?)\).* ?ORACLE_HOME\s?=\s?(.+?)\)"
# list_re = "^\.*SID_DESC\s?=\s?(.+?)\).*?SID_NAME\s?=\s?(\d+?)\).* ?ORACLE_HOME\s?=\s?(.+?)\)"
# listener_ora = "   SID_DESC = (GLOBAL_DBNAME = testdb1)(SID_NAME = testdb1)(ORACLE_HOME = /u01/app/oracle/product/10.2.0/db_1)"

# list_re = "\(\s*(?:SID_NAME)\s*=\s*\w+\s*\)"

list_re = "\(\s*(?:SID_DESC)\s*=\s*\.*\s*\)"

test_re = "\(\s*SID_DESC\s*=\s*\(\s*"  # find the beginning of SID_DESC
test1_re = "\([^()]*\)"  # find any text between ()
# find text between () where SID_NAME or ORACLE_HOME is described
# and extract name and value of the parameter
test2_re = "\(\s*(?P<name>SID_NAME|ORACLE_HOME)=(?P<val>[^()]*)\)"
# find text between () where SID_DESC is described
test3_re = "\(\s*(?:SID_DESC)=\.*\)"
print("list_re=",re.findall(list_re, listener_ora, re.M + re.S + re.DOTALL))
print("test_re=",re.findall(test_re, listener_ora, re.M + re.S + re.DOTALL))
print("test1_re=",re.findall(test1_re, listener_ora, re.M + re.S + re.DOTALL))
print("test2_re=",re.findall(test2_re, listener_ora, re.M + re.S + re.DOTALL))
print("test3_re=",re.findall(test3_re, listener_ora, re.M + re.S + re.DOTALL))
# print(re.match(list_re, listener_ora, re.M + re.S))
#print(re.finditer(list_re, listener_ora, re.M + re.S))

# filenames = re.findall('\w+\.(?:txt|php|css)', listener_ora)
# print(filenames)

for match in re.finditer(test2_re, listener_ora, re.M + re.S + re.DOTALL):
    t = match.groups()
    # easy_connects[t[0]] = "%s:%s/%s" % t[1:]
    print("_____________________________________")
    print("match=", match)
    print(match.groups())
    print(match.groupdict())
    #print(match.string)


#print(easy_connects)
