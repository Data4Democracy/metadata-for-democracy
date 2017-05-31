# Metadata for Democracy

The purpose of this project is to provide real-time status information about Data For Democracy's projects and allow volunteers to more easily find out what work they can contribute today.

The initial version will track github activity for each project and provide an API endpoint for retrieving that information.

[**Project Lead:**](https://github.com/Data4Democracy/read-this-first/blob/master/lead-role-description.md) [@yesthatjake](https://datafordemocracy.slack.com/messages/@yesthatjake/) 

## Project Strucutre

The initial work for this project will be in 4 parts:

* A datastore for keeping information about the projects.
* A script for retrieving and storing a snapshot for the project data.
* A web hook that listens for github changes and updates the dataset.
* An API endpoint for querying the dataset.

## Technologies

Which technologies are used will be a function of what skills our volunteers bring to the table. The initial plan is to use python and postgreSQL.

## Running the Project

Metadata for Democracy uses docker to run in development. If you don't have docker installed, you can read the installation instructions [here](https://github.com/Data4Democracy/docker-scaffolding).

Once you have docker installed and running, navigate to the root project directory and execute

```docker-compose up```

This will start the database, web hook, and API server.

To run the snapshot script, navigate to the snapshot subdirectory and execute

./take.py

## Coding standards



## Guiding principles

In addition to the [goals of Data For Democracy](http://datafordemocracy.org/about.html), this project seeks to adhere to the following principles:

* Write for reuse - While this tool is being built first for Data For Democracy, it should be written with an eye towards being available to any organization that uses some or all of the tools we use to organize our own work.

* No vendor lock-in - Write to run on any platform with thin, modular adapters for specific platforms.
