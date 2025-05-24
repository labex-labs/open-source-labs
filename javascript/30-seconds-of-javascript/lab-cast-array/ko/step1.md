# JavaScript 에서 값을 배열로 변환하기

값을 배열로 변환하려면 아래 제공된 `castArray` 함수를 사용하십시오.

```js
const castArray = (val) => (Array.isArray(val) ? val : [val]);
```

이 함수를 사용하려면 변환하려는 값을 인수로 전달하십시오. 이 함수는 `Array.isArray()`를 사용하여 값이 이미 배열인지 확인합니다. 배열인 경우 함수는 그대로 반환합니다. 배열이 아닌 경우 함수는 값을 배열로 캡슐화하여 반환합니다.

`castArray`를 사용하는 방법의 예는 다음과 같습니다.

```js
castArray("foo"); // returns: ['foo']
castArray([1]); // returns: [1]
```

JavaScript 코딩을 연습하려면 터미널 또는 SSH 를 열고 `node`를 입력하십시오.
