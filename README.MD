# Face Swapper Web App
A user-friendly web application for swapping faces between two images, built with Flask and InsightFace.

## Features
* Seamless Face Swapping: Swap faces between any two uploaded images.

* Aesthetic UI: A clean, modern, and responsive user interface using custom CSS.

* Robust Backend: Handles image uploads, processing, and display using Python and Flask.

* Error Handling: Provides user feedback for cases where faces are not detected.

* Persistent Session: Displays original and swapped images side-by-side for easy comparison.

## Technologies Used
* Python: The main programming language for the backend.

* Flask: A micro-framework for building the web application.

* InsightFace: The core computer vision library for face detection and swapping.

* OpenCV: Used for image reading and manipulation.

* HTML/CSS: For the front-end user interface and styling.

## Setup and Installation
Clone the repository:

git clone [your_repository_url]
cd [your_repository_name]
Create a virtual environment (recommended):

python -m venv venv 
pip install -r requirements.txt

## Project Structure:
* Ensure your project structure looks like this:

face-swapper/
├── app.py

├── image_process.py

├── templates/

│   └── index.html

└── static/

    ├── css/

    │   └── styles.css

    ├── uploads/

    └── results/     

The uploads and results directories should be created manually if they don't exist.

## Run the application:

python app.py
The app will start on http://127.0.0.1:5000.

Usage
Open your web browser and navigate to http://127.0.0.1:5000.

Click "Choose First Image" and "Choose Second Image" to select your images.

Click the "Swap Faces" button.


The application will process the images and display the original and swapped versions below the upload form.


