# How to Create a Shallow Clone of an Object

To create a shallow clone of an object, use `Object.assign()` and an empty object (`{}`). Follow these steps:

1. Open the Terminal/SSH and type `node` to start practicing coding.
2. Use the following code to create a shallow clone of the original object:

```js
const shallowClone = (obj) => Object.assign({}, obj);
```

3. To clone the object, use the `shallowClone()` function as follows:

```js
const a = { x: true, y: 1 };
const b = shallowClone(a); // a !== b
```

In this example, `a` and `b` are two different objects, but they have the same values.
