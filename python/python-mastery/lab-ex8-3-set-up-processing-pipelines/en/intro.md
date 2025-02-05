# Introduction

**Objectives:**

- Using coroutines to set up processing pipelines

**Files Created:** `cofollow.py`, `coticker.py`

**Note**

For this exercise the `stocksim.py` program should still be running in the background.

In Exercise 8.2 you wrote some code that used generators to set up a processing pipeline. A key aspect of that program was the idea of data flowing between generator functions. A very similar kind of dataflow can be set up using coroutines. The only difference is that with a coroutine, you send data into different processing elements as opposed to pulling data out with a for-loop.
