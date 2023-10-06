# Exercise 6.8: Setting up a simple pipeline

Let's see the pipelining idea in action. Write the following function:

```python
>>> def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

>>>
```

This function is almost exactly the same as the first generator example in the previous exercise except that it's no longer opening a file--it merely operates on a sequence of lines given to it as an argument. Now, try this:

```python
>>> from follow import follow
>>> lines = follow('stocklog.csv')
>>> goog = filematch(lines, 'GOOG')
>>> for line in goog:
        print(line)

... wait for output ...
```

It might take awhile for output to appear, but eventually you should see some lines containing data for GOOG.

Note: These exercises must be carried out simultaneously on two separate terminals.
