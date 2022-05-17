import time
'''
DECORATOR is a function which takes 
    function as an argument and
    it has an inner function which collects the arguments passed to the source function
'''
def cal_time(func):     # func=cubeit
    def wrapper(*x, **y):      # *x, **y => arguments passed to the squareit function = nums
        start = time.time()
        res=func(*x,**y)     # cubeit(nums)
        end = time.time()
        print(func.__name__+" took: ", str((end - start) * 1000) + " milli seconds")
        return res
    return wrapper

@cal_time
def squareit(nums):
    result=[]
    for x in nums:
        result.append(x**2)
    return result

@cal_time
def cubeit(nums):
    result=[]
    for x in nums:
        result.append(x ** 3)
    return result

l1=list(range(1,1000001))
squareit(l1)
cubeit(l1)