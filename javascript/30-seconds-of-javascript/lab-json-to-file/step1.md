# Writing JSON to a File

To write a JSON object to a file, follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the `fs.writeFileSync()` method, template literals, and `JSON.stringify()` to write a JSON object to a `.json` file.
3. The `JSONToFile` function below demonstrates how to implement this.

```js
const fs = require("fs");

const JSONToFile = (obj, filename) =>
  fs.writeFileSync(`${filename}.json`, JSON.stringify(obj, null, 2));

JSONToFile({ test: "is passed" }, "testJsonFile");
// writes the object to 'testJsonFile.json'
```

With these steps, you'll be able to write a JSON object to a file in no time!
