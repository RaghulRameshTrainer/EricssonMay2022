'''

def tv_channal():
    yield "start sports"
    yield "cnn"
    yield "espn"
    yield "National"

# prog=tv_channal()
# print(next(prog))
# print(next(prog))
# print(next(prog))
# print(next(prog))
for p in tv_channal():
    print(p)
'''
#Fibonacci sequence 0,1,1,2,3,5,8,13,21,34,55,89......

def fib():
    x,y=0,1
    while True:
        yield x     #0,1,1,2,3,5
        x,y=y,x+y  #1(1),1(2),2(3),3(5),5(8)


for f in fib():
    if f > 100:
        break
    print(f,end=' ')