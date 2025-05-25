# jQuery 작동 방식

> `index.html`은 이미 VM 에 제공되었습니다.

이 파일은 환경 초기화 중에 자동으로 생성됩니다. 자동으로 생성되지 않으면 위의 이미지와 같이 파일과 함수를 생성하십시오. 함수 코드는 다음과 같습니다.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // Your code goes here.
    </script>
  </body>
</html>
```

`<script>` 요소의 `src` 속성은 jQuery 의 복사본을 가리켜야 합니다. [Downloading jQuery](https://jquery.com/download/) 페이지에서 jQuery 의 복사본을 다운로드하고 `jquery.min.js` 파일을 HTML 파일과 동일한 디렉토리에 저장하십시오.

> 참고: jQuery 를 다운로드할 때 파일 이름에 버전 번호 (예: `jquery-x.y.z.js`) 가 포함될 수 있습니다. 이 파일의 이름을 `jquery.js`로 바꾸거나 `<script>` 요소의 `src` 속성을 파일 이름과 일치하도록 업데이트하십시오.

#### 문서 준비 완료 시 코드 실행

브라우저가 문서를 로드하는 것을 완료한 후에 코드가 실행되도록 하기 위해 많은 JavaScript 프로그래머는 코드를 `onload` 함수로 래핑합니다.

```js
window.onload = function () {
  alert("welcome");
};
```

불행히도, 배너 광고를 포함하여 모든 이미지가 다운로드를 완료할 때까지 코드가 실행되지 않습니다. 문서를 조작할 준비가 되는 즉시 코드를 실행하기 위해 jQuery 에는 [ready event](http://api.jquery.com/ready/)라고 하는 구문이 있습니다.

```js
$(document).ready(function () {
  // Your code here.
});
```

> 참고: jQuery 라이브러리는 `jQuery`와 `$`라는 `window` 객체의 두 가지 속성을 통해 메서드와 속성을 노출합니다. `$`는 단순히 `jQuery`의 별칭이며, 더 짧고 빠르게 작성할 수 있기 때문에 자주 사용됩니다.

예를 들어, ready event 내에서 링크에 클릭 핸들러를 추가할 수 있습니다.

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

위의 jQuery 코드를 HTML 파일의 `// Your code goes here` 부분에 복사합니다. 그런 다음 HTML 파일을 저장하고 브라우저에서 테스트 페이지를 다시 로드합니다.

#### 전체 예시

다음 예제는 위에 설명된 클릭 핸들링 코드를 HTML `<body>`에 직접 포함하여 보여줍니다. 실제로 코드를 별도의 JS 파일에 넣고 `<script>` 요소의 `src` 속성을 사용하여 페이지에 로드하는 것이 좋습니다.

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>click me</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> 웹 서비스 포트 8080 에서 실행하려면 오른쪽 하단의 'Go Live'를 클릭하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
