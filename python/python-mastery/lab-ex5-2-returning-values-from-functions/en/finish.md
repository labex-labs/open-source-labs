# Summary

In this lab, you learned several important patterns for returning values from functions in Python:

1. **Returning Multiple Values**: Python functions can return multiple values by packaging them into a tuple. This allows you to return and unpack several values in a clean, readable way.

2. **Optional Return Values**: For functions that might not always produce a valid result, returning `None` is a common pattern to indicate the absence of a value. We also discussed the alternative approach of raising exceptions.

3. **Futures for Concurrent Programming**: When working with concurrent code, a `Future` serves as a placeholder for a result that will be available later. This allows you to get return values from functions running in separate threads or processes.

Each of these patterns addresses specific problems that arise when working with function return values. Understanding these patterns will help you write more robust and flexible Python code.

For further practice:

- Experiment with different error handling strategies in your functions
- Try using Futures with other types of concurrent execution like processes
- Explore how these patterns work with asynchronous programming using `async`/`await`
