# 일치하는 키 찾기

주어진 값과 일치하는 객체의 모든 키를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.keys()`를 사용하여 객체의 모든 프로퍼티를 가져옵니다.
3. `Array.prototype.filter()`를 사용하여 각 키 - 값 쌍을 테스트하고 주어진 값과 같은 모든 키를 반환합니다.

다음은 이 로직을 구현하는 예시 함수입니다.

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

이 함수는 다음과 같이 사용할 수 있습니다.

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
