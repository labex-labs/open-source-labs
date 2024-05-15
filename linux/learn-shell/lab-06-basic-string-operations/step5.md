# Substring Replacement

To replace substrings in a string, you can use various syntaxes. Here are some examples:

- Replace the first occurrence of a substring with replacement:

```bash
STRING="to be or not to be"
echo ${STRING[@]/be/eat} # Outputs: "to eat or not to be"
```

- Replace all occurrences of a substring:

```bash
STRING="to be or not to be"
echo ${STRING[@]//be/eat} # Outputs: "to eat or not to eat"
```

- Delete all occurrences of a substring (replace with an empty string):

```bash
STRING="to be or not to be"
echo ${STRING[@]// not/} # Outputs: "to be or to be"
```

- Replace the occurrence of a substring if it's at the beginning of the string:

```bash
STRING="to be or not to be"
echo ${STRING[@]/#to be/eat now} # Outputs: "eat now or not to be"
```

- Replace the occurrence of a substring if it's at the end of the string:

```bash
STRING="to be or not to be"
echo ${STRING[@]/%be/eat} # Outputs: "to be or not to eat"
```

- Replace the occurrence of a substring with shell command output:

```bash
STRING="to be or not to be"
echo ${STRING[@]/%be/be on $(date +%Y-%m-%d)} # Outputs: "to be or not to be on 2022-05-10"
```
