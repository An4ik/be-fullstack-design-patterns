## Theory

### What is Factory Design Pattern?

The **Factory Design Pattern** comes under creational pattern as this pattern provides one of the best ways to create an object.

#### Why the need for it: Problem Statement
Factory methods deal with the problem of creating objects without having to specify the exact class of the object that will be created.

#### Terminology

**factory**: The static method which renpond to creating objects. 

**Creator**: The class which creates an product objects with factory method.

**Product**: The object which subclasses from Creator object.


## Explanation of Adapter Design Pattern Example

You have **Company** creator class, that has static factory method which should be refer to creating objects. You want to create objects without directly its initialization.

There are 2 kind of companies which extends from company:
+ **Apple** (Have only invent() method)
+ **Google** (Have only invent() method)


## Instruction

1. Open **factory.py**.

2. You see that there are classes, but methods are not implemented.

3. Look at the file **tests/test_factory.py**.

4. Run these tests:

```python3 -m unittest tests/test_factory.py'```

You will see that there are few tests, and at first you should have failed test cases 

5. To pass all tests, complete functions, which are written in **factory.py** file.

6. You should complete one function at a time, then be sure that you have less failures
or/and erros left. Commit and push your changes.

7. Finally, you have to be sure that no test is failed and all of them are passed.

8. Analyze our implementation **answers/factory.py**.

