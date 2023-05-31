# Number of Days in Month

> To start practicing coding, open the Terminal/SSH and type `node`.

Gets the number of days in the given `month` of the specified `year`.

- Use the `Date` constructor to create a date from the given `year` and `month`.
- Set the days parameter to `0` to get the last day of the previous month, as months are zero-indexed.
- Use `Date.prototype.getDate()` to return the number of days in the given `month`.

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

```js
daysInMonth(2020, 12)); // 31
daysInMonth(2024, 2)); // 29
```
