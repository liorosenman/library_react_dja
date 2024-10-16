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
