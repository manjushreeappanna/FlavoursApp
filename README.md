# Chocolate House Application

Welcome to the Chocolate House Application! This application allows users to manage seasonal flavors, ingredient inventory, and customer feedback.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Running with Docker](#running-with-docker)

## Features

- Add and view seasonal flavors
- Add and manage ingredients in inventory
- Collect customer feedback on flavors

## Prerequisites

- Docker installed on your machine. You can download it from [Docker's official site](https://www.docker.com/get-started).
- Git installed on your machine to clone the repository (if applicable).

## Installation

1. **Clone the Repository** (if you haven't already):

    ```bash
    git clone https://github.com/manjushreeappanna/FlavoursApp.git
    cd FlavoursApp
    ```

2. **Navigate to the Application Directory**:
   
   If your files are in a specific directory (e.g., `cho`), make sure you navigate there, or adjust the `Dockerfile` as necessary.

## Usage

The application uses Flask for web development and SQLite for database management.

### Running the Application

1. **Run Locally (without Docker)**:
   - Install the required packages:
     ```bash
     pip install flask sqlite3
     ```
   - Run the application:
     ```bash
     python app.py
     ```
   - Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Running with Docker

1. **Build the Docker Image**:

    ```bash
    docker build -t flavours_app .
    ```

2. **Run the Docker Container**:

    ```bash
    docker run -p 5000:5000 flavours_app
    ```

3. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` to access the application.

