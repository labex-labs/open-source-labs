# Objects Contain Data and Behavior

The book _Design Patterns: Elements of Reusable Object-Oriented Software_ by
Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides (Addison-Wesley,
1994), colloquially referred to as _The Gang of Four_ book, is a catalog of
object-oriented design patterns. It defines OOP in this way:

Object-oriented programs are made up of objects. An _object_ packages both data
and the procedures that operate on that data. The procedures are typically
called _methods_ or _operations_.

Using this definition, Rust is object oriented: structs and enums have data,
and `impl` blocks provide methods on structs and enums. Even though structs and
enums with methods aren’t _called_ objects, they provide the same
functionality, according to the Gang of Four’s definition of objects.
