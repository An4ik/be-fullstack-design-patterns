# ABCclasses

Python is a very flexible language. One of the aspects of this flexibility is the possibilities provided by metaprogramming. And although in the core of the language abstract classes are not represented, they were implemented in the standard module abs.

Abstract classes are a unique way of documenting code and help limit (decouple) the interaction of individual abstractions in a program (classes). As well as abstract classes do not provide for the creation of objects, moreover, they implement one of the principles of OOP polymorphism. Regarding polymorphism, you can read here 'https://habr.com/post/37576/'.

Abstract classes also have methods like regular classes, but the difference from ordinary classes is that we cannot create objects in abstract classes. Abstract methods - contain only method definitions without implementation. It is assumed that the descendant class should predefine the method and implement its functionality.

__metaclass__ is class in the OOP, objects of which in turn are classes.
