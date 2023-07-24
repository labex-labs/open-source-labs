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

To configure remote debugging in IntelliJ, click on `Run` > `Edit Configuration ...`

![](./assets/intelij_debug_run_edit_configurations.png)

Add a new remote configuration.

![](./assets/intellij_debug_add_remote_configuration.png)

In the `Run\Debug Configurations` window, set the `Name` of the configuration as `docker tomcat` and in `Settings` set the port to '8000' as the default Tomcat JPDA debuging port. Click on `OK` to save the configuration.

![](./assets/intellij_debug_tomcat_remote_settings.png)
