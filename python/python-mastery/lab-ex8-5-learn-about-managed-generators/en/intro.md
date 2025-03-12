# Introduction

**Objectives:**

- Learn about managed generators
- Understand how to drive generators in unusual ways
- Build a simple task scheduler using generators
- Create a network server using generators

**Files Created:** `multitask.py`, `server.py`

A generator function in Python doesn't execute on its own - it needs to be driven by some other code. For example, a generator used for iteration only runs when you iterate over it using a `for` loop. Similarly, coroutines need their `send()` method to be called to execute.

In advanced applications, generators can be driven in various interesting ways. In this lab, we will explore some practical examples of managed generators.
