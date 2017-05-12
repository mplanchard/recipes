"""
Simple illustration of a funciton-style decorator with args
"""

from functools import wraps


def decorator(*outer_args):

    print('decorator(%s)' % outer_args)

    def wrap(wrapped):

        print('wrap({})'.format(wrapped))

        @wraps(wrapped)
        def wrapper(*args):

            print('wrapper(%s)' % args)
            print('warpper.outer_args = %s' % outer_args)

            return wrapped(*args)

        return wrapper

    return wrap

print('pre-definition')

@decorator('foo')
def some_func(*args):
    print('some_func(%s)' % args)


print('post-definition')


some_func('bar')



'''
Output:

pre-definition
decorator(foo)
wrap(<function some_func at 0x10196d0d0>)
post-definition
wrapper(bar)
warpper.outer_args = foo
some_func(bar)

'''

