# Running Selected Tests and Using Test Discovery

The unittest module provides several ways to run specific tests or automatically discover and run all tests in your project.

## Running Specific Tests

You can run specific test methods or test classes by using the pattern option with the unittest module.

1. To run just the tests related to creating a Stock object:

```bash
python3 -m unittest teststock.TestStock.test_create
```

2. To run all tests in the TestStock class:

```bash
python3 -m unittest teststock.TestStock
```

## Using Test Discovery

The unittest module can automatically discover and run all test files in your project.

1. Rename the current file to follow the test discovery naming pattern:

```bash
mv teststock.py test_stock.py
```

2. Run the test discovery:

```bash
python3 -m unittest discover
```

This will find and run all test files that match the pattern `test_*.py` in the current directory.

3. You can also specify a directory to search for tests:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Where:

- `-s .` specifies the directory to start discovery (current directory in this case)
- `-p "test_*.py"` is the pattern to match test files

You should see all 12 tests run and pass, just like before.

4. Rename the file back to the original name for consistency with the lab:

```bash
mv test_stock.py teststock.py
```

By using test discovery, you can easily run all tests in a project without having to specify each test file individually.
