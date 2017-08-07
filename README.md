### Books
To setup:

`docker-compose run django python3 hearstbook/manage.py migrate`

To migrate db schema:

`docker-compose run django python3 hearstbook/manage.py migrate`

To run the server:

`docker-compose up`

To kill the server:

`docker-compose down`

To run the tests:

`docker-compose run django python3 hearstbook/manage.py test hearstbook`

The one ambiguity in the problem was there was no clear definition of a category. To implement a true category, I would add a m2m on Book to a BookCategory.

I spent most of my time writing tests specific to the framework, all of the setup of the views/models is pretty straightforward.

The next piece I would add to this application is an admin widget to look up books online via ISBN, generating a Book object.