# Substring Extraction

To extract a substring from a string, use the `${STRING:$POS:$LEN}` syntax. Here's an example:

```bash
STRING="this is a string"
POS=1
LEN=3
echo ${STRING:$POS:$LEN} # Outputs: "his"
```

If you omit `:$LEN`, the substring will be extracted from $POS to the end of the string.

```text
his
```
