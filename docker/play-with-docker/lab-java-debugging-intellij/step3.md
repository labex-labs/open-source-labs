# Building the application

The application is a basic Spring MVC application that receives user input from a form, writes the data to a database, and queries the database.

The application is built using Maven. To build the application click on icon on the bottom left of the IntelliJ window and select `Maven Projects`.

![](./assets/intellij_maven_setup.png)

The `Maven Projects` window will open on the right side. Maven goals of `clean` and `install` need to be set to build the application.

To set the `clean` goal, click on `Lifecycle` to display the tree of goals. Right click on `clean` and select `Create 'UserSignup [clean]'...`

![](./assets/intellij_maven_goal_clean.png)

Click `OK` in the `Create Run/Debug Configuration` window.

![](./assets/intellij_maven_goal_clean_menu.png)

Configure the `install` goal similarly. Click on `install` in the Lifecycle tree. Select `Create 'UserSignup[install]'...`

![](./assets/intellij_maven_goal_install.png)

Click `OK` in the `Create Run/Debug Configuration` window.

![](./assets/intelligj_maven_goal_install_menu.png)

To build the application run `clean`

![](./assets/intellij_maven_goal_clean_run.png)

Then run `install`

![](./assets/intellij_maven_goal_install_run.png)

When the application builds, you will see a success message in the log window.

![](./assets/intellij_maven_goal_install_log.png)
