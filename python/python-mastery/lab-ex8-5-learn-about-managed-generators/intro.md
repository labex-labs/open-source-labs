# Introduction

_Objectives:_

- Learn about managed generators

_Files Created:_ `multitask.py`, `server.py`

A generator or coroutine function can never execute without being
driven by some other code. For example, a generator used for
iteration doesn't do anything unless iteration is actually carried out
using a for-loop. Similarly, a collection of coroutines won't run
unless their `send()` method is invoked somehow.

In advanced applications of generators, it is possible to drive
generators in various unusual ways. In this exercise, we look at a
few examples.
