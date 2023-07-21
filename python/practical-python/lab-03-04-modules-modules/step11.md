# Module Search Path

As noted, `sys.path` contains the search paths.
You can manually adjust if you need to.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

Paths can also be added via environment variables.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles', ...]
```

As a general rule, it should not be necessary to manually adjust
the module search path. However, it sometimes arises if you're
trying to import Python code that's in an unusual location or
not readily accessible from the current working directory.

For this exercise involving modules, it is critically important to
make sure you are running Python in a proper environment. Modules
often present new programmers with problems related to the current working
directory or with Python's path settings. For this course, it is
assumed that you're writing all of your code in the `Work/` directory.
For best results, you should make sure you're also in that directory
when you launch the interpreter. If not, you need to make sure
`practical-python/Work` is added to `sys.path`.
