# Exercise - Create ENGLISH_CALC Function

In this exercise, we will create a function called `ENGLISH_CALC` that can process sentences like `'3 plus 5'`, `'5 minus 1'`, or `'4 times 6'`, and print the results as `'3 + 5 = 8'`, `'5 - 1 = 4'`, or `'4 * 6 = 24'` respectively.

```bash
function ENGLISH_CALC {
  a=$1
  b=$3
  signn=$2
  if [ $signn == "plus" ]; then
    echo "$a + $b = $(($a+$b))"
  elif [ $signn == "minus" ]; then
    echo "$a - $b = $(($a-$b))"
  elif [ $signn == "times" ]; then
    echo "$a * $b = $(($a*$b))"
  fi
}

# Testing code
ENGLISH_CALC 3 plus 5
ENGLISH_CALC 5 minus 1
ENGLISH_CALC 4 times 6
```
