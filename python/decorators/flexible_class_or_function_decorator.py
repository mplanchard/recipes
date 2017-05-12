"""
Possibly the most flexible decorator. Can decorate with or without parens, on functions
or classes.
"""


from functools import wraps
from inspect import isclass, isfunction, ismethod


def _inner_decorator(wrapped):

    print('no_arg_decorator(%s)' % (wrapped, ))

    def func_or_meth_wrapper(*args):
        print('wrapper(%s)' % (args, ))
        return wrapped(*args)

    if isclass(wrapped):

        class ClassWrapper:

            def __init__(self, *args):
                self.wrapped = wrapped(*args)

            def __getattr__(self, item):
                attr = getattr(self.wrapped, item)
                if ismethod(attr) or isfunction(attr):
                    return _inner_decorator(attr)
                else:
                    return attr

        wrapper = ClassWrapper

    else:
        wrapper = wraps(wrapped)(func_or_meth_wrapper)

    return wrapper


def decorator(*outer_args):

    print('arg_decorator(%s)' % (outer_args, ))

    # The below handles the expected situation when the decorator is
    # used without parens, there will be only one argument, and it will
    # be a callable of some kind.
    # replace `str` with whatever your expected first param should be
    if outer_args and not isinstance(outer_args[0], str):
        return _inner_decorator(outer_args[0])

    return _inner_decorator


print('pre-definition')

@decorator('foo')
def some_func(*args):
    print('some_func(%s)' % (args, ))


print('post-definition')


some_func('bar')


print('pre-definition')

@decorator
def other_func(*args):
    print('other_func(%s)' % args)


print('post-definition')


other_func('bar')


@decorator('foo')
class DecoratedClass:

    class_attribute = 'class'

    def __init__(self):
        self.instance_attribute = 'instance'

    @classmethod
    def method(cls, *args):
        print('method_one({})'.format(args))


dc = DecoratedClass()

dc.method('baz')
print(dc.class_attribute)
print(dc.instance_attribute)

'''
Output:

pre-definition
arg_decorator(('foo',))
no_arg_decorator(<function some_func at 0x1024f3730>)
post-definition
wrapper(('bar',))
some_func(('bar',))
pre-definition
arg_decorator((<function other_func at 0x1024f3840>,))
no_arg_decorator(<function other_func at 0x1024f3840>)
post-definition
wrapper(('bar',))
other_func(bar)
arg_decorator(('foo',))
no_arg_decorator(<class '__main__.DecoratedClass'>)
no_arg_decorator(<bound method DecoratedClass.method of <class '__main__.DecoratedClass'>>)
wrapper(('baz',))
method_one(('baz',))
class
instance

'''
