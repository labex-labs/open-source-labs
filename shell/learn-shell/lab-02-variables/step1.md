# Creating Shell Variables

Shell variables are created by assigning a value to them using the `=` sign. Let's start by creating a simple shell script that defines some variables.

1. Open a terminal in your WebIDE (VS Code).

2. Create a new file named `variables.sh` in the `/home/labex/project` directory:

   ```bash
   touch /home/labex/project/variables.sh
   ```

3. Open the `variables.sh` file in the WebIDE and add the following content:

   ```bash
   #!/bin/bash
   
   PRICE_PER_APPLE=5
   MyFirstLetters=ABC
   greeting='Hello        world!'
   
   echo "Price per apple: $PRICE_PER_APPLE"
   echo "My first letters: $MyFirstLetters"
   echo "Greeting: $greeting"
   ```

   In this script, we've created three variables:

   - `PRICE_PER_APPLE`: An integer variable
   - `MyFirstLetters`: A string variable
   - `greeting`: A string variable with multiple spaces

4. Save the file.

5. Make the script executable:

   ```bash
   chmod +x /home/labex/project/variables.sh
   ```

6. Run the script:

   ```bash
   ./variables.sh
   ```

   You should see the following output:

   ```
   Price per apple: 5
   My first letters: ABC
   Greeting: Hello world!
   ```

   Notice that the extra spaces in the `greeting` variable are not preserved in the output.
