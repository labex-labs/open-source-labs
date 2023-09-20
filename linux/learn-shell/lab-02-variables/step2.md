# Referencing Shell Variables

To reference a shell variable, you can simply use its name. However, there are a few scenarios where you need to use special syntax.

## Escaping Special Characters

If you want to include special characters in a variable's value, you need to escape them using a backslash "\\".

```bash
PRICE_PER_APPLE=5
echo "The price of an Apple today is: \$HK $PRICE_PER_APPLE"
```

## Avoiding Ambiguity

To avoid any ambiguity in variable substitution, you can enclose the variable name with `{}`.

```bash
MyFirstLetters=ABC
echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"
```

## Preserving Whitespace

If the variable value contains whitespace, you can preserve it by enclosing the variable name with `""`.

```bash
greeting='Hello        world!'
echo $greeting" now with spaces: $greeting"
```

Run the script and you will see the following output:

```bash
cd ~/project
chmod +x variables.sh
./variables.sh
```

```text
The price of an Apple today is: $HK 5
The first 10 letters in the alphabet are: ABCDEFGHIJ
Hello world! now with spaces: Hello        world!
```
