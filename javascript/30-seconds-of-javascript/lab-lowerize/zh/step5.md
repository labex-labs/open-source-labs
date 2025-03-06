# 创建可复用的模块

既然我们已经有了可用的函数，接下来让我们创建一个可复用的 JavaScript 模块文件，以便将其导入到其他项目中。

首先，通过连续按两次 Ctrl+C 或者输入 `.exit` 并按回车键来退出 Node.js 交互式 shell。

现在，在项目目录中创建一个名为 `object-utils.js` 的新文件：

1. 在 WebIDE 中，导航到左侧的文件资源管理器面板
2. 在项目目录中右键单击，然后选择“新建文件”
3. 将文件命名为 `object-utils.js`
4. 在文件中添加以下代码：

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

现在，让我们创建一个测试文件来验证模块是否能正常工作。创建一个名为 `test.js` 的新文件：

1. 在 WebIDE 中，导航到左侧的文件资源管理器面板
2. 在项目目录中右键单击，然后选择“新建文件”
3. 将文件命名为 `test.js`
4. 在文件中添加以下代码：

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

现在，让我们运行测试文件：

```bash
node test.js
```

你应该会看到类似于以下的输出：

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

恭喜！你已经成功创建了一个可复用的 JavaScript 模块，其中包含将对象键转换为小写的函数。现在，这个模块可以导入到你的任何 JavaScript 项目中。
