# Regular Expressions

The challenge requires you to complete the code to perform various regular expression-related tasks in Golang.

## Requirements

- Use the `regexp` package to perform regular expression-related tasks.
- Use `MatchString` to test whether a pattern matches a string.
- Use `Compile` to optimize a `Regexp` struct.
- Use `MatchString` to test a match like `Compile`.
- Use `FindString` to find the match for the regexp.
- Use `FindStringIndex` to find the first match and return the start and end indexes for the match instead of the matching text.
- Use `FindStringSubmatch` to return information for both `p([a-z]+)ch` and `([a-z]+)`.
- Use `FindStringSubmatchIndex` to return information about the indexes of matches and submatches.
- Use `FindAllString` to find all matches for a regexp.
- Use `FindAllStringSubmatchIndex` to apply to all matches in the input, not just the first.
- Use `Match` to test a match with `[]byte` arguments and drop `String` from the function name.
- Use `MustCompile` to create global variables with regular expressions.
- Use `ReplaceAllString` to replace subsets of strings with other values.
- Use `ReplaceAllFunc` to transform matched text with a given function.

## Example

```sh
# For a complete reference on Go regular expressions check
# the [`regexp`](https://pkg.go.dev/regexp) package docs.
```
