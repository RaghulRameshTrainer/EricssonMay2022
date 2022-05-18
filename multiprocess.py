import multiprocessing
import time
def calc_square(nums):
    for x in nums:
        print("square :"+str(x*x))
        time.sleep(1)
def calc_cube(nums):
    for x in nums:
        print("cube :"+str(x*x*x))
        time.sleep(1)
if __name__=='__main__':
    l1=[1,2,3,4,5]
    p1=multiprocessing.Process(target=calc_square,args=(l1,))
    p2=multiprocessing.Process(target=calc_cube,args=(l1,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done")