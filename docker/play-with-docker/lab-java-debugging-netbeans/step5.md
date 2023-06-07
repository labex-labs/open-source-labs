# Debugging the Application

In the application, click on `Signup` to create a new user. Fill out the registration form and click `Submit`

![](./assets/app_debug_signup2.png)

Click `Yes` to confirm.

![](./assets/app_debug_signup_confirm.png)

Test out the login.

![](./assets/app_debug_login2.png)

Oh no!

![](./assets/app_debug_login_fail2.png)

#### Configure Remote Debugging

In the menu click on `Debug` > `Attach Debugger...`

![](./assets/netbeans_debug_attach_debugger_menu.png)

Make sure that the port is set to 8000, click on `OK`.

![](./assets/netbeans_debug_attach_debugger_configure.png)

#### Finding the Error

Since the problem is with the password, lets see how the password is set in the User class. In the User class, the setter for password is scrambled using [rot13](https://en.wikipedia.org/wiki/ROT13) before it is saved to the database.

Since we enabled remote debugging earlier, you should see the Daemon Threads for Tomcat in the `Debugging` window. Set a breakpoint for in the User class where the password is set.

![](./assets/netbeans_debug_User_breakpoint.png)

Register a new user with the username of 'Moby' and with 'm0by' as the password, click `Submit`, click `yes`

![](./assets/app_register_moby2.png)

NetBeans will display the code at the breakpoint and the value of password in the variables window. Note that the value is `m0by`

![](./assets/netbeans_debug_User_moby.png)

Click on `Continue` icon or press `F5` to let the code run.

![](./assets/netbeans_debug_resume.png)

Next, set a breakpoint on the getPassword in the User class to see the value returned for password. You can also toggle off the breakpoint for setPassword. Try to log into the application. Look at the value for password in the NetBeans variables window, note that it is `z0ol` which is `m0by` using ROT13.

![](./assets/netbeans_debug_User_show_user.png)

In this MVC application the UserController uses the findByLogin method in the UserServiceImpl class which uses the findByUsername method to retrieve the information from the database. It then checks to see if the password from the form matches the user password. Since the password from the login form is not scrambled using ROT13, it does not match the user password and you cannot log into the application.

To fix this, apply ROT13 to the password by adding

```
import com.docker.UserSignup.utit.Rot13

String passwd = Rot13.rot13(password);
```

![](./assets/netbeans_debug_UserServiceImpl_code.png)

Set a breakpoint in UserServiceImpl on the findByLogin method. Press `F11` or click on `Run` > `Build Project` to update the deployed code. Log in again and look at the values for the breakpoint. The 'passwd' variable is `z0ol` which matches the password for the user moby.

![](./assets/netbeans_debug_UserServiceImpl_values.png)

Continue (`F5`) and you should successfully log in.

![](./assets/app_debug_success.png)

{:.quiz}
True or false: You have to restart a container after you make changes to the code or they won't be reflected in the application

- ( ) True
- (x) False

{:.quiz}
True or false: Debugging a Java app running in a container requires a special plugin for the IDE

- ( ) True
- (x) False