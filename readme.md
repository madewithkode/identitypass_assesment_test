# IdentityPass Python Developer Assesment Tasks

This repository houses the code for the IdentityPass Python Developer Assesment Tasks - A URL shortener and Asynchronous API aggregation endpoint. 

## Retrieve code

-   `$ git clone https://github.com/madewithkode/identitypass_assesment_test.git`

## Requrements

This project requires the following system dependencies:


*   Docker

*   Docker-compose


## Running

-   `$ docker-compose up`  - This command utilizes docker to build(on initial run) and bring up the project and all its relevant services inside a container.

-   `$ docker exec -it django bash`  - This would open up an interactive bash session inside the django container, cd into the projects src directory using `cd src` where you can now run migrations with `python manage.py migrate`.

## Other Useful Commands

-   `$ docker-compose down` - Use this command to bring down the container and all its services. add the -v flag if you want to discard any associated volumes as well.


## Endpoints

The UI documentation can be found at `/api/docs`, the following is a rundown of available endpoints:

-  GET `/api/v1/async/`  - This endpoint aynchronously fetches and aggregates responses from two endpoints, namely `https://randomuser.me/api/` and `https://quotable.io/quotes?page=1` and aggregates their different results into one response and returns that. 

-  POST `/api/v1/shortener/generate/` - This endpoint receives an arbitrary URL and returns a shortened version.

