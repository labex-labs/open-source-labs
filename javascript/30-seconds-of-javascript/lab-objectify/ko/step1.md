# JavaScript 에서 배열을 객체로 매핑하는 방법

JavaScript 에서 객체 배열을 객체로 매핑하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 배열을 객체로 매핑합니다.
3. 객체의 키를 매핑하려면 `mapKey` 매개변수를 사용하고, 값을 매핑하려면 `mapValue` 매개변수를 사용합니다.

다음은 `objectify` 함수를 사용하여 객체 배열을 객체로 매핑하는 방법을 보여주는 코드 스니펫입니다.

```js
const objectify = (arr, mapKey, mapValue = (i) => i) =>
  arr.reduce((acc, item) => {
    acc[mapKey(item)] = mapValue(item);
    return acc;
  }, {});
```

그런 다음 `objectify` 함수를 사용하여 다음과 같은 방식으로 객체 배열을 객체로 매핑할 수 있습니다.

```js
const people = [
  { name: "John", age: 42 },
  { name: "Adam", age: 39 }
];

// name 속성을 키로 사용하여 객체 배열을 객체로 매핑합니다.
objectify(people, (p) => p.name.toLowerCase());
// Output: { john: { name: 'John', age: 42 }, adam: { name: 'Adam', age: 39 } }

// name 속성을 키로, age 속성을 값으로 사용하여 객체 배열을 객체로 매핑합니다.
objectify(
  people,
  (p) => p.name.toLowerCase(),
  (p) => p.age
);
// Output: { john: 42, adam: 39 }
```
