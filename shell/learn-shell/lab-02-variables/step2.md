# Referencing Shell Variables

When referencing shell variables, there are a few scenarios where you need to use special syntax. Let's explore these cases.

1. Open the `variables.sh` file in the WebIDE.

2. Replace the content of the file with the following:

   ```bash
   #!/bin/bash
   
   PRICE_PER_APPLE=5
   MyFirstLetters=ABC
   greeting='Hello        world!'
   
   # Escaping special characters
   echo "The price of an Apple today is: \$HK $PRICE_PER_APPLE"
   
   # Avoiding ambiguity
   echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"
   
   # Preserving whitespace
   echo $greeting
   echo "$greeting"
   ```

3. Save the file.

4. Run the script:

   ```bash
   ./variables.sh
   ```

   You should see the following output:

   ```
   The price of an Apple today is: $HK 5
   The first 10 letters in the alphabet are: ABCDEFGHIJ
   Hello world!
   Hello        world!
   ```

   Note the differences:

   - The `$` sign is escaped in the first line to print it literally.
   - Curly braces `{}` are used to clearly define the variable name in the second line.
   - The last two lines show the difference between using quotes and not using quotes when referencing a variable with whitespace.
