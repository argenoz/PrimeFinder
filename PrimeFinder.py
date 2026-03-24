


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


def get_P(n):
    return P_set_find(n)[-1]

print(get_P(1233))


