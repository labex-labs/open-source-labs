# Writing Tests

Now that you have set up the testing environment, you can start writing tests for your Flask application. Here are some examples of common tests you might want to write:

1. Test a route:

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   This test sends a GET request to the root route ("/") and checks that the response status code is 200 and the response data contains the string "Hello, World!".

2. Test a POST request:

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   This test sends a POST request to the login route ("/login") with form data containing a username and password. It checks that the response status code is 200 and the response data contains the string "Logged in successfully".

3. Test a command:

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   This test invokes a command named "hello" and checks that the command exits with a code of 0 and the output contains the string "Hello, World!".
