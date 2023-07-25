# match Arms

As discussed in Chapter 6, we use patterns in the arms of `match` expressions.
Formally, `match` expressions are defined as the keyword `match`, a value to
match on, and one or more match arms that consist of a pattern and an
expression to run if the value matches that arm’s pattern, like this:

```
match VALUE {
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
    PATTERN => EXPRESSION,
}
```

For example, here’s the `match` expression from Listing 6-5 that matches on an
`Option<i32>` value in the variable `x`:

```
match x {
    None => None,
    Some(i) => Some(i + 1),
}
```

The patterns in this `match` expression are the `None` and `Some(i)` to the
left of each arrow.

One requirement for `match` expressions is that they need to be _exhaustive_ in
the sense that all possibilities for the value in the `match` expression must
be accounted for. One way to ensure you’ve covered every possibility is to have
a catchall pattern for the last arm: for example, a variable name matching any
value can never fail and thus covers every remaining case.

The particular pattern `_` will match anything, but it never binds to a
variable, so it’s often used in the last match arm. The `_` pattern can be
useful when you want to ignore any value not specified, for example. We’ll
cover the `_` pattern in more detail in “Ignoring Values in a Pattern” on page
XX.
