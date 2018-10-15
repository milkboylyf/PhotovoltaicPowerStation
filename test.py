from multiprocessing import Pool
# from functools import partial
#
# def somefunc(str_1, str_2, iterable_iterm):
#    print("%s %s %d" % (str_1, str_2, iterable_iterm*iterable_iterm))
#     # print(iterable_iterm*iterable_iterm)
#
# def main():
#     iterable = [1, 2, 3, 4, 5]
#     pool = Pool(processes=6)
#     str_1 = "This"
#     str_2 = "is"
#     func = partial(somefunc, str_1, str_2)
#     pool.map(func, iterable)
#     pool.close()
#     pool.join()
#
# if __name__ == "__main__":
#     main()


from multiprocessing import Pool
def myfun(x):
    return x*x


if __name__ == '__main__':
    pool = Pool()
    xs = range(5)
    result = pool.map(myfun, xs)
    print(result)
    rst1 = pool.imap(myfun, xs)
    rst2 = pool.imap_unordered(myfun,xs)
    print(type(rst1))
    print(type(rst2))
    print(rst1)
    print(rst2)

    pool.close()
