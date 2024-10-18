# Basic settings
# Configure the database: 
    1. Pull the postgres by docker pull command - docker pull dpage/pgadmin4
    2. Run the container - docker run --name my_postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=library -p 5432:5432 -d postgres
    3. Configuring django's settings - DATABASES - Connceting to the postgres
    4. Creating a basic model in the app
    5. Make migrations and migrate the model.
    6. GO inside the container's shell --- docker exec -it my_postgres psql -U myuser -d library 
    7. List all tables --- \dt
    8. Customer table was created.
    9. Serializers for Customer and User were created.
    10. Book models was created, with two enums

# Register form fields input validation
    Done but was not tested.
# Register method
    Works (without the decorator of input validity)
    With @input_validity --- error: "detail": "Method \"POST\" not allowed."
# Compose file of pgadmin and postgres
    Problems in setting up and configuring the compose file.
    ** Open pgadmin in http://localhost:8080/browser/
       General Name = library
       Host name/address = postgres
       Password = admin123
    === Compose file working, pgadmin and postgres work
# Stored procedures
Every time I load the program, the procedures will load up automatically.

# DB
In addition to the models, enums should be saved as well.
Initializing file named init.sql, in which procedures will be created.
Model book was created, in pgadmin too.

# Login, token and Logout -
---working---
