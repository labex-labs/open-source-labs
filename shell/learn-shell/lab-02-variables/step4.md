# Arithmetic Operations

Shell variables can also be used in arithmetic operations. Bash provides the `$((expression))` syntax for performing arithmetic.

1. Create a new file named `arithmetic.sh` in the `/home/labex/project` directory:

   ```bash
   touch /home/labex/project/arithmetic.sh
   ```

2. Open the `arithmetic.sh` file in the WebIDE and add the following content:

   ```bash
   #!/bin/bash
   
   X=10
   Y=5
   
   # Addition
   SUM=$((X + Y))
   echo "Sum of $X and $Y is: $SUM"
   
   # Subtraction
   DIFF=$((X - Y))
   echo "Difference between $X and $Y is: $DIFF"
   
   # Multiplication
   PRODUCT=$((X * Y))
   echo "Product of $X and $Y is: $PRODUCT"
   
   # Division
   QUOTIENT=$((X / Y))
   echo "Quotient of $X divided by $Y is: $QUOTIENT"
   
   # Modulus (remainder)
   REMAINDER=$((X % Y))
   echo "Remainder of $X divided by $Y is: $REMAINDER"
   
   # Increment
   X=$((X + 1))
   echo "After incrementing, X is now: $X"
   
   # Decrement
   Y=$((Y - 1))
   echo "After decrementing, Y is now: $Y"
   ```

3. Save the file.

4. Make the script executable:

   ```bash
   chmod +x /home/labex/project/arithmetic.sh
   ```

5. Run the script:

   ```bash
   ./arithmetic.sh
   ```

   You should see the following output:

   ```
   Sum of 10 and 5 is: 15
   Difference between 10 and 5 is: 5
   Product of 10 and 5 is: 50
   Quotient of 10 divided by 5 is: 2
   Remainder of 10 divided by 5 is: 0
   After incrementing, X is now: 11
   After decrementing, Y is now: 4
   ```

   This script demonstrates various arithmetic operations using shell variables.
