# Somewhat Better Approach

If you're going to catch all errors, this is a more sane approach.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
```

It reports a specific reason for failure. It is almost always a good idea to have some mechanism for viewing/reporting errors when you write code that catches all possible exceptions.

In general though, it's better to catch the error as narrowly as is reasonable. Only catch the errors you can actually handle. Let other errors pass by--maybe some other code can handle them.
