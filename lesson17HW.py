class MethodNameValidatorMeta(type):
    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value):
                if not attr_name.startswith('_'):
                    raise ValueError(
                        f"Method '{attr_name}' is invalid. Method names must start with '_'."
                    )
        return super().__new__(mcs, name, bases, namespace)


class MyClass(metaclass=MethodNameValidatorMeta):
    def _test(self):
        return "valid method"

    def _another_method(self):
        return "also valid"

    x = 10
    y = "some attribute"


obj = MyClass()
print(obj._test())
print(obj._another_method())


class InvalidClass(metaclass=MethodNameValidatorMeta):
    def test(self):
        return "invalid method"
