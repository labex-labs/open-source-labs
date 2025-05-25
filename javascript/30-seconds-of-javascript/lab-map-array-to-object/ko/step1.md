# 배열을 객체에 매핑하기

함수를 사용하여 배열의 값을 객체에 매핑하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 `arr`의 각 요소에 `fn`을 적용하고 결과를 객체로 결합합니다.
3. 각 속성의 키로 `el`을 사용하고, `fn`의 결과를 값으로 사용합니다.

다음은 코드 스니펫 예시입니다.

```js
const mapObject = (arr, fn) =>
  arr.reduce((acc, el, i) => {
    acc[el] = fn(el, i, arr);
    return acc;
  }, {});
```

이 예제와 같이 `mapObject` 함수를 사용할 수 있습니다.

```js
mapObject([1, 2, 3], (a) => a * a); // { 1: 1, 2: 4, 3: 9 }
```
