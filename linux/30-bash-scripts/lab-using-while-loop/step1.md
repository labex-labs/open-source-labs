# Using While Loop

Create a Bash file named **while_example.sh** that demonstrates the use of the **while** loop. In the example, the **while** loop should iterate for **5** times. The value of a variable named **count** should increment by **1** in each step. When the value of **count** variable reaches 5, the **while** loop should terminate.

- The Bash file should be named **while_example.sh**.
- The **while** loop should iterate for 5 times.
- The value of a variable named **count** should increment by 1 in each step.
- When the value of **count** variable reaches 5, the **while** loop should terminate.
- The Bash file should be executable.
- The Bash file should output the value of **count** in each iteration of the **while** loop.
- The Bash file should terminate after the **while** loop ends.

```bash
#!/bin/bash
valid=true
count=1
while $valid; do
  echo $count
  if [ $count -eq 5 ]; then
    break
  fi
  ((count++))
done
```

To run the Bash file, use the following command:

```
bash while_example.sh
```
