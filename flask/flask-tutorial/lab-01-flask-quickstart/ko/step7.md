# 애플리케이션 다시 실행

애플리케이션을 다시 실행하고 동적 콘텐츠 기능을 테스트해 보겠습니다.

1. Flask 개발 서버가 아직 실행 중이면 중지합니다 (Ctrl+C 를 누르십시오).
2. 다음 명령을 실행하여 서버를 다시 시작합니다:

   ```bash
   flask run --host=0.0.0.0
   ```

3. **Web 5000** 탭의 URL 을 복사하여 브라우저의 새 탭에 붙여넣습니다.

   ![Web 5000 URL 복사](../assets/copy-url.png)

4. URL 끝에 `/LabEx`를 추가하고 Enter 키를 누릅니다.

   ![Hello LabEx 웹 페이지](../assets/hello-labex.png)

5. URL 에서 `name` 매개변수의 값을 변경하고 Enter 키를 누릅니다.
