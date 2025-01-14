# OSRSDle API

The **OSRSDle API** is a backend application built using **Python**, **Flask**, **SQLAlchemy**, **APScheduler**, and **PyJWT** for a game called *OSRSDle*. This is a guessing game based on the popular game *Old School RuneScape (OSRS)*. The API interacts with a **PostgreSQL** database hosted on **Supabase**, allowing users to fetch data about items, monsters, quests, and high scores. It also provides user authentication, creation, and management features such as login and logout.

## Table of Contents

- [Installation](#installation)
- [Technologies](#technologies)
- [API Endpoints](#api-endpoints)
  - [Equipments](#equipments)
  - [Monsters](#monsters)
  - [Quests](#quests)
  - [Users](#users)
  - [Highscores](#highscores)
- [Authentication](#authentication)
- [Scheduler Tasks](#scheduler-tasks)
- [Contributing](#contributing)
- [Additional Information](#additional-information)

## Installation

To get started with the OSRSDle API, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dan-perosa/osrsdle-api.git
   cd osrsdle-api

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables**:
   ```bash
   DATABASE_URL=your_database_url
   JWT_SECRET_KEY=your_secret_key

5. **Initialize the database**:
   ```bash
   flask db upgrade

6. **Run the application**:
   ```bash
   flask --app app run

Now the API should be running locally at http://127.0.0.1:5000.

## Technologies

This API is built using the following technologies:

- **Flask**: A lightweight web framework for building APIs.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **APScheduler**: For managing cron-like scheduled tasks.
- **PyJWT**: For creating and verifying JSON Web Tokens (JWTs) for user authentication.
- **PostgreSQL**: A relational database for storing the game data and user information.
- **Supabase**: A backend-as-a-service platform hosting the PostgreSQL database.

### API Endpoints

## Equipments

- **GET /equipments/**
  - Fetches all available equipment items in the game.
  - Response: List of equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/head**
  - Fetches all head equipment items in the game.
  - Response: List of head equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/cape**
  - Fetches all cape equipment items in the game.
  - Response: List of cape equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/neck**
  - Fetches all neck equipment items in the game.
  - Response: List of neck equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/ammunition**
  - Fetches all ammunition equipment items in the game.
  - Response: List of ammunition equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/weapon**
  - Fetches all weapon equipment items in the game.
  - Response: List of weapon equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/shield**
  - Fetches all shield equipment items in the game.
  - Response: List of shield equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/two_handed**
  - Fetches all two-handed weapon equipment items in the game.
  - Response: List of two-handed weapon equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/body**
  - Fetches all body equipment items in the game.
  - Response: List of body equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/legs**
  - Fetches all leg equipment items in the game.
  - Response: List of leg equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/hands**
  - Fetches all hand equipment items in the game.
  - Response: List of hand equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/feet**
  - Fetches all feet equipment items in the game.
  - Response: List of feet equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/ring**
  - Fetches all ring equipment items in the game.
  - Response: List of ring equipment items with details (e.g., name, ID, stats, etc.).

- **GET /equipments/{equipment_id}**
  - Fetches detailed information about a specific equipment item by its ID.
  - Response: Equipment item details.


## Monsters

- **GET /monsters**
  - Fetches all monsters in the game.
  - Response: List of monsters with details (e.g., name, ID, combat level, etc.).

- **GET /monsters/{monster_id}**
  - Fetches detailed information about a specific monster by its ID.
  - Response: Monster details.

## Quests

- **GET /quests**
  - Fetches all quests in the game.
  - Response: List of quests with details (e.g., name, ID, quest points, etc.).

- **GET /quests/{quest_id}**
  - Fetches detailed information about a specific quest by its ID.
  - Response: Quest details.

## Users

- **POST /user/create**
  - Register a new user.
  - Body: JSON containing `username`, `password`.
  - Response: User created successfully.

- **POST /user/login**
  - Log in and receive a JWT token.
  - Body: JSON containing `username`, `password`.
  - Response: `token`, User logged in successfully.

- **POST /user/logout**
  - Logs the user out (in practice, this could invalidate the token on the frontend).
  - Response: User logged out.

## Highscores

- **GET /user/get_highscores**
  - Fetches the highscores for the game.
  - Response: List of highscores.

## Authentication

The API uses **JSON Web Tokens (JWT)** to handle user authentication.

1. **Login**: Use the `/user/login` endpoint to log in and receive a JWT token.
2. **Secure Endpoints**: For any endpoint that requires authentication, include the JWT token in the `token` header:
   ```http
   token: <your_token>

### Scheduler Tasks

The API uses **APScheduler** to handle background tasks. These tasks can include things like automatic daily challenges, and other scheduled features within the game.

The cron jobs in the system are specifically used to reset the minigames every day at midnight. These resets include:

- **Quest Minigames Reset**: Resets the progress of quest minigame and chooses a new random quest.
- **Monster Minigames Reset**: Resets the progress of monster minigame and chooses a new random monster.
- **Equipment Minigames Reset**: Resets all the equipment-related minigames and chooses a new random equipment in each minigame.

These cron jobs ensure that the minigames are refreshed daily at midnight, allowing players to have a new set of challenges each day.

### Contributing

I always welcome contributions! If you'd like to help improve the API, please follow these steps:

1. **Fork the repository**: Click on the "Fork" button on the top-right of this repository to create your own copy of the project.
2. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b your-feature-branch
3. **Make your changes**: Implement your changes or additions to the codebase.
4. **Commit your changes**: Commit your changes with a clear and descriptive commit message.
   ```bash
   git commit -m "Description of the changes made"
5. **Push your changes**: Push your changes to your forked repository.
   ```bash
   git push origin your-feature-branch
6. **Create a pull request**: Go to the original repository and create a pull request to merge your changes.

### Additional Information

This project is a study project created by a fan based on a licensed game. I do not hold any rights over the game or its content. The purpose of this project is solely for educational and personal learning purposes.

