# 객체를 키 - 값 쌍의 배열로 변환하기

객체를 키 - 값 쌍의 배열로 변환하려면 `Object.keys()` 메서드와 `Array.prototype.map()` 메서드를 사용합니다. 이렇게 하면 객체의 키를 반복하고 키 - 값 쌍이 있는 배열을 생성합니다. 또는 유사한 기능을 제공하는 `Object.entries()` 메서드를 사용할 수도 있습니다.

다음은 객체를 키 - 값 쌍의 배열로 변환하는 방법을 보여주는 코드 조각입니다.

```js
const objectToEntries = (obj) => Object.keys(obj).map((k) => [k, obj[k]]);
```

`objectToEntries()` 함수를 사용하여 객체를 다음과 같이 키 - 값 쌍의 배열로 변환할 수 있습니다.

```js
objectToEntries({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```
