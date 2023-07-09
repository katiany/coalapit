# Test API

This is an API written in Fast API.

This API returns an average of deductibles, stop losses and oop maxis, based on other API responses.

# Set up

You can set all API URL as environment variables before building and running the application.

The APIs are set in the docker-compose.yml file.

# Install

Firstly, make sure you have docker installed.

Then, build the application:

> docker-compose build

And run:

> docker-compose up -d

The API will run locally on port 8008

# REST API

You can make requests passing an id of `member_id` as a parameter. The API will return the average of all data retrieved from all APIs.

# Tests

To run the tests locally, just run:

> make test