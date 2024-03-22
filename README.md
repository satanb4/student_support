# MyPath Application

## Description
The new MyPath project application built from the ground up to be asynchronous and fast 🔥
The official repository operated under Glasgow University Software Services.

## Stack
- Python 3.11
- FastAPI
- HTMX
- TailwindCSS+DaisyUI
- PostgreSQL

## Tools
- Docker
- Docker Compose
- Pytest
- Gitlab CI/CD

## Installation
1. Clone the repository
2. Run `virtualenv venv`
3. Run `source venv/bin/activate`
4. Run `pip install -r requirements.txt`
5. cd into `frontend` and run `npm install`
6. Run `pre-commit install`

## Usage
1. cd to tailwindcss/
2. Run `npx tailwindcss -i ../app/src/css/inputs.css -o ../app/src/css/output.css --watch`
3. cd to the root directory in different terminal
4. Run `uvicorn app.main:app --reload --port 8080`
5. Visit `http://localhost:8000`
6. Enjoy!

### IntelliJ / PyCharm Specifics
If you are using an IntelliJ IDE, you can run the application by creating a new configuration with the following settings:

TailwindCSS:
- Type: NPM
- Name: TailwindCSS
- Command: `run`
- Script: `exec`

FastAPI:
- Type: Python
- Name: FastAPI
- Module: `uvicorn`
- Parameters: `app.main:app --reload --port 8080`

## Contributing
1. Fork the repository - `git clone`
2. Create a new branch - `git switch -c feature/branch-name`
3. Make your changes
4. Create a pull request - `git push origin feature/branch-name` -> development branch
5. Wait for approval
6. Merge your changes
7. Celebrate 🎉

## Developers
- [Sayan Bandyopadhyay](https://www.linkedin.com/in/sayan-bandyopadhyay/)
- [Finn Lestrange](https://finnlestrange.tech)
