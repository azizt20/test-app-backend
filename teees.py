import json

ttt = '[[1],[2,3],"lorem",[5],[11,12]]'
res = json.loads(ttt)
print(res[1][1])
if [1,2] == [1,2]:
    print('adda')