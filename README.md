### Books Demo Docker Instructions ###

1. set up the container:
`docker-compose build`

2. migrate db schema:

`docker-compose run django hearstbook/manage.py migrate`

3. make a super user:
`docker-compose run django hearstbook/manage.py createsuperuser`

4. run the server:

`docker-compose up`

4. login and make some books
http://127.0.0.1:8000/admin/

5. kill the server:

`docker-compose down`

To run the tests:

`docker-compose run django python3 hearstbook/manage.py test hearstbook.library`

The one ambiguity in the problem was there was no clear definition of a category. To implement a true category, I would add a m2m on Book to a BookCategory.

I spent most of my time writing tests specific to the framework, all of the setup of the views/models is pretty straightforward.

The next piece I would add to this application is an admin widget to look up books online via ISBN, generating a Book object.
