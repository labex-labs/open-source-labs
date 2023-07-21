# Closures

## Introduction

In this lab, you will learn how to use anonymous functions to create closures in Golang.

You need to create a function that returns another function. The returned function should increment a variable by one each time it is called. The variable should be unique to each returned function.

- The function `intSeq` should return another function.
- The returned function should increment a variable by one each time it is called.
- The variable should be unique to each returned function.

## TODO

```go
func intSeq() func() int {
    i := 0
    return func() int {
        // TODO: Increment i by one each time this function is called.
        // TODO: Return the new value of i.
    }
}
```

```
1
2
3
1
```

## Summary

In this lab, you learned how to use anonymous functions to create closures in Golang. Closures are useful when you want to define a function inline without having to name it.
