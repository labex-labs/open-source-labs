# Function to Add Minutes to Date

To add a specific number of minutes to a given date, use the following function:

```js
const addMinutesToDate = (date, n) => {
  // Create a Date object from the given date
  const d = new Date(date);
  // Add n minutes to the Date object
  d.setTime(d.getTime() + n * 60000);
  // Return a string representation of the new date in yyyy-mm-dd HH:MM:SS format
  return d.toISOString().split(".")[0].replace("T", " ");
};
```

To use this function, pass a string representation of the date as the first argument and the number of minutes to add (or subtract, if negative) as the second argument. For example:

```js
addMinutesToDate("2020-10-19 12:00:00", 10); // '2020-10-19 12:10:00'
addMinutesToDate("2020-10-19", -10); // '2020-10-18 23:50:00'
```

Note that the function returns the new date as a string in `yyyy-mm-dd HH:MM:SS` format.
