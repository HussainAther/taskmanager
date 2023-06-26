# Task Management Application

This is a full-stack task management application developed using Flask for the backend and React for the frontend.

## Features

- User Authentication: Users can register, log in, and log out.
- Task Management: Users can create, read, update, and delete tasks.
- Frontend: The frontend is built using React with HTML, CSS, and JavaScript.
- Backend: The backend is developed using Flask, a Python web framework.
- Database: SQLite is used as the database management system.

## Installation

1. Clone the repository:

```
git clone https://github.com/HussainAther/taskmanager
```

2. Backend Setup:

- Install Python and Flask.
- Set up a virtual environment (optional but recommended).
- Install the required Python packages using pip:

```
pip install -r requirements.txt
```

3. Frontend Setup:

- Install Node.js and npm.
- Navigate to the frontend directory:

```
cd frontend
```

- Install the required npm packages:

```
npm install
```

## Usage

1. Start the Backend Server:

- In the project root directory, run the following command:

```
python app.py
```

- The Flask development server will start running at `http://localhost:5000`or the given URL.

2. Start the Frontend Development Server:

- In the `frontend` directory, run the following command:

```
npm start
```

- The React development server will start running at the given host.

3. Access the Application:

- Open your web browser and visit `http://localhost:3000` or the given URL to access the Task Management Application.


## Using a virtual environment 

Note: It's recommended to use a virtual environment to isolate your project's dependencies. This allows you to maintain separate environments for different projects without conflicts. You can create a virtual environment using virtualenv or venv:

Using virtualenv:

```
virtualenv venv
```

Using venv (built-in in Python 3):

```
python -m venv venv
```

After creating the virtual environment, activate it before installing packages or running your application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

