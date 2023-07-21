# Virtual Environments

A common solution to package installation issues is to create a
so-called "virtual environment" for yourself. Naturally, there is no
"one way" to do this--in fact, there are several competing tools and
techniques. However, if you are using a standard Python installation,
you can try typing this:

```bash
$ python -m venv mypython
bash %
```

After a few moments of waiting, you will have a new directory
`mypython` that's your own little Python install. Within that
directory you'll find a `bin/` directory (Unix) or a `Scripts/`
directory (Windows). If you run the `activate` script found there, it
will "activate" this version of Python, making it the default `python`
command for the shell. For example:

```bash
$ source mypython/bin/activate
(mypython) bash %
```

From here, you can now start installing Python packages for yourself.
For example:

```
(mypython) $ python -m pip install pandas
...
```

For the purposes of experimenting and trying out different
packages, a virtual environment will usually work fine. If,
on the other hand, you're creating an application and it
has specific package dependencies, that is a slightly
different problem.
