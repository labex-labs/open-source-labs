# 논리 XOR (Logical Xor)

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 논리 XOR 은 인자 중 하나만 `true`인지 확인합니다. 논리 XOR 을 생성하려면 두 개의 주어진 값에 논리 OR (`||`), AND (`&&`), NOT (`!`) 연산자를 사용하십시오. 다음은 이에 대한 예시 코드입니다.

```js
const xor = (a, b) => (a || b) && !(a && b);
```

다음은 출력 값입니다.

```js
xor(true, true); // false
xor(true, false); // true
xor(false, true); // true
xor(false, false); // false
```
