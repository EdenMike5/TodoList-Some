# Web TodoList Project

## Overview
A simple web-based Todo List application with FastAPI backend and vanilla JavaScript frontend.

## Tech Stack
- Backend: Python FastAPI, SQLAlchemy, SQLite
- Frontend: HTML, CSS (Bootstrap), JavaScript

## Setup

### Backend
1. Navigate to backend directory
2. Install dependencies (already done): fastapi, uvicorn, sqlalchemy
3. Run the server: `uvicorn main:app --reload`

### Frontend
1. Navigate to frontend directory
2. Serve the static files: `python -m http.server 3000`
3. Open browser to http://localhost:3000

## API Endpoints
- GET /todos: Get all todos
- POST /todos: Create new todo
- PUT /todos/{id}: Update todo completion
- DELETE /todos/{id}: Delete todo

## Features
- Add new todos
- Mark todos as completed/incomplete
- Delete todos
- Persistent storage with SQLite