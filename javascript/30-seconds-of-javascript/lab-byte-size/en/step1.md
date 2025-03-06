# Understanding JavaScript String Representation

Before we calculate the byte size of strings, it is important to understand how strings are represented in JavaScript.

In JavaScript, strings are sequences of UTF-16 code units. This means that characters like emojis or certain symbols may take more than one byte to represent. For example, a simple English letter takes 1 byte, but an emoji might take 4 bytes.

Let's start by launching Node.js in the terminal:

1. Open the Terminal by clicking on the terminal icon in the WebIDE interface
2. Type the following command and press Enter:

```bash
node
```

You should now be in the Node.js interactive console, which looks something like this:

```
Welcome to Node.js v14.x.x.
Type ".help" for more information.
>
```

![Open the node](../assets/screenshot-20250306-cFJ9GgLX@2x.png)

In this console, we can experiment with JavaScript code directly. Try typing the following command to see the length of a string:

```javascript
"Hello World".length;
```

You should see the output:

```
11
```

This gives us the character count, but not the actual byte size. The character count and byte size can be different, especially with special characters. Let's explore this further in the next step.
