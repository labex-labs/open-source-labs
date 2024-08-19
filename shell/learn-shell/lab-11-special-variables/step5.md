# Understanding the Difference Between $@ and $\*

The special variables `$@` and `$*` are both used to represent all command-line arguments, but they behave differently when enclosed in double quotes. Let's create a script to demonstrate this difference.

1. Create a new file named `at_vs_star.sh`:

```bash
touch ~/project/at_vs_star.sh
```

2. Open the file in the WebIDE editor and add the following content:

```bash
#!/bin/bash

echo "Using \$@:"
for arg in "$@"; do
  echo "Argument: $arg"
done

echo "Using \$*:"
for arg in "$*"; do
  echo "Argument: $arg"
done
```

This script demonstrates the difference between `$@` and `$*` when used in a loop.

3. Save the file and make it executable:

```bash
chmod +x ~/project/at_vs_star.sh
```

4. Run the script with multiple arguments, including some with spaces:

```bash
./at_vs_star.sh "arg with spaces" another_arg "third arg"
```

You should see output similar to this:

```
Using $@:
Argument: arg with spaces
Argument: another_arg
Argument: third arg
Using $*:
Argument: arg with spaces another_arg third arg
```

Here's what's happening:

- With `"$@"`, each argument is treated as a separate entity. Arguments with spaces are preserved as single units.
- With `"$*"`, all arguments are combined into a single string, separated by the first character of the IFS (Internal Field Separator) variable, which is usually a space.

This difference is crucial when you need to process arguments that might contain spaces or other special characters.
