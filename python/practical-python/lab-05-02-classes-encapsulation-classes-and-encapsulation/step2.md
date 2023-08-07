# A Problem

In Python, almost everything about classes and objects is _open_.

- You can easily inspect object internals.
- You can change things at will.
- There is no strong notion of access-control (i.e., private class members)

That is an issue when you are trying to isolate details of the _internal implementation_.
