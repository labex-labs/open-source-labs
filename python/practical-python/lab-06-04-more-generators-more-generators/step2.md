# Why Generators

- Many problems are much more clearly expressed in terms of iteration.
  - Looping over a collection of items and performing some kind of operation (searching, replacing, modifying, etc.).
  - Processing pipelines can be applied to a wide range of data processing problems.
- Better memory efficiency.
  - Only produce values when needed.
  - Contrast to constructing giant lists.
  - Can operate on streaming data
- Generators encourage code reuse
  - Separates the _iteration_ from code that uses the iteration
  - You can build a toolbox of interesting iteration functions and _mix-n-match_.
