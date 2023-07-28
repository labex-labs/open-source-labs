# Conditionals

> Open the Terminal/SSH and type node to start practicing coding.

Conditionals are code structures used to test if an expression returns true or not. A very common form of conditionals is the `if...else` statement. For example:

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  alert("Yay, I love chocolate ice cream!");
} else {
  alert("Awwww, but chocolate is my favorite…");
}
```

The expression inside the `if ()` is the test. This uses the strict equality operator (as described above) to compare the variable `iceCream` with the string `chocolate` to see if the two are equal. If this comparison returns `true`, the first block of code runs. If the comparison is not true, the second block of code—after the `else` statement—runs instead.
