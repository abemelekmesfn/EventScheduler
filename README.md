# EventScheduler
The Event Scheduler API is a Django REST API that allows users to create, manage, and track events in a structured way. It includes user authentication, event management, participant tracking, and reminder support. The system is designed to be scalable and API-first, meaning it can be easily connected with a frontend such as React or a mobile application.

The project has been organized into modular apps: a users app that handles authentication and profile management, and an events app that manages the scheduling, updating, and deletion of events. Each event stores details like title, description, location, start and end time, and organizer information. Users can also invite and manage participants, and events can be filtered based on date or organizer.

To get started, you first need to clone the repository and set up a Python virtual environment. After installing dependencies from requirements.txt, run the migrations to set up your database. Once complete, you can start the development server with python manage.py runserver. The project will then be available at http://127.0.0.1:8000. For admin access, you can create your own superuser or log in with the provided test credentials.

For testing purposes, a demo account is already available. The username is abemelek, the email is test@example.com
, and the password is pasword123. These credentials can be used to log in immediately and test the API endpoints. You can register a new user by sending a POST request to /api/users/register/ with a username, email, and password in JSON format. Authentication is handled through the /api/users/login/ endpoint, where you send a username and password to receive an authentication token. Once authenticated, you can interact with the events API.

Events are managed through the /api/events/ endpoint. A GET request to this endpoint retrieves all events. To create a new event, you send a POST request with event details such as title, description, start time, end time, and location. Updating an event is done with a PUT request to /api/events/{id}/, and deleting an event is done with a DELETE request to the same URL. In both cases, the user must be authenticated.

In short, the Event Scheduler API provides a solid backend foundation for managing events and users. With the provided test account, you can quickly explore the system, log in, and begin creating or managing events.
