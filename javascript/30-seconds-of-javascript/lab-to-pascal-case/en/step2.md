# Working with Regular Expressions for Word Splitting

To convert a string to Pascal case, the first step is to split the string into individual words. We can use regular expressions (regex) to identify word boundaries regardless of the delimiter used (spaces, hyphens, underscores, etc.).

In JavaScript, regular expressions are enclosed between forward slashes (`/pattern/`). Let's explore how to use regex to split a string into words.

1. In your Node.js session, let's try a simple example first. Type the following code:

```javascript
let str = "hello_world-example";
let words = str.split(/[-_]/);
console.log(words);
```

The output should be:

```
[ 'hello', 'world', 'example' ]
```

This regex `/[-_]/` matches either a hyphen or an underscore, and `split()` uses these matches as separators.

2. Now, let's try a more complex string and regex. Type:

```javascript
let complexStr = "hello_WORLD-example phrase";
let regex =
  /[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+/g;
let matches = complexStr.match(regex);
console.log(matches);
```

The output should be:

```
[ 'hello', 'WORLD', 'example', 'phrase' ]
```

Let's break down this regex:

- `/[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)/`: Matches uppercase letter sequences
- `/[A-Z]?[a-z]+[0-9]*/`: Matches words that may begin with an uppercase letter
- `/[A-Z]/`: Matches single uppercase letters
- `/[0-9]+/`: Matches number sequences
- The `g` flag makes the matching global (finds all matches)

The `match()` method returns an array of all matches found in the string. This will be essential for our Pascal case converter since it can identify words in almost any format.
