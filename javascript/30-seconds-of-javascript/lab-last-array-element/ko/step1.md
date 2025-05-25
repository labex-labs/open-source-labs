# JavaScript 에서 배열의 마지막 요소 가져오는 방법

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 다음 함수는 배열의 마지막 요소를 반환합니다.

```js
const last = (arr) => (arr && arr.length ? arr[arr.length - 1] : undefined);
```

이 함수를 사용하려면 인수로 배열을 제공해야 합니다. 이 함수는 배열이 truthy(참 같은 값) 인지, 그리고 `length` 속성을 가지고 있는지 확인합니다. 두 조건이 모두 참이면 배열의 마지막 요소의 인덱스를 계산하여 반환합니다. 그렇지 않으면 `undefined`를 반환합니다.

다음은 몇 가지 예시입니다.

```js
last([1, 2, 3]); // 3
last([]); // undefined
last(null); // undefined
last(undefined); // undefined
```
