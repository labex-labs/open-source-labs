# Function to Create Directory if Not Exists

To create a directory, use the `createDirIfNotExists` function. It checks if the directory already exists with `fs.existsSync()`, and creates the directory with `fs.mkdirSync()` if it does not exist.

```js
const fs = require("fs");

const createDirIfNotExists = (dir) =>
  !fs.existsSync(dir) ? fs.mkdirSync(dir) : undefined;
```

To use the function, type `createDirIfNotExists('directory-name')`. For example, `createDirIfNotExists('test')` will create the directory 'test' if it does not exist. Then, to start practicing coding, open the Terminal/SSH and type `node`.
