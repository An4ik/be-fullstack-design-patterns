"""
Singleton Design Pattern.
"""


class Singleton(type):
    """
      Ensure a class has only one instance, and provide a global point of access to it.

    It has one and only one instance.

    Your implementation which is also documented well.

    Attributes:
        __instance - ....
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
