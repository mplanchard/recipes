"""
An illustration of the different methods of access to class
attributes and their differing values in class methods versus
bound methods.
"""


from pprint import pprint

class SomeClass:

    class_attr = 'class_attr'

    def __init__(self):
        self.instance_attr = 'instance_attr'

    def bound_method(self):
        print('bound_method')
        print('============')
        print('vars:')
        pprint(vars(self))
        print('dir:')
        pprint(dir(self))
        print('dict:')
        pprint(self.__dict__)
        print()

    @classmethod
    def class_method(cls):
        print('class_method')
        print('============')
        print('vars:')
        pprint(vars(cls))
        print('dir:')
        pprint(dir(cls))
        print('dict:')
        pprint(cls.__dict__)
        print()


sc = SomeClass()
sc.bound_method()
sc.class_method()


"""
Output:

bound_method
============
vars:
{'instance_attr': 'instance_attr'}
dir:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'bound_method',
 'class_attr',
 'class_method',
 'instance_attr']
dict:
{'instance_attr': 'instance_attr'}

class_method
============
vars:
mappingproxy({'__dict__': <attribute '__dict__' of 'SomeClass' objects>,
              '__doc__': None,
              '__init__': <function SomeClass.__init__ at 0x102d73620>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'SomeClass' objects>,
              'bound_method': <function SomeClass.bound_method at 0x102d736a8>,
              'class_attr': 'class_attr',
              'class_method': <classmethod object at 0x102d5ce80>})
dir:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'bound_method',
 'class_attr',
 'class_method']
dict:
mappingproxy({'__dict__': <attribute '__dict__' of 'SomeClass' objects>,
              '__doc__': None,
              '__init__': <function SomeClass.__init__ at 0x102d73620>,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'SomeClass' objects>,
              'bound_method': <function SomeClass.bound_method at 0x102d736a8>,
              'class_attr': 'class_attr',
              'class_method': <classmethod object at 0x102d5ce80>})
              
"""
