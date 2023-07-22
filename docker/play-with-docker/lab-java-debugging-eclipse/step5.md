# Debugging the Application

In the application, click on `Signup` to create a new user. Fill out the registration form and click `Submit`

![](./assets/app_debug_signup2.png)

Click `Yes` to confirm.

![](./assets/app_debug_signup_confirm.png)

Test out the login.

![](./assets/app_debug_login2.png)

Oh no!

![](./assets/app_debug_login_fail2.png)

## Configure Remote Debugging

Tomcat supports remote debugging the Java Platform Debugger Architecture (JPDA). Remote debugging was enabled when the tomcat image (registration-webserver) was built.

To configure remote debugging in Eclipse, click on `Run` > `Debug Configurations ...`

![](./assets/eclipse_debug_configure2.png)

Select `Remote Java Application` and click on `Launch New Configuration` icon

![](./assets/eclipse_debug_configure_new.png)

Enter a `Name` for the configuration. Select the project using the `browse` button. Click on `Apply` to save the configuration and click on `Debug` to start the debugging connection between Tomcat and Eclipse.

![](./assets/eclipse_debug_configure_docker.png)
