# Email Spam Detection Using Machine Learning

A web application that uses Machine Learning to classify emails as spam or ham (not spam). Built with Python, Flask, and scikit-learn.

## Tech Stack

- **Python** - Programming language
- **Flask** - Web framework for building the application
- **scikit-learn** - Machine learning library for model training and prediction
- **HTML/CSS** - Frontend styling and structure
- **Bootstrap 5** - CSS framework for responsive design
- **Font Awesome** - Icons for the user interface

## Project Structure+

```
.
├── app.py                                    # Flask application main file
├── templates/
│   └── index.html                           # Web interface template
├── Email_Spam_Message_Classification_Using_Machine_Learning.ipynb  # Jupyter notebook with model training
├── mail_data.csv                            # Dataset for training
├── logistic_regression.pkl                  # Trained ML model
├── feature_extraction.pkl                   # TF-IDF vectorizer
└── README.md                                # Project documentation
```

## How to Run

### Prerequisites

- Python 3.7 or higher installed on your system
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/prajaktaukirde/Email-Spam-Detection-Using-ML.git
   cd Email-Spam-Detection-Using-ML
   ```

2. **Install required dependencies**
   ```bash
   pip install flask scikit-learn
   ```

3. **Run the Flask application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   
   Navigate to `http://127.0.0.1:5000` in your web browser.


## Model Details

The machine learning model was trained using:
- **Algorithm**: Logistic Regression
- **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Dataset**: SMS Spam Collection Dataset


