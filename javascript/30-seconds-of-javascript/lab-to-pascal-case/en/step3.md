# Capitalizing Each Word

Now that we can split a string into words, we need to capitalize the first letter of each word and make the rest lowercase. Let's implement this functionality.

1. In your Node.js session, let's write a function to capitalize a single word. Type:

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

The output should be:

```
Hello
World
Javascript
```

2. Now, let's apply this function to an array of words using the `map()` method. Type:

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

The output should be:

```
[ 'Hello', 'World', 'Javascript' ]
```

The `map()` method creates a new array by applying a function to each element of the original array. In this case, we're applying our `capitalizeWord` function to each word.

3. Finally, let's join the capitalized words together to form a Pascal case string:

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

The output should be:

```
HelloWorldJavascript
```

The `join("")` method combines all elements of an array into a single string, using the provided delimiter (an empty string in this case) between each element.

These steps demonstrate the core process of converting a string to Pascal case:

1. Split the string into words
2. Capitalize each word
3. Join the words without any separators
