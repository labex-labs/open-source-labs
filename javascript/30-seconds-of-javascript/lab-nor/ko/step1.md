# JavaScript 에서 논리 Nor 사용 방법

JavaScript 코딩을 시작하려면 터미널/SSH 에 접속하여 `node`를 입력하십시오. 논리 Nor 는 주어진 인자 중 어느 것도 참이 아닌지 확인합니다. 두 값의 논리적 OR 의 반전을 반환하려면 논리적 NOT (`!`) 연산자를 사용하십시오. 다음은 예시입니다.

```js
const nor = (a, b) => !(a || b);
```

다음은 몇 가지 출력 결과입니다.

```js
nor(true, true); // false
nor(true, false); // false
nor(false, false); // true
```
