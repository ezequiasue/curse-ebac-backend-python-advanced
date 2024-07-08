import time
import multiprocessing

# Create a Global Variable

results = []


def calc_square(numbers):
    global results
    for i in numbers:
        print("square: ", str(i * i))
        results.append(i * i)
        print("witnin a result: " + str(results))


def cal_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print("cube: ", str(i * i * i))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # creating one Process here p1

    p1.start()
    # starting processes here parallel by using starting function.

    p1.join()
    # this join() will wait untill calc_square() function is finished.

    print("result : " + str(results))
    # This print didn't work here we have to print it within the process
    print("Sucess")
