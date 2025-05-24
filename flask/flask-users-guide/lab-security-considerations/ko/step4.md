# 보안 헤더

브라우저는 보안을 제어하기 위해 다양한 응답 헤더를 인식합니다. Flask 애플리케이션에서 다음 보안 헤더를 검토하고 사용하는 것이 좋습니다.

- HTTP Strict Transport Security (HSTS): 브라우저에게 모든 HTTP 요청을 HTTPS 로 변환하도록 지시합니다.
- Content Security Policy (CSP): 다양한 유형의 리소스를 어디에서 로드할 수 있는지 지정합니다.
- X-Content-Type-Options: 브라우저가 응답 콘텐츠 유형을 준수하도록 강제합니다.
- X-Frame-Options: 외부 사이트가 iframe 에 사이트를 포함하는 것을 방지합니다.

Flask 애플리케이션에서 HTTPS 및 보안 헤더를 관리하기 위해 `Flask-Talisman` 확장을 사용할 수 있습니다.
