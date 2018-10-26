# Strategy Design Pattern
The strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime.
Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.
Strategy lets the algorithm vary independently from the clients that use it.
Capture the abstraction in an interface, bury implementation details in derived classes.

#### Links
+ https://en.wikipedia.org/wiki/Strategy_pattern
+ https://sourcemaking.com/design_patterns/strategy


# Explanation of Strategy Design Pattern example
Suppose that you need to write classes for Man and Woman, which inherit from Person class. Each Person can have their own Name and Job.
But sometimes people want to change their jobs. Your classes should implement this using Strategy Design Pattern.
There is **JobStrategyAbstract** class, which has 1 required abstract method work.
And 3 classes that implement **JobStrategyAbstract** class: **DeveloperStrategy**, **TeacherStrategy** and **DoctorStrategy**.
Each have their own implementation of required abstract work method.

+ **DeveloperStrategy**'s work method should return "is working as a Developer at Google." string.
+ **TeacherStrategy**'s work method should return "is working as a Teacher in school." string.
+ **DoctorStrategy**'s work method should return "is working as a Doctor in hospital." string.

There is also **Person** class, which has 2 attributes name and job.
**Person** class has 2 child class that inherit from it, **Man** and **Woman** classes, which both have their own implementation of __str__ magic function.

+ **Man**'s __str__ magic function should return name of the person + " is a man and " + whatever job attribute's work method returns.
+ **Woman**'s __str__ magic function should return name of the person + " is a woman and " + whatever job attribute's work method returns.


# Instructions

1. Look at the file **strategy.py**. 

2. Classes and methods aren't implemented. Your task is to implement them using Strategy Design Pattern.

3. Look at the file **tests/test_strategy.py**.

3. Run tests:
   
        python3 -m unittest tests/test_strategy.py
        
    You will see that it ran 4 tests and all of them FAILED (failures=1, errors=3)

4. Now, complete classes and methods in **strategy.py**.

5. After running tests, all of them must be passed.

6. Compare your answer with our located in **answers/strategy.py**.

7. Commit and push your changes.
