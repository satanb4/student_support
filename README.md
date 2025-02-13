# MyPath Application

## Description
The new MyPath project application built from the ground up to be asynchronous and fast 🔥
Concept site under University of Glasgow

## Demo
https://github.com/satanb4/student_support/assets/26685910/cdd56f9a-6b00-4095-a01c-3c9fd0e205c3



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
4. Run `pip install -r requirements/requirements.txt`
5. cd into `frontend` and run `npm install`
6. Run `pre-commit install`

## Usage
1. cd to tailwindcss/
2. Run `npx tailwindcss -i ../app/src/css/inputs.css -o ../app/src/css/output.css --watch`
3. cd to the root directory in different terminal
4. Run `hypercorn app.main:app --reload --bind 127.0.0.1:8080`
5. Visit `http://localhost:8000`
6. Enjoy!

## Database Setup (Developer)
- Run the postgres database:- <br>
`sudo docker run --name mypath_db -v /var/lib/postgresql/data:/var/lib/postgresql/data -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=mypath -p 5432:5432 -d postgres:16`


## Running Migrations (Developer)
- Run the migration:- `alembic upgrade head`

```
Creating Migrations (Initial) - DO NOT RUN
- Create the migrations folder:- `alembic init -t async migrations`
- Generate a migration:- `alembic revision --autogenerate -m "Initial migration"`
```

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
- Module: `hypercorn`
- Parameters: `app.main:app --reload --bind 127.0.0.1:8080`

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
