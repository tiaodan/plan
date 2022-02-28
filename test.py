a = ((30,),)
print(a[0][0])
print(type(a[0][0]))


resultjson = {
        "code": 500,
        "msg": "",
        "count": 0,
        "data": []
    }
print(type(resultjson))
if isinstance(resultjson, dict):
    print('dict')

a = [1, 2, 3, 4]
if 10 not in a:
    print('10 not in a')

a = 'str'
b = 'st'
if b in a:
    print('st in str')

# a = "s"
a = ""
print(len(a))
if a is not None and a != '':
    print('a is not None')

a = {'a': 'aa', 'bb': 'bb'}
if 'aa' in a:
    print('aa in dict-a')

test = [{'id': 5, 'name': '地铁'}, {'id': 6, 'name': '打卡'}, {'id': 7, 'name': '早饭'}]

print(type(test))
for x in test;
    print(x)