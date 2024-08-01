# Index

To find the position of a character or substring in a string, use the `expr index` command. Here's an example:

```bash
STRING="this is a string"
SUBSTRING="hat"
expr index "$STRING" "$SUBSTRING" # Outputs: 1 (position of the first 't' in $STRING)
```

```text
1
```
