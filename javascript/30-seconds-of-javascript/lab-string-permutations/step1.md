# String Permutations Algorithm

To generate all permutations of a string that contains duplicates, use the following algorithm:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use recursion to create all possible permutations of the given string.
3. For each letter in the given string, create all the partial permutations for the rest of its letters.
4. Use `Array.prototype.map()` to combine the letter with each partial permutation.
5. Use `Array.prototype.reduce()` to combine all permutations in one array.
6. Base cases are for `String.prototype.length` equal to `2` or `1`.
7. ⚠️ **WARNING**: The execution time increases exponentially with each character. For strings with more than 8 to 10 characters, the environment may hang as it tries to solve all the different combinations.

Here's the JavaScript code for the algorithm:

```js
const stringPermutations = (str) => {
  if (str.length <= 2) return str.length === 2 ? [str, str[1] + str[0]] : [str];
  return str
    .split("")
    .reduce(
      (acc, letter, i) =>
        acc.concat(
          stringPermutations(str.slice(0, i) + str.slice(i + 1)).map(
            (val) => letter + val,
          ),
        ),
      [],
    );
};
```

You can test the `stringPermutations` function with the following code:

```js
stringPermutations("abc"); // ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
