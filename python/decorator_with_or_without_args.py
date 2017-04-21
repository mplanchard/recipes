"""
The following illustrates the flow of execution for a flexible
decorator that be called either be called, with/without arguments,
e.g. ``@decorate()`` or ``@decorate('foo')``, or used as a raw
decorator, e.g. ``@decorate``.
"""

class decorate:

    def __init__(self, *args, **kwargs):
        """"""
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        """"""
        print('in __call__()')

        if callable(self.args[0]) and len(self.args) == 1 and not self.kwargs:
            print('__call__ acting as func wrapper')
            func = self.args[0]
            self._pre()
            ret = func(*args, **kwargs)
            self._post()
            return ret

        elif callable(args[0]) and len(args) == 1 and not kwargs:
            print('__call__ returning a wrapped func')

            func = args[0]

            def func_wrapper(*args, **kwargs):
                """"""
                print('func_wrapper()')
                self._pre()
                ret = func(*args, **kwargs)
                self._post()
                return ret

            return func_wrapper

        else:
            raise RuntimeError('Problem with call signature')

    def _pre(self):
        print('_pre function')

    def _post(self):
        print('_post function')


print('pre-decoration with args')


@validate('a', 'b')
def func_with_dec_args(*args):
    print('func_with_dec_args args: {}'.format(args))
    return 'foo'


print('post-decoration with args')


print('pre-decoration no args')

@validate
def func_with_no_dec_args(*args):
    print('func_with_no_dec_args args: {}'.format(args))
    return 'bar'


print('post-decoration no args')


ret = func_with_dec_args('a', 'b')
print(ret)

ret = func_with_no_dec_args('c', 'd')
print(ret)

