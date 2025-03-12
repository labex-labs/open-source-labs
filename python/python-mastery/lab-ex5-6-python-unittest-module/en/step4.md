# Running Selected Tests and Using Test Discovery

The `unittest` module in Python is a powerful tool that allows you to test your code effectively. It provides several ways to run specific tests or automatically discover and run all tests in your project. This is very useful because it helps you focus on specific parts of your code during testing or quickly check the entire project's test suite.

## Running Specific Tests

Sometimes, you may want to run only specific test methods or test classes instead of the entire test suite. You can achieve this by using the pattern option with the `unittest` module. This gives you more control over which tests are executed, which can be handy when you're debugging a particular part of your code.

1. To run just the tests related to creating a Stock object:

```bash
python3 -m unittest teststock.TestStock.test_create
```

In this command, `python3 -m unittest` tells Python to run the `unittest` module. `teststock` is the name of the test file, `TestStock` is the name of the test class, and `test_create` is the specific test method we want to run. By running this command, you can quickly check if the code related to creating a `Stock` object is working as expected.

2. To run all tests in the `TestStock` class:

```bash
python3 -m unittest teststock.TestStock
```

Here, we omit the specific test method name. So, this command will execute all the test methods within the `TestStock` class in the `teststock` file. This is useful when you want to check the overall functionality of the `Stock` object's test cases.

## Using Test Discovery

The `unittest` module can automatically discover and run all test files in your project. This saves you the trouble of manually specifying each test file to run, especially in larger projects with many test files.

1. Rename the current file to follow the test discovery naming pattern:

```bash
mv teststock.py test_stock.py
```

The test discovery mechanism in `unittest` looks for files that follow the naming pattern `test_*.py`. By renaming the file to `test_stock.py`, we make it easier for the `unittest` module to find and run the tests in this file.

2. Run the test discovery:

```bash
python3 -m unittest discover
```

This command tells the `unittest` module to automatically discover and run all test files that match the pattern `test_*.py` in the current directory. It will search through the directory and execute all the test cases found in the matching files.

3. You can also specify a directory to search for tests:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Where:

- `-s .` specifies the directory to start discovery (current directory in this case). The dot (`.`) represents the current directory. You can change this to another directory path if you want to search for tests in a different location.
- `-p "test_*.py"` is the pattern to match test files. This ensures that only files with names starting with `test_` and having the `.py` extension are considered as test files.

You should see all 12 tests run and pass, just like before.

4. Rename the file back to the original name for consistency with the lab:

```bash
mv test_stock.py teststock.py
```

After running the test discovery, we rename the file back to its original name to keep the lab environment consistent.

By using test discovery, you can easily run all tests in a project without having to specify each test file individually. This makes the testing process more efficient and less error-prone.
