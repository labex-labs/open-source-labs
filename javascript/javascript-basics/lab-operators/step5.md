# Not, Does-not-equal

This returns the logically opposite value of what it precedes. It turns a `true` into a `false`, etc.. When it is used alongside the Equality operator, the negation operator tests whether two values are not equal.

For "Not", the basic expression is true, but the comparison returns `false` because we negate it:

```js
// Not(!)
let myVariable = 3;
!(myVariable === 3);
```

"Does-not-equal" gives basically the same result with different syntax. Here we are testing "is `myVariable` NOT equal to 3". This returns `false` because `myVariable` IS equal to 3:

```js
// Does-not-equal(!==)
let myVariable = 3;
myVariable !== 3;
```

There are a lot more operators to explore, but this is enough for now. See [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) for a complete list.

> **Note:** Mixing data types can lead to some strange results when performing calculations. Be careful that you are referring to your variables correctly, and getting the results you expect. For example, enter `'35' + '25'` into your console. Why don't you get the result you expected? Because the quote marks turn the numbers into strings, so you've ended up concatenating strings rather than adding numbers. If you enter `35 + 25` you'll get the total of the two numbers.
