# JavaScript 에서 배열의 첫 번째 요소 가져오는 방법

JavaScript 에서 배열의 첫 번째 요소를 가져오려면 `head` 함수를 사용할 수 있습니다. 사용 방법은 다음과 같습니다.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. 다음 코드를 사용하여 배열의 head 를 가져옵니다.

```js
const head = (arr) => (arr && arr.length ? arr[0] : undefined);
```

4. `head` 함수를 배열을 인수로 호출하여 첫 번째 요소를 가져옵니다. 배열이 비어 있거나 falsy (거짓) 값인 경우, 함수는 `undefined`를 반환합니다.

다음은 몇 가지 예시입니다.

```js
head([1, 2, 3]); // 1
head([]); // undefined
head(null); // undefined
head(undefined); // undefined
```
