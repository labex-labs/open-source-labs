# Discussion

Writing extensible code is one of the most common uses of inheritance
in libraries and frameworks. For example, a framework might instruct
you to define your own object that inherits from a provided base
class. You're then told to fill in various methods that implement
various bits of functionality.

Another somewhat deeper concept is the idea of "owning your
abstractions." In the exercises, we defined _our own class_ for
formatting a table. You may look at your code and tell yourself "I should
just use a formatting library or something that someone else already
made instead!" No, you should use BOTH your class and a library.
Using your own class promotes loose coupling and is more flexible.
As long as your application uses the programming interface of your class,
you can change the internal implementation to work in any way that you
want. You can write all-custom code. You can use someone's third
party package. You swap out one third-party package for a different
package when you find a better one. It doesn't matter--none of
your application code will break as long as you preserve the
interface. That's a powerful idea and it's one of the reasons why
you might consider inheritance for something like this.

That said, designing object oriented programs can be extremely
difficult. For more information, you should probably look for books
on the topic of design patterns (although understanding what happened
in this exercise will take you pretty far in terms of using objects in
a practically useful way).
