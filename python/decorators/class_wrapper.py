"""
Generic class wrapper
"""

from inspect import isfunction, ismethod
from types import FunctionType, MethodType
from typing import Union


class _ClassWrapper:
    """A generic class wrapper for decorating class functions/methods
    
    """
    wrapped = None
    inner_decorator = None

    def __init__(self, *args, **kwargs):
        self.wrapped = self.wrapped(*args, **kwargs)

    def __getattr__(self, item):
        attr = getattr(self.wrapped, item)
        if ismethod(attr) or isfunction(attr):
            return self.inner_decorator(attr)
        else:
            return attr

    @classsmethod
    def wrap(cls, wrapped: type, 
             inner_decorator: Union[FunctionType, MethodType]):
        """Return a new class wrapping the passed class"""
        return type(
            'Wrapped{}'.format(wrapped.__name__),
            (cls, ),
            {'wrapped': wrapped, 'inner_decorator': inner_decorator}
        )

