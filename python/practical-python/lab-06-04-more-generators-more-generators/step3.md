# `itertools` module

The `itertools` is a library module with various functions designed to help with iterators/generators.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
```

All functions process data iteratively. They implement various kinds of iteration patterns.

More information at [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) tutorial from PyCon '08.

In the previous exercises, you wrote some code that followed lines being written to a log file and parsed them into a sequence of rows. This exercise continues to build upon that. Make sure the `stocksim.py` is still running.
