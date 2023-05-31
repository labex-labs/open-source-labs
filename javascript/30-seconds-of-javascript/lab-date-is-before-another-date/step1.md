# Check if Date Is Before Another Date

> To start practicing coding, open the Terminal/SSH and type `node`.

Checks if a date is before another date.

- Use the less than operator (`<`) to check if the first date comes before the second one.

```js
const isBeforeDate = (dateA, dateB) => dateA < dateB;
```

```js
isBeforeDate(new Date(2010, 10, 20), new Date(2010, 10, 21)); // true
```
