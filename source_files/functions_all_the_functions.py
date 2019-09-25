def outer_function():
    def inner_function1():
        print("inner function1")

    def inner_function2():
        print("inner function2")
    inner_function1()
    inner_function2()
    inner_function1()


def a_decorator(func):
    def wrapper():
        print("before the method is called, this happens")
        func()
        print("after the method is called, this happens")
    return wrapper


def average():
    # ask for input
    try:
        score1 = float(input("Enter a number:"))
        score2 = float(input("Enter a number:"))
        # calculate the average
        s_list = [score1, score2]

    except ValueError:
        print("you did bad")
        avg = 0
    else:
        avg = sum(s_list)/len(s_list)
    finally:
        print("average calculated")
    # return the average
    return avg


def guessing_game():
    return 5


def list_function():
    a_list = [2, 4, 6, 8]
    return a_list

# has parameter list, aka arguments, variables
def average_3(score1, score2, score3):
    # calculate the average
    # return the average
    pass


# has parameter list, aka arguments, it will be a list
def average_list(s_list):
    # calculate the average
    return sum(s_list)/len(s_list)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)



if __name__ == '__main__':
   # print(average())
   # print(average_list([1, 2, 3]))
   #  m_list = list_function()
   # for f in m_list:
    # print(f)

    #ask_ok(reminder="You messed it up", retries=10, prompt="Are you ok?")
    #outer_function()
    new_function = a_decorator(outer_function)
    new_function()

