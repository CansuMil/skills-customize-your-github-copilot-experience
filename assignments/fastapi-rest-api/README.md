# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and document RESTful APIs using the FastAPI framework in Python. You will create a simple API for managing a collection of resources (e.g., books, tasks, or users) and practice handling HTTP requests, responses, and data validation.

## 📝 Tasks

### 🛠️  Create a FastAPI Project

#### Description
Set up a new FastAPI project and create a main application file. Run the development server and verify that the default route ("/") returns a welcome message.

#### Requirements
Completed program should:
- Use FastAPI to create a web application
- Define a root endpoint ("/") that returns a JSON welcome message
- Run locally and be accessible at http://localhost:8000

### 🛠️  Implement CRUD Endpoints

#### Description
Add endpoints to your FastAPI app to Create, Read, Update, and Delete (CRUD) items in a resource collection (e.g., books, tasks, or users). Use Pydantic models for data validation.

#### Requirements
Completed program should:
- Define a Pydantic model for your resource (e.g., Book, Task, or User)
- Implement endpoints for:
  - Creating a new item (POST)
  - Retrieving all items (GET)
  - Retrieving a single item by ID (GET)
  - Updating an item by ID (PUT or PATCH)
  - Deleting an item by ID (DELETE)
- Return appropriate HTTP status codes and error messages

### 🛠️  (Optional) Add API Documentation and Extra Features

#### Description
Enhance your API with additional features and explore FastAPI's automatic documentation.

#### Requirements
Completed program could:
- Add input validation and error handling
- Use FastAPI's automatic interactive docs (Swagger UI)
- Add authentication or pagination
- Write example requests and responses in the README
