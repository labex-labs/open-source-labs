# Understanding the Difference Between `$@` and `$*`

There is a difference in behavior when these special variables, `$@` and `$*`, are enclosed in double quotes. Let's see an example:

```shell
#!/bin/bash
function func {
    echo "--- \"\$*\""
    for ARG in "$*"
    do
        echo $ARG
    done

    echo "--- \"\$@\""
    for ARG in "$@"
    do
        echo $ARG
    done
}

func We are argument
```

In the above example, we define a function `func` that takes multiple arguments. We iterate over the `$*` and `$@` variables. When enclosed in double quotes, `$*` treats all arguments as a single word, whereas `$@` treats them as separate words.

Revise the file `~/project/special.sh` and run it again.

```text
Script Name: ./special.sh
--- "$*"
We are argument
--- "$@"
We
are
argument
```
