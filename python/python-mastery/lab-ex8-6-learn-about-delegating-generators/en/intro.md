# Introduction

In this lab, you will learn about delegating generators in Python using the `yield from` statement. This feature, introduced in Python 3.3, simplifies code that depends on generators and coroutines.

Generators are special functions that can pause and resume execution, retaining their state between calls. The `yield from` statement offers an elegant way to delegate control to another generator, enhancing code readability and maintainability.

**Objectives:**

- Understand the purpose of the `yield from` statement
- Learn how to use `yield from` to delegate to other generators
- Apply this knowledge to simplify coroutine-based code
- Understand the connection to modern async/await syntax

**Files you will work with:**

- `cofollow.py` - Contains coroutine utility functions
- `server.py` - Contains a simple network server implementation
