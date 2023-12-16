def counter(start):
    def increment(step=1):
        nonlocal start
        start = start +step
        print(start)
    return increment

my_func = counter(5)

my_func()
my_func()
