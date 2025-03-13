# Creating the Package Structure

Now, we're going to create our Python package. But first, let's understand what a Python package is. A Python package is a way to organize related Python modules into a single directory hierarchy. It helps in managing and reusing code more effectively. To create a Python package, we need to follow these steps:

1. Create a directory with the package name. This directory will serve as the container for all the modules that belong to the package.
2. Create an `__init__.py` file inside this directory. This file is crucial because it makes Python recognize the directory as a package. When you import the package, the code in `__init__.py` is executed, which can be used to initialize the package.
3. Move our Python module files into this directory. This step ensures that all the related code is grouped together within the package.

Let's create the package structure step by step:

1. First, create a directory called `structly`. This will be the root directory of our package.

```bash
mkdir structly
```

2. Next, create an empty `__init__.py` file inside the `structly` directory.

```bash
touch structly/__init__.py
```

The `__init__.py` file can be empty, but it's required to make Python treat the directory as a package. When you import the package, the code in `__init__.py` is executed, which can be used to initialize the package.

3. Now, let's move our Python module files into the `structly` directory. These module files contain the functions and classes that we want to include in our package.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Verify that all files have been moved correctly. We can use the `ls -l` command to list the contents of the `structly` directory.

```bash
ls -l structly/
```

You should see the following files listed:

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