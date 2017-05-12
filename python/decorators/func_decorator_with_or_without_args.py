"""
An illustration of a basic function decorator that can be called
with or without parens & arguments
"""


from functools import wraps


def no_arg_decorator(wrapped, *outer_args):

    print('no_arg_decorator(%s)' % (wrapped, ))
    print('no_arg_decorator.outer_args = %s', (outer_args, ))

    @wraps(wrapped)
    def wrapper(*args):
        print('wrapper(%s)' % (args, ))
        print('wrapper.outer_args = %s' % (outer_args, ))
        return wrapped(*args)

    return wrapper


def arg_decorator(*outer_args):

    print('arg_decorator(%s)' % (outer_args, ))

    # replace `str` with whatever your expected first param should be
    if outer_args and not isinstance(outer_args[0], str):
        return no_arg_decorator(outer_args[0])

    return no_arg_decorator


print('pre-definition')

@arg_decorator('foo')
def some_func(*args):
    print('some_func(%s)' % (args, ))


print('post-definition')


some_func('bar')


print('pre-definition')

@arg_decorator
def other_func(*args):
    print('other_func(%s)' % args)


print('post-definition')


other_func('bar')


'''
Output:

pre-definition
arg_decorator(('foo',))
no_arg_decorator(<function some_func at 0x101a69048>)
no_arg_decorator.outer_args = %s ((),)
post-definition
wrapper(('bar',))
wrapper.outer_args = ()
some_func(('bar',))
pre-definition
arg_decorator((<function other_func at 0x101a69158>,))
no_arg_decorator(<function other_func at 0x101a69158>)
no_arg_decorator.outer_args = %s ((),)
post-definition
wrapper(('bar',))
wrapper.outer_args = ()
other_func(bar)
'''

