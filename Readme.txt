Does the web application use Django to serve static HTML content?

http://localhost:8000/restaurant/

Has the learner committed the project to a Git repository?

https://github.com/AlvaroMontoyaLehmann/littlelemon

Does the application connect the backend to a MySQL database?

Yeah! settings.py fiel

Are the menu and table booking APIs implemented?

http://localhost:8000/restaurant/booking/tables/

Is the application set up with user registration and authentication?

Registration: http://localhost:8000/auth/users/
Authentication: http://localhost:8000/restaurant/api-token-auth #Method POST, BODY {"username":"","password":""}

Does the application contain unit tests?

Test comand:
py manage.py test Littlelemon.tests.test_views
py manage.py test Littlelemon.tests.test_models

Can the API be tested with the Insomnia REST client?

http://localhost:8000/restaurant/menu/
http://localhost:8000/restaurant/menu/id
http://localhost:8000/restaurant/booking/tables
http://localhost:8000/restaurant/booking/tables/id
