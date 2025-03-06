# 创建转换为小写键的函数

既然你已经了解了如何访问对象的键并使用 `reduce()` 方法，那么让我们创建一个将对象的所有键转换为小写的函数。

在你的 Node.js 交互式 shell 中，定义以下函数：

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

下面来详细分析这个函数的工作原理：

1. `Object.keys(obj)` 获取输入对象的所有键
2. `.reduce()` 将这些键转换为一个新对象
3. 对于每个键，我们在累加器对象 (`acc`) 中创建一个新条目，其中：
   - 使用 `key.toLowerCase()` 将键转换为小写
   - 从输入对象中获取原始值 (`obj[key]`)
4. 我们以一个空对象 `{}` 作为累加器的初始值
5. 最后，返回累加器，它就是一个键为小写的新对象

现在，让我们使用之前创建的 `user` 对象来测试这个函数：

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

你应该会看到如下输出：

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

完美！所有的键现在都是小写了。

让我们再试一个例子，确保函数能正常工作：

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

输出应该是：

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

对于具有不同键大小写样式的不同对象，这个函数都能正常工作。
