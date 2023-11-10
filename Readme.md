# A Real-Time Messaging App built with FastAPI, MongoDB and RabbitMQ using Domain Driven Development Principles

## Overview

The app allows users to send and receive messages in real-time. It's built on top of FastAPI web framework, and using MongoDB collections to store messages data. The app uses RabbitMQ as a message broker to enable real-time communication. The application is designed following the principles of Domain-Driven Design (DDD) to ensure a clean and structured codebase.

This app also showcases some design patterns such as mediator, dependency injection, observer and many more. 

Feel free to use this repo as a boilerplate for your messaging micro-services!

## Getting Started
These instructions will help you set up the project on your local machine for development and testing.

To run the project you should install some key binary packages to run the project on your local machine:

* `poetry`
* `python3.11+`
* `pre-commit` for clean codding
* `docker` and `docker-compose` to run the app in docker (it is much more convient with `docker` although it is not neccessary and you actually can run the project full-locally)
* `makefile` for run `make <something>` type commands

To actually run the project you have to clone the repository and run the `make all` command at repo's root directory. You can actually run `make services` command to only start services and run the app on your local machine through `uvicorn` directly though it can actually break some pythonpaths and may cause the import issues.

## Some Key Dependencies And Practicies

* [depdency-injector](https://github.com/ets-labs/python-dependency-injector) a dependency injection library to inject the dependencies.
* [FastAPI](https://github.com/tiangolo/fastapi) - a main web framework
