# Historical Digression

List comprehensions come from math (set-builder notation).

```code
a = [ x * x for x in s if x > 0 ] # Python

a = { x^2 | x ∈ s, x > 0 }         # Math
```

It is also implemented in several other languages. Most coders probably aren't thinking about their math class though. So, it's fine to view it as a cool list shortcut.

Start by running your `report.py` program so that you have the portfolio of stocks loaded in the interactive mode.

```bash
$ python3 -i report.py
```

Now, at the Python interactive prompt, type statements to perform the operations described below. These operations perform various kinds of data reductions, transforms, and queries on the portfolio data.
