# 두 URL 이 동일한 오리진에 있는지 확인하기

두 URL 이 동일한 오리진에 있는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.

2. `URL.protocol` 및 `URL.host`를 사용하여 두 URL 이 동일한 프로토콜과 호스트를 갖는지 확인합니다.

```js
const isSameOrigin = (origin, destination) =>
  origin.protocol === destination.protocol && origin.host === destination.host;
```

3. 비교하려는 URL 을 사용하여 두 개의 URL 객체를 생성합니다.

```js
const origin = new URL("https://www.30secondsofcode.org/about");
const destination = new URL("https://www.30secondsofcode.org/contact");
```

4. 두 URL 객체를 인수로 사용하여 `isSameOrigin` 함수를 호출하여 부울 (boolean) 출력을 얻습니다.

```js
isSameOrigin(origin, destination); // true
```

5. 다른 URL 로 함수를 테스트하여 동일한 오리진에 있는지 확인할 수도 있습니다.

```js
const other = new URL("https://developer.mozilla.org");
isSameOrigin(origin, other); // false
```
