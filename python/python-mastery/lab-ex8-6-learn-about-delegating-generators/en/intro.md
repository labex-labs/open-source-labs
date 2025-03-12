# Introduction

In this lab, you will learn about delegating generators in Python using the `yield from` statement. This feature was introduced in Python 3.3 to simplify code that relies on generators and coroutines.

Generators are special functions that can pause and resume execution, maintaining their state between calls. When working with generators, especially in libraries, it can be challenging to expose clean interfaces to users without revealing the low-level mechanics.

The `yield from` statement provides an elegant way to delegate control to another generator, making your code more readable and maintainable.

**Objectives:**

- Understand the purpose of the `yield from` statement
- Learn how to use `yield from` to delegate to other generators
- Apply this knowledge to simplify coroutine-based code
- Understand the connection to modern async/await syntax

**Files you will work with:**

- `cofollow.py` - Contains coroutine utility functions
- `server.py` - Contains a simple network server implementation
