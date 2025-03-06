# Understanding ISO Date Format and JavaScript Date Objects

Before we start coding, let us understand what the ISO 8601 date format is and how JavaScript handles dates.

## The ISO 8601 Date Format

The ISO 8601 format is an international standard for representing dates and times. The simplified extended ISO format looks like this:

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

Where:

- `YYYY` represents the year (four digits)
- `MM` represents the month (two digits)
- `DD` represents the day (two digits)
- `T` is a literal character separating the date and time
- `HH` represents hours (two digits)
- `mm` represents minutes (two digits)
- `ss` represents seconds (two digits)
- `sss` represents milliseconds (three digits)
- `Z` indicates UTC timezone (Zulu time)

For example, `2023-05-12T14:30:15.123Z` represents May 12, 2023, at 2:30:15.123 PM UTC.

## The JavaScript Date Object

JavaScript provides a built-in `Date` object for working with dates and times. When you create a new `Date` object, you can pass an ISO-formatted string to it:

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

Let us open the terminal and practice working with Date objects:

1. Open the Terminal by clicking on the Terminal menu at the top of the WebIDE
2. Type `node` and press Enter to start the Node.js interactive shell
3. Create a new Date object for the current time:

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. Convert this Date object to an ISO string:

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

You should see output similar to:

```
2023-05-12T14:30:15.123Z
```

5. Create a Date from an ISO string:

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

This demonstrates how JavaScript can parse and create Date objects from ISO formatted strings.
