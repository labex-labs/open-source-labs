# JavaScript 에서 객체 키를 대문자로 변환하는 방법

JavaScript 에서 객체의 모든 키를 대문자로 변환하려면 다음 단계를 따르세요.

1. `Object.keys()`를 사용하여 객체의 키 배열을 가져옵니다.
2. `Array.prototype.reduce()`를 사용하여 배열을 객체로 매핑합니다.
3. `String.prototype.toUpperCase()`를 사용하여 키를 대문자로 변환합니다.

다음은 코드입니다.

```js
const upperize = (obj) =>
  Object.keys(obj).reduce((acc, k) => {
    acc[k.toUpperCase()] = obj[k];
    return acc;
  }, {});
```

함수를 테스트하려면 다음과 같이 호출할 수 있습니다.

```js
upperize({ Name: "John", Age: 22 }); // { NAME: 'John', AGE: 22 }
```
