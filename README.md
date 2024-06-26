# Website Status Checker

## Description

The Website Status Checker is a simple web application that allows you to monitor the status of various websites. You can add websites to the list, and the application will periodically check if the websites are up or down. You can start and stop the status checking manually, and you can also edit or delete websites from the list.

## Features

- Add websites to monitor their status.
- Manually start and stop the status checking.
- View the status, response time, and status code of each website.
- Edit and delete websites from the list.
- Use of AJAX for dynamic content updates.
- Stylish UI with Bootstrap and SweetAlert2 for interactive pop-ups.

## Technologies Used

- Python (Flask) for the backend
- SQLite for database
- HTML, CSS, and JavaScript for the frontend
- Bootstrap for styling
- SweetAlert2 for interactive alerts

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/layersony/website-status-checker.git
    cd website-status-checker
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv env_backend/
    source env_backend/bin/activate  # On Windows use `env_backend/\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```

5. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

## Usage

1. **Add a Website:**

    - Enter the URL of the website you want to monitor in the input field and click "Add".

2. **Start Checking:**

    - Click the "Start Checking" button to start monitoring the status of the websites.

3. **Stop Checking:**

    - Click the "Stop Checking" button to stop monitoring the status.

4. **View Details:**

    - Click on a website URL in the list to view more details about its status.

5. **Edit Website:**

    - Click the "Edit" button next to a website URL to change its URL.

6. **Delete Website:**

    - Click the "Delete" button next to a website URL to remove it from the list.

## File Structure


- `templates/index.html`: Contains the HTML structure and embedded JavaScript for the frontend.
- `db.py` : Contains the DB Code
- `main.py`: Contains the Flask backend code.
- `requirements.txt`: Contains the Python dependencies.

## API Endpoints

- **GET /api/websites:** Retrieves the list of websites.
- **POST /add_website:** Adds a new website to the list.
- **POST /edit_website:** Edits an existing website URL.
- **POST /delete_website:** Deletes a website from the list.
- **GET /api/check_status:** Checks the status of a specific website.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
