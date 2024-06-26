def printbinarynum(size,res,n):
    if size==n:
        print(res)
        return
    printbinarynum(size+1,res+'1',n)
    printbinarynum(size+1,res+'0',n)
n=3
printbinarynum(0,'',n)