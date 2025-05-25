# 터미널/SSH 에서 임의의 16 진수 색상 코드 생성하기

터미널/SSH 에서 임의의 16 진수 색상 코드를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력합니다.
3. 다음 코드를 사용하여 임의의 24 비트 (6 \* 4 비트) 16 진수를 생성합니다.

```js
const randomHexColorCode = () => {
  let n = (Math.random() * 0xfffff * 1000000).toString(16);
  return "#" + n.slice(0, 6);
};
```

4. 임의의 16 진수 색상 코드를 생성하려면 `randomHexColorCode()` 함수를 호출합니다.

예시:

```js
randomHexColorCode(); // '#e34155'
```

이렇게 하면 코딩 프로젝트에서 사용할 수 있는 임의의 16 진수 색상 코드가 생성됩니다.
