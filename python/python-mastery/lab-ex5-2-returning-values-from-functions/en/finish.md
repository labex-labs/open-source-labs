# Summary

In this lab, you have learned several key patterns for returning values from functions in Python. Firstly, Python functions can return multiple values by packing them into a tuple, enabling clean and readable value return and unpacking. Secondly, for functions that may not always yield valid results, returning `None` is a common way to indicate the absence of a value, and raising exceptions was also presented as an alternative.

Lastly, in concurrent programming, a `Future` acts as a placeholder for a future result, allowing you to obtain return values from functions running in separate threads or processes. Understanding these patterns will enhance the robustness and flexibility of your Python code. For further practice, experiment with different error - handling strategies, use Futures with other concurrent execution types, and explore their application in asynchronous programming with `async`/`await`.
