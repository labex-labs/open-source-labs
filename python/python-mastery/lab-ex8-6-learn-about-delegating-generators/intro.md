# Introduction

**Objectives:**

- Learn about delegating generators

**Files Modified:** `cofollow.py`, `server.py`

One potential issue in code that relies on generators is the problem of hiding details from the user and writing libraries. A lot of low-level mechanics are generally required to drive everything and it's often rather awkward to directly expose it to users.

Starting in Python 3.3, a new `yield from` statement can be used to delegate generators to another function. It is a useful way to clean-up code that relies on generators.
