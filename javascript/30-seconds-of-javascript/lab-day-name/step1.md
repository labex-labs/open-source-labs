# Retrieving Day Name from a Date Object

To retrieve the name of the weekday from a `Date` object, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use `Date.prototype.toLocaleDateString()` with the `{ weekday: 'long' }` option to retrieve the weekday.
3. You can use the optional second argument to get a language-specific name or omit it to use the default locale.

Here's an example implementation:

```js
const dayName = (date, locale) =>
  date.toLocaleDateString(locale, { weekday: "long" });
```

You can use this function like this:

```js
dayName(new Date()); // 'Saturday'
dayName(new Date("09/23/2020"), "de-DE"); // 'Samstag'
```
