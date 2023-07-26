# Enabling Recursive Types with Boxes

A value of a _recursive type_ can have another value of the same type as part
of itself. Recursive types pose an issue because at compile time Rust needs to
know how much space a type takes up. However, the nesting of values of
recursive types could theoretically continue infinitely, so Rust can’t know how
much space the value needs. Because boxes have a known size, we can enable
recursive types by inserting a box in the recursive type definition.

As an example of a recursive type, let’s explore the _cons list_. This is a
data type commonly found in functional programming languages. The cons list
type we’ll define is straightforward except for the recursion; therefore, the
concepts in the example we’ll work with will be useful any time you get into
more complex situations involving recursive types.
