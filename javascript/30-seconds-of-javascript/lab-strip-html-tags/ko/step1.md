# 문자열에서 HTML/XML 태그 제거 방법

문자열에서 HTML/XML 태그를 제거하려면 정규 표현식 (regular expression) 을 사용할 수 있습니다. 다음 단계를 따르세요:

1. 터미널/SSH 를 엽니다.
2. `node`를 입력하여 코딩 연습을 시작합니다.
3. 다음 코드를 사용합니다:

```js
const stripHTMLTags = (str) => str.replace(/<[^>]*>/g, "");
```

4. 다음 예시로 함수를 테스트합니다:

```js
stripHTMLTags("<p><em>lorem</em> <strong>ipsum</strong></p>"); // 'lorem ipsum'
```

이렇게 하면 입력 문자열에서 모든 HTML/XML 태그가 제거되고 나머지 텍스트가 반환됩니다.
