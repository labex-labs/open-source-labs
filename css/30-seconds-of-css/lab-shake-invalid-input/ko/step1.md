# 유효하지 않은 입력 시 흔들림 효과

`index.html`과 `style.css`는 이미 VM 에 제공되어 있습니다.

유효하지 않은 입력이 있을 때 흔들림 애니메이션을 생성하려면 다음 단계를 따르세요.

1. `pattern` 속성을 사용하여 허용되는 입력을 지정하는 정규 표현식 (regular expression) 을 정의합니다. 예를 들어, 문자만 허용하려면 `[A-Za-z]*`를 사용합니다.
2. `@keyframes`를 사용하여 흔들림 애니메이션을 정의합니다. `margin-left` 속성을 설정하여 입력을 좌우로 이동시킵니다.
3. `:invalid` 의사 클래스를 사용하여 흔들림 애니메이션을 입력에 적용합니다.
4. 선택적으로, 오류를 나타내기 위해 입력에 빨간색 box-shadow 를 추가합니다.

다음은 코드 스니펫 (code snippet) 예시입니다.

```html
<input type="text" placeholder="Letters only" pattern="[A-Za-z]*" />
```

```css
@keyframes shake {
  0% {
    margin-left: 0rem;
  }
  25% {
    margin-left: 0.5rem;
  }
  75% {
    margin-left: -0.5rem;
  }
  100% {
    margin-left: 0rem;
  }
}

input:invalid {
  animation: shake 0.2s ease-in-out 0s 2;
  box-shadow: 0 0 0.6rem #ff0000;
}
```

오른쪽 하단의 'Go Live'를 클릭하여 포트 8080 에서 웹 서비스를 실행하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.
