def func():
    print('Function Part 1')
    
    x = yield
    
    print(x)
    print('Function Part 2')
    
    
    a = yield
    print(a)    
    print('Function Part 3')
    
    
try:
    y  = func()
      
    next(y)  # Function part 1 executed, to reach the first yield we used next

    y.send(6) # Function part 2 executed and value sent 6
    
    y.send(12) # Function part 2 executed and value sent 12 and StopIteration raised
    
     
except StopIteration as e:
    pass