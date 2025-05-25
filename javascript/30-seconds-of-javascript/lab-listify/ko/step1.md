# JavaScript 에서 객체를 배열로 매핑하는 방법

JavaScript 에서 객체를 배열로 매핑하려면 `listify()` 함수를 사용할 수 있습니다. 방법은 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. `Object.entries()`를 사용하여 객체의 키 - 값 쌍의 배열을 가져옵니다.

3. `Array.prototype.reduce()`를 사용하여 배열을 객체로 매핑합니다.

4. `mapFn`을 사용하여 객체의 키와 값을 매핑하고 `Array.prototype.push()`를 사용하여 매핑된 값을 배열에 추가합니다.

다음은 `listify()` 함수의 코드입니다.

```js
const listify = (obj, mapFn) =>
  Object.entries(obj).reduce((acc, [key, value]) => {
    acc.push(mapFn(key, value));
    return acc;
  }, []);
```

다음은 `people`이라는 객체와 함께 사용하는 예시입니다.

```js
const people = { John: { age: 42 }, Adam: { age: 39 } };
listify(people, (key, value) => ({ name: key, ...value }));
// [ { name: 'John', age: 42 }, { name: 'Adam', age: 39 } ]
```

이 함수를 사용하면 JavaScript 에서 객체를 배열로 쉽게 매핑할 수 있습니다.
