### Books Demo Docker Instructions ###

1. set up the container:

`docker-compose build`

2. start up the application:

`docker-compose up`

3. migrate db schema:

`docker-compose run migrate`

4. make a super user:

`docker-compose run createsuper`

5. login and make some books

http://localhost:8000/admin/

6. Poke around the APIs:

* http://localhost:8000/libraries/
* http://localhost:8000/books/
6. kill the server:

`docker-compose down`

To run the tests:

`docker-compose run django python3 hearstbook/manage.py test hearstbook.library`

The one ambiguity in the problem was there was no clear definition of a category. 
~~To implement a true category, I would add a m2m on Book to a BookCategory.~~ 
Added a library model and viewset.

I spent most of my time writing tests specific to the framework, all of the setup of the views/models is pretty straightforward. I am also not a docker config expert. This is evolving.

The next piece I would add to this application is an admin widget to look up books online via ISBN, generating a Book object.
