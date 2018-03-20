import sys


def funny_print():
    print_func = print

    def wrapper(*args, **kwargs):
        try:
            if int(args[0] > 14):
                print_func(int(args[0])*2)
            else:
                print_func(int(args[0]))
        except:
            print_func("hehe ", end="")
            print_func(*args, **kwargs)
    return wrapper


sys.modules['builtins'].print = funny_print()
