import time
import threading

def calc_square(numbers):
    print('Calculate square numbers: ')
    for i in numbers:
        # time-delay
        #time.sleep(2)
        print('square: {}'.format(str(i * i)))
        
    
    
def calc_cube(numbers):
    print('Calculate cube numbers')
    for i in numbers:
        time.sleep(2)
        print('cube:{}'.format(str(i * i * i)))
        
        
if __name__== '__main__':
    arr = [2,3,8,9]
    t1 = threading.Thread(target=calc_square, args=(arr,))
    t2 = threading.Thread(target=calc_cube, args=(arr,))
    #creating two threads here ti & t2
    
    t1.start()
    t2.start()
    # Starting threads here parallel by start funcion
    
    t1.join()
    # This join() will wait untill the cal_square() function is finished
    
    t2.join()
    # This join() will wait untill the cal_square() function is finished
    
    print('Main Thread Here!!')
    print('Sucesses!')