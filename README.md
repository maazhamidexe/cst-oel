# Flask Text Analysis App

This Flask app analyzes text input provided by the user. It allows the user to perform two actions: sentiment analysis and spelling correction.

## Installation

To run this application, follow these steps:

1. Clone the repository:
   git clone <repository_url>

2. Navigate to the project directory:
   cd flask-text-analysis-app

3. Install the required dependencies:
   pip install -r requirements.txt

## Usage

1. Run the Flask app:
   python app.py

2. Open your web browser and navigate to 'http://localhost:5000/'.

3. Enter text in the provided input field.

4. Choose the action you want to perform:
   - **Analyze Sentiment**: Analyzes the sentiment of the provided text.
   - **Correct Spelling**: Corrects the spelling of the provided text.

5. Click the **Submit** button to perform the selected action.

6. View the result on the result page.

## Project Structure

The project structure is as follows:

- 'app.py': Contains the Flask application code.
- 'templates/': Directory containing HTML templates for rendering the user interface.
  - 'index.html': Template for the main page where users input text and select actions.
  - 'result.html': Template for displaying the result of the selected action.

## Dependencies

- Flask: Web framework for building the application.
- TextBlob: Python library for processing textual data.
