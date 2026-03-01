# Climate Web App - Final Year Project

Welcome to the **Climate Web App** repository! This project serves as a comprehensive web application integrating a machine learning model to analyze and predict climate-related data. The project consists of a client interface, a server to handle API requests, and a machine learning module for predictions.

## Project Structure

The repository is structured as follows:

- **`climate-web-app/`**: The main directory containing the application components.
  - **`client/`**: Contains the frontend source code (UI/UX) for the web application.
  - **`server/`**: Contains the backend Node.js/Express application.
    - **`app.js`**: The main entry point for the backend server.
    - **`routes/`**: API route definitions.
    - **`controllers/`**: Logic for handling API requests.
    - **`model/`**: Database models/schemas.
  - **`ml-model/`**: Contains the machine learning code and resources.
    - **`train.py`**: Python script for training the machine learning model.
    - **`predict.py`**: Python script for running predictions using the trained model.
    - **`model.pkl`**: The serialized (trained) machine learning model.
  - **`dataset/`**: Directory for storing the datasets used to train and test the machine learning model.

## Tech Stack

- **Frontend**: To be implemented in the `client/` directory.
- **Backend**: Node.js, Express.js (with `cors` and `axios`).
- **Machine Learning**: Python.

## Setup Instructions

### Prerequisites
- [Node.js](https://nodejs.org/) installed
- [Python 3](https://www.python.org/) installed

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd final-year-project
   ```

2. **Install Backend Dependencies:**
   ```bash
   npm install
   ```

3. **Install Python Dependencies:**
   Navigate to the `ml-model` directory and install the required Python packages (e.g., scikit-learn, pandas, etc.) that your scripts rely on.
   ```bash
   # Add your pip install commands here based on ml-model requirements
   ```

## Running the Application

1. **Start the Backend Server:**
   ```bash
   node climate-web-app/server/app.js
   ```

2. **Run the Machine Learning Scripts:**
   To train the model:
   ```bash
   python climate-web-app/ml-model/train.py
   ```
   To make predictions:
   ```bash
   python climate-web-app/ml-model/predict.py
   ```

3. **Start the Frontend:**
   Navigate to the `client/` directory and follow the specific frontend instructions (to be added) to start the UI.

## License

This project is licensed under the ISC License.
