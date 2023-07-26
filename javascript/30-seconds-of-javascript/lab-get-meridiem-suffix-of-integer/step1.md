# How to Get the Meridiem Suffix of an Integer

To get started with coding, open the Terminal/SSH and type `node`.

Here's a function that converts an integer to a 12-hour format string with a meridiem suffix.

To do this, use the modulo operator (`%`) and conditional checks.

```js
const getMeridiemSuffixOfInteger = (num) => {
  if (num === 0 || num === 24) {
    return "12am";
  } else if (num === 12) {
    return "12pm";
  } else if (num < 12) {
    return num + "am";
  } else {
    return (num % 12) + "pm";
  }
};
```

Here are some examples of how to use this function:

```js
getMeridiemSuffixOfInteger(0); // '12am'
getMeridiemSuffixOfInteger(11); // '11am'
getMeridiemSuffixOfInteger(13); // '1pm'
getMeridiemSuffixOfInteger(25); // '1pm'
```

This function takes an integer as an argument and returns a string with the meridiem suffix.
