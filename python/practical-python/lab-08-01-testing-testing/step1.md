# Assertions

The `assert` statement is an internal check for the program. If an
expression is not true, it raises a `AssertionError` exception.

`assert` statement syntax.

```python
assert <expression> [, 'Diagnostic message']
```

For example.

```python
assert isinstance(10, int), 'Expected int'
```

It shouldn't be used to check the user-input (i.e., data entered
on a web form or something). It's purpose is more for internal
checks and invariants (conditions that should always be true).
