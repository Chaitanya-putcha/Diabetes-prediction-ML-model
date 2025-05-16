# Diabetes Prediction Web Application

This project is a web application that predicts diabetes outcomes based on user input using a logistic regression model. The application is built using Flask and provides a user-friendly interface for inputting health data.

## Project Structure

```
diabetes-prediction-webapp
├── app.py                   # Main application file
├── requirements.txt         # Project dependencies
├── model                    # Directory containing the trained model
│   └── diabetes_model.pkl   # Serialized logistic regression model
├── templates                # Directory for HTML templates
│   └── index.html           # Main page template
├── static                   # Directory for static files
│   └── style.css            # CSS styles for the web application
└── README.md                # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd diabetes-prediction-webapp
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

- Input your health data into the form fields provided on the main page.
- Click the "Predict" button to receive a prediction on whether you are likely to have diabetes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.