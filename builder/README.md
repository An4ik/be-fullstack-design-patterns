## Builder

Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach.
This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. 
This builder is independent of other objects. Designed to solve the problem of the Telescoping Constructor anti-pattern.

#### Why we use Builder Design Pattern?

While considering the builder pattern you need to look weather the object is having

* Complex constructor
        
    Multiple constructor having combinations of multiple parameter with nested objects

* Large number of parameters.
    
    Having large number of field parameter is also the key point to consider.

* Immutability.

    You can force the immutability to the object once you are done with creation of object.
    
It typically solve problem in object oriented programming i.e determining what constructor to use. Often we write many constructor and it is really hard to manage them. The multiple constructor with combination of multiple parameters variation is called the telescoping constructor.

> Builder pattern is used to create instance of very complex object having telescoping constructor in easiest way.


**Pros**
1) Code is more maintainable if number of fields required to create object is more than 4 or 5.
2) Object Creation code less error-prone as user will know what they are passing because of explicit method call.
3) Builder pattern increase robustness, as only fully constructed object will be available to client.
4) You can force immutability to the object once its created.

**Cons**
1) Builder pattern is verbose and requires code duplication as Builder needs to copy all fields from Original or Item class.