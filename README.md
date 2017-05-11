# Metadata for Democracy

The purpose of this project is to provide real-time status information about Data For Democracy's projects and allow volunteers to more easily find out what work they can contribute today.

The initial version will track github activity for each project and provide an API endpoint for retrieving that information.

[**Project Lead:**](https://github.com/Data4Democracy/read-this-first/blob/master/lead-role-description.md) [@yesthatjake](https://datafordemocracy.slack.com/messages/@yesthatjake/) 

## Project Strucutre

The initial work for this project will be in 4 parts:

* A datastore for keeping information about the projects.
* A script for retrieving and storing a snapshot for the project data.
* A service that listens for github changes and updates the dataset.
* An API endpoint for querying the dataset.


