# Logging Configuration

The logging behavior is configured separately.

```python
# main.py

...

if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename  = 'app.log',      # Log output file
        level     = logging.INFO,   # Output level
    )
```

Typically, this is a one-time configuration at program startup. The configuration is separate from the code that makes the logging calls.
