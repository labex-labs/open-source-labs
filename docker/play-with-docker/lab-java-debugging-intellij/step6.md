# Finding the Error

Since the problem is with the password, let's see how the password is set in the User class. In the User class, the setter for password is scrambled using [rot13](https://en.wikipedia.org/wiki/ROT13) before it is saved to the database.

![](./assets/intellij_debug_User_password.png)

Try registering a new user using the debugger. In the menu click on `Run` > `Debug...`

![](./assets/intellij_run_debug.png)

Choose the remote Tomcat debug configuration. The Debugger console will be displayed at the bottom of the IntelliJ window.

![](./assets/intellij_debug_choose_remote_tomcat.png)

Set a breakpoint in the User class where the password is set.

![](./assets/intellij_debug_set_breakpoint_password.png)

Register a new user with the username of 'Moby' and with 'm0by' as the password, click `Submit`, click `yes`

![](./assets/app_register_moby2.png)

IntelliJ will display the code at the breakpoint and the value of password in the variables window. Note that the value is `m0by`

![](./assets/intellij_debug_User_moby.png)

Click on `Resume Program` to let the code run or press `F8` to step over the breakpoint.

![](./assets/intellij_debug_resume.png)

Next, set a breakpoint on the getPassword in the User class to see the value returned for password. You can also toggle off the breakpoint for setPassword.

![](./assets/intellij_debug_User_getPassword.png)

Try to log into the application. Look at the value for password in the debugging console, note that it is `z0ol` which is `m0by` using ROT13.

![](./assets/intellij_debug_User_show_user.png)

In this MVC application the UserController uses the findByLogin method in the UserServiceImpl class which uses the findByUsername method to retrieve the information from the database. It then checks to see if the password from the form matches the user password. Since the password from the login form is not scrambled using ROT13, it does not match the user password and you cannot log into the application.

To fix this, apply ROT13 to the password by adding

```
import com.docker.UserSignup.utit.Rot13

String passwd = Rot13.rot13(password);
```

![](./assets/intellij_debug_UserServiceImpl_code.png)

Set a breakpoint in UserServiceImpl on the findByLogin method. Log in again and look at the values for the breakpoint. The 'passwd' variable is `z0ol` which matches the password for the user moby.

![](./assets/intellij_debug_UserServiceImpl_values.png)

Continue (`F8`) and you should successfully log in.

![](./assets/app_debug_success.png)

{:.quiz}
True or false: You have to restart a container after you make changes to the code or they won't be reflected in the application

- ( ) True
- (x) False

{:.quiz}
True or false: Debugging a Java app running in a container requires a special plugin for the IDE

- ( ) True
- (x) False
