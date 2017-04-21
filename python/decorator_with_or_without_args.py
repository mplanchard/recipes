"""
The following illustrates the flow of execution for a flexible
decorator that be called either be called, with/without arguments,
e.g. ``@decorate()`` or ``@decorate('foo')``, or used as a raw
decorator, e.g. ``@decorate``.

Rather than ``callable()``, if you expect a callable object might
be passed to your decorator, you can also use ``inspect.isfunction(arg)
or inspect.ismethod(arg)``.
"""


class decorate:

    def __init__(self, *args, **kwargs):
        """__init__ is always called at decoration time
        
        If the decorator is called with parens, ``__init__()``
        is called with the arguments passed to the decorator.
        
        If the decorator is raw, ``__init__()`` is called with
        one argument, which is the decorated function.
        
        Note that because of this, you may only have ONE specified
        positional argument, which is understood to either be
        the decorated function or something else. Other arguments
        must be kwargs.
        """
        print('__init__({})'.format(locals()))
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        """__call__ is either called at decoration time or at runtime
        
        If the decorator is specified with parens, as a call,
        ``__call__()`` is called upon decoration and should return
        a wrapped function. In this case, only one argument is
        passed to ``__call__()`, which is the decorated function.
        
        If the decorator is raw, with no parens, ``__call__()``
        will be called when the funcion is called, and acts as the
        function wrapper. In this case, the arguments to 
        ``__call__()`` are the arguments passed to the function.
        """
        print('__call__({})'.format(locals()))

        if len(self.args) == 1 and callable(self.args[0]) and not self.kwargs:
            print('__call__ acting as func wrapper')
            func = self.args[0]
            self._pre()
            ret = func(*args, **kwargs)
            self._post()
            return ret

        elif len(args) == 1 and callable(args[0]) and not kwargs:
            print('__call__ returning a wrapped func')

            func = args[0]

            def func_wrapper(*args, **kwargs):
                """This wrapper will replace the decorated function
                
                As such, it should be sure to call the decorated
                function.
                
                The arguments to this wrapper are the arguments
                passed to the function.
                """
                print('func_wrapper({})'.format(locals()))
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


@decorate()
def func_with_dec_args(*args):
    print('func_with_dec_args({})'.format(args))
    return 'foo'


print('post-decoration with args')


print('pre-decoration no args')

@decorate
def func_with_no_dec_args(*args):
    print('func_with_no_dec_args({})'.format(args))
    return 'bar'


print('post-decoration no args')


ret = func_with_dec_args('a', 'b')
print(ret)

ret = func_with_no_dec_args('c', 'd')
print(ret)

