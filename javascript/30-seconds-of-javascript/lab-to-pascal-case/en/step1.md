# Understanding Pascal Case and Setting Up the Environment

Pascal case is a naming convention where:

- The first letter of each word is capitalized
- No spaces, hyphens, or underscores are used between words
- All other letters are lowercase

For example:

- "hello world" → "HelloWorld"
- "user_name" → "UserName"
- "first-name" → "FirstName"

Let's start by setting up our development environment.

1. Open the Terminal from the WebIDE interface by clicking on "Terminal" in the top menu bar.

2. Start a Node.js interactive session by typing the following command in the Terminal and pressing Enter:

```bash
node
```

You should see the Node.js prompt (`>`) appear, indicating that you are now in the Node.js interactive environment.

3. Let's try a simple string manipulation to get warmed up. Type the following code at the Node.js prompt:

```javascript
let name = "john doe";
let capitalizedFirstLetter = name.charAt(0).toUpperCase() + name.slice(1);
console.log(capitalizedFirstLetter);
```

The output should be:

```
John doe
```

This simple example demonstrates how to capitalize the first letter of a string. We used:

- `charAt(0)` to get the first character
- `toUpperCase()` to convert it to uppercase
- `slice(1)` to get the rest of the string
- Concatenation with `+` to combine them

These string methods will be helpful as we build our Pascal case converter.
