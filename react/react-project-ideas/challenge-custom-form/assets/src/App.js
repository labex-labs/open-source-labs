import CustomForm from "./components/CustomForm/CustomForm";
// TODO: Complete the code here
function App() {

  const handleLogin = () => { }
  const handleRegister = () => { }

  return (
    <div className="App">
      <CustomForm
        username={{
          type: "text",
          label: "Username",
          placeholder: "Enter Username",
          ref: usernameRef,
          isInput: true,
        }}
        password={{
          type: "password",
          label: "Password",
          placeholder: "Enter Password",
          ref: passwordRef,
          isInput: true,
        }}
        loginButton={{
          handler: handleLogin,
          buttonText: "Login",
          isInput: false,
        }}
        registerButton={{
          handler: handleRegister,
          buttonText: "Register",
          isInput: false,
        }}
      />
    </div>
  );
}

export default App;
