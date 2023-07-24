# Building the application

The application is a basic Spring MVC application that receives user input from a form, writes the data to a database, and queries the database.

The application is built using Maven. To build the application click on `Run` > `Run configurations`

![](./assets/eclipse_maven_run_config3.png)

Select `Maven build` > `New`

![](./assets/eclipse_maven_build_new.png)

Enter a `Name` for the configuration.

Set the base direct of the application `<path>/registration-docker/app`.

Set the `Goals` to `clean install`.

Click `Apply`

Click `Run`

![](./assets/eclipse_maven_run_config_apply.png)

The results of the build will be displayed in the console.

![](./assets/eclipse_maven_console_build_result.png)
