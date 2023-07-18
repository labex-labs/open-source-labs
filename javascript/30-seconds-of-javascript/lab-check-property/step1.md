# Property Checker

To check if a specific property of an object meets a certain condition, use the `checkProp` function. This function creates a curried function that takes a predicate function and a property name as arguments. The returned function then takes an object and returns `true` or `false` based on whether the specified property meets the condition specified by the predicate function.

Here's an example implementation of `checkProp`:

```js
const checkProp = (predicate, prop) => (obj) => !!predicate(obj[prop]);
```

And here are some examples of how you might use it:

```js
const lengthIs4 = checkProp((l) => l === 4, "length");
lengthIs4([]); // false
lengthIs4([1, 2, 3, 4]); // true
lengthIs4(new Set([1, 2, 3, 4])); // false (Set uses Size, not length)

const session = { user: {} };
const validUserSession = checkProp((u) => u.active && !u.disabled, "user");

validUserSession(session); // false

session.user.active = true;
validUserSession(session); // true

const noLength = checkProp((l) => l === undefined, "length");
noLength([]); // false
noLength({}); // true
noLength(new Set()); // true
```

In summary, the `checkProp` function allows you to easily check the value of a specific property on an object by specifying a predicate function for that property.
