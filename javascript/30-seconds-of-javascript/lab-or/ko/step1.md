# JavaScript 에서 논리 OR 연산자 사용하기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 논리 OR 연산자 (`||`) 는 주어진 인자 중 적어도 하나가 `true`인지 확인합니다.

다음은 논리 OR 연산자를 사용하는 예시입니다.

```js
const or = (a, b) => a || b;
```

다음은 연산자를 사용할 때의 몇 가지 출력 예시입니다.

```js
or(true, true); // true
or(true, false); // true
or(false, false); // false
```
