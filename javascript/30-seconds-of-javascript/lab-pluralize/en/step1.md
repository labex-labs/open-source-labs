# Pluralize String

To pluralize a word based on a given number, use the `pluralize` function. Start by opening the Terminal/SSH and typing `node`. This function can return either the singular or plural form of the word, depending on the input number. You can also supply an optional dictionary to use custom plural forms.

To define the `pluralize` function, use a closure that takes in the `word` and an optional `plural` form. If the input `num` is either `-1` or `1`, return the singular form of the `word`. Otherwise, return the `plural` form. If no custom `plural` form is supplied, the function will use the default of the singular `word` + `s`.

If the first argument is an object, the `pluralize` function returns a new function that can use the supplied dictionary to resolve the correct plural form of the `word`.

Here is the `pluralize` function in action:

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

You can use the `pluralize` function like this:

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

If you have a dictionary of custom plural forms, you can create an `autoPluralize` function that automatically uses the correct plural form for a given `word`:

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
