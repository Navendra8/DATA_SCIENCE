import numpy as np
class stats():
    def __init(self,num):
        self.num=self.num
    
    def mean(self,num):
        m=sum(num)/len(num)
        return m 
        
    def median(self,num):
        
        if len(num)%2 != 0:
            num.sort()
            a=len(num)
            i= int((a+1)/2)
            med=num[i-1]
            return med
        else:
            N=len(num)
            i1=N//2
            i2=(N+2)//2
            m = (num[i1-1]+num[i2-1])/2
            return m
     
    def mode(self,num):
        num.sort()
        a = 0
        n = num[0]
        for i in num:
            times_accur = num.count(i)
            if times_accur > a:
                a = times_accur
                n = i
        return n
