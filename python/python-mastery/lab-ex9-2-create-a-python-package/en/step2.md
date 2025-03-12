# Creating the Package Structure

Now, let's create our Python package. To create a Python package, we need to:

1. Create a directory with the package name
2. Create an `__init__.py` file inside this directory (this makes Python recognize the directory as a package)
3. Move our Python module files into this directory

Let's create the package structure:

1. First, create a directory called `structly`:

```bash
mkdir structly
```

2. Next, create an empty `__init__.py` file inside the `structly` directory:

```bash
touch structly/__init__.py
```

The `__init__.py` file can be empty, but it's required to make Python treat the directory as a package. When you import the package, the code in `__init__.py` is executed, which can be used to initialize the package.

3. Now, let's move our Python module files into the `structly` directory:

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Verify that all files have been moved correctly:

```bash
ls -l structly/
```

You should see:

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

Now we have created a basic package structure. The directory hierarchy should look like this:

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

In the next step, we'll fix the import statements to make the package work correctly.
