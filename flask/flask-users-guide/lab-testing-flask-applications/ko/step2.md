# 테스트 작성

이제 테스트 환경을 설정했으므로 Flask 애플리케이션에 대한 테스트를 작성할 수 있습니다. 다음은 작성할 수 있는 일반적인 테스트의 몇 가지 예입니다.

1. 라우트 (route) 테스트:

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   이 테스트는 루트 라우트 ("/") 로 GET 요청을 보내고 응답 상태 코드 (status code) 가 200 이고 응답 데이터에 문자열 "Hello, World!"가 포함되어 있는지 확인합니다.

2. POST 요청 테스트:

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   이 테스트는 사용자 이름과 비밀번호를 포함하는 폼 데이터 (form data) 와 함께 로그인 라우트 ("/login") 로 POST 요청을 보냅니다. 응답 상태 코드가 200 이고 응답 데이터에 문자열 "Logged in successfully"가 포함되어 있는지 확인합니다.

3. 명령 테스트:

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   이 테스트는 "hello"라는 명령을 호출하고 명령이 코드 0 으로 종료되고 출력에 문자열 "Hello, World!"가 포함되어 있는지 확인합니다.
