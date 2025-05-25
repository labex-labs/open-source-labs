# JavaScript 에서 객체 키 이름 변경 방법

제공된 값으로 여러 객체 키의 이름을 변경하려면 `renameKeys` 함수를 사용할 수 있습니다. 따라야 할 단계는 다음과 같습니다.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 `Array.prototype.reduce()` 및 스프레드 연산자 (`...`) 와 함께 사용하여 객체의 키를 가져와 `keysMap`에 따라 이름을 변경합니다.
3. `keysMap`과 객체 (`obj`) 를 `renameKeys` 함수에 인수로 전달합니다.
4. `renameKeys` 함수는 이름이 변경된 키를 가진 새로운 객체를 반환합니다.

`renameKeys` 함수를 사용하는 예는 다음과 같습니다.

```js
const renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );

const obj = { name: "Bobo", job: "Front-End Master", shoeSize: 100 };
renameKeys({ name: "firstName", job: "passion" }, obj);
// { firstName: 'Bobo', passion: 'Front-End Master', shoeSize: 100 }
```
