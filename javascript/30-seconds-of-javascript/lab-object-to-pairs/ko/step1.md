# 객체를 키 - 값 쌍의 배열로 변환하기

객체를 키 - 값 쌍의 배열로 변환하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Object.entries()` 메서드를 사용하여 객체로부터 키 - 값 쌍 배열의 배열을 얻습니다.
3. 객체를 인수로 받아 키 - 값 쌍의 배열을 반환하는 `objectToPairs`라는 함수를 생성합니다.
4. 예시 객체로 `objectToPairs` 함수를 호출하여 출력을 테스트합니다.

다음은 예시 구현입니다.

```js
const objectToPairs = (obj) => Object.entries(obj);
objectToPairs({ a: 1, b: 2 }); // [ ['a', 1], ['b', 2] ]
```

이러한 단계를 따르면 JavaScript 를 사용하여 객체를 키 - 값 쌍의 배열로 쉽게 변환할 수 있습니다.
