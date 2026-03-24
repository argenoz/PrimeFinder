


def P_set_find(n):
    
    if n<1:
        return []
    ans = [2,3]
    ans = [2,3]
    while True:
        i = len(ans)
        if i>=n:
            if i > n:
                ans = ans[:n]
            break
        bigi = ans[-1]
        digi = range(1,bigi)
        ci=[]
        for i in digi:
            flg = False
            ii = bigi+i
            for j in ans[:-1]:
                if ii< j*j:
                    break
                flg = (ii)%j==0
                if flg:
                    break
            if not flg:
                ci.append(ii)
                if len(ans)+len(ci)==n:
                    break
        ans = ans+ci
        #print(ans)
    return ans


def P_set_find__(n):
    #the best, but the heaviest
    if n<1:
        return []
    ans = [2,3]
    ci = []
    fTrue = True
    fFalse = not fTrue
    while True:
        l = len(ans)
        if l>=n:
            if l > n:
                ans = ans[:n]
            break
        bigi = ans[-1]
        digi = range(1,bigi)
        digi = [[i,fTrue] for i in digi]
        for q in ans[:-1]:
            r = bigi%q
            i = (q - r) - 1
            l = len(digi)
            while i < l:
                digi[i][1]=fFalse
                i=i+q
        for q in digi:
            if q[1]:
                ci.append(q[0]+bigi)
        ans = ans+ci
        ci = []
    return ans



def P_set_find_2(n):
    
    if n<1:
        return []
    ans = [2,3]
    ci = []
    fTrue = True
    fFalse = not fTrue
    while True:
        l = len(ans)
        if l>=n:
            if l > n:
                ans = ans[:n]
            break
        bigi = ans[-1]
        z = [ i-bigi%i    for i in ans[:-1] ]
        i=1
        while i < bigi:
            flg = fFalse
            l = len(z)
            for q in range(l):
            
                flg = z[q] == i%ans[q]
                if flg:
                    break
            if not flg:
                ci.append(i+bigi)
            i = i+1
        
        
        ans = ans+ci
        ci = []
        ci = []
    return ans

    



def get_P(n):
    return P_set_find_2(n)[-1]

print(get_P(1000001-2))


