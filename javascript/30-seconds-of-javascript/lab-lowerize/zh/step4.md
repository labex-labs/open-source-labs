# 处理边界情况

我们的函数对于简单对象表现良好，但对于更复杂的情况呢？让我们来探索一些边界情况，看看我们的函数如何处理它们。

## 空对象

首先，让我们用一个空对象进行测试：

```javascript
lowerizeKeys({});
```

输出应该是一个空对象：

```
{}
```

## 包含嵌套对象的对象

如果对象包含嵌套对象会怎样呢？让我们试试看：

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

输出将是：

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

注意，只有顶级键 `User` 被转换为小写。嵌套对象内的键保持不变。

为了处理嵌套对象，我们需要修改函数以递归地处理所有对象。让我们创建一个增强版本：

```javascript
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
```

这个增强版函数：

1. 检查每个值是否也是一个对象（且不是数组或 null）
2. 如果是，则对该嵌套对象递归调用自身
3. 否则，使用原始值

让我们用嵌套对象来测试它：

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

现在你应该看到所有键都被转换为小写，即使是嵌套对象中的键：

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

干得好！你已经创建了一个可以处理嵌套对象的高级函数。
