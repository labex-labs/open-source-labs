# Create Directory if Not Exists

> To start practicing coding, open the Terminal/SSH and type `node`.

Creates a directory, if it does not exist.

- Use `fs.existsSync()` to check if the directory exists, `fs.mkdirSync()` to create it.

```js
const fs = require('fs');

const createDirIfNotExists = dir =>
  !fs.existsSync(dir) ? fs.mkdirSync(dir) : undefined;
```

```js
createDirIfNotExists('test');
// creates the directory 'test', if it doesn't exist
```
