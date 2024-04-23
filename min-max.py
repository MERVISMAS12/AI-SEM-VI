v = [1, 4, 2, 5, 3, 5, 6, 7]
cnt = 0
n = len(v)
while n>1:
    n //=2
    cnt+=1

ismax = False

if cnt % 2:
    ismax = True

while cnt > 0:
    a = []
    for i in range(0, len(v)-1, 2):
        if ismax:
            mx = max(v[i], v[i + 1])
            a.append(mx)
        else:
            mn = max(v[i], v[i + 1])
            a.append(mn)
    v = a
    ismax = not ismax
    cnt-=1

print("ANS: ", v[0])
    
