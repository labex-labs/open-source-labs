# 기본 URL 검색

주어진 URL 에서 기본 URL 을 검색하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. 다음 JavaScript 함수를 사용하여 매개변수나 프래그먼트 식별자 없이 현재 URL 을 가져옵니다.

```js
const getBaseURL = (url) => url.replace(/[?#].*$/, "");
```

4. `url`을 기본 URL 을 검색하려는 URL 로 바꿉니다.
5. 이 함수는 `'?'` 또는 `'#'`가 발견되면 그 뒤의 모든 것을 제거하고 기본 URL 을 반환합니다.
6. 다음은 예시입니다.

```js
getBaseURL("http://url.com/page?name=Adam&surname=Smith");
// 'http://url.com/page'
```
