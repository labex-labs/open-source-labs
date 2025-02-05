# Third Party Test Tools

The built-in `unittest` module has the advantage of being available everywhere--it's part of Python. However, many programmers also find it to be quite verbose. A popular alternative is [pytest](https://docs.pytest.org/en/latest/). With pytest, your testing file simplifies to something like the following:

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

To run a test, just type a command like `python -m pytest`. It will then find and run all the tests. The module can be installed using `pip install pytest`.

There's a lot more to `pytest` than this example, but it's usually pretty easy to get started should you decide to try it out.

In this exercise, you will explore the basic mechanics of using Python's `unittest` module.

In earlier exercises, you wrote a file `stock.py` that contained a `Stock` class. For this exercise, it assumed that you're using the code written for Exercise 7.9 involving typed-properties. If, for some reason, that's not working, you might want to copy the solution from `Solutions/7_9` to your working directory.
