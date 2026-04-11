# AI Detection Hub

A web application with three Machine Learning detection systems: Email Spam Detection, Fake News Detection, and Phishing URL Detection. Built with Python, Flask, and scikit-learn.

## Features

| Feature | Model | Accuracy |
|---------|-------|----------|
| Email Spam Detection | Logistic Regression + TF-IDF | 97% |
| Fake News Detection | Logistic Regression + TF-IDF | 98.63% |
| Phishing URL Detection | Random Forest | 96% |

## Tech Stack

- **Python 3.11** - Programming language
- **Flask** - Web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **Bootstrap 5** - CSS framework
- **Chart.js** - Data visualization
- **Font Awesome** - Icons

## Project Structure

```
.
├── app.py                                    # Flask application
├── templates/
│   ├── home.html                            # Home page with pie chart
│   ├── index.html                           # Email spam detection
│   ├── news.html                            # Fake news detection
│   └── phishing.html                        # Phishing URL detection
├── notebooks/
│   ├── Email_Spam_Message_Classification_Using_Machine_Learning.ipynb
│   ├── News_Detectio.ipynb
│   └── URLdetection.ipynb
├── models/
│   ├── logistic_regression.pkl              # Email model
│   ├── feature_extraction.pkl               # Email vectorizer
│   ├── fake_news_model.pkl                  # News model
│   ├── news_vectorizer.pkl                  # News vectorizer
│   └── phishing_model.pkl                   # Phishing model
├── requirements.txt                         # Dependencies
└── README.md                                # This file
```

## How to Run

### Prerequisites

- Python 3.11 (required for TensorFlow compatibility)
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/prajaktaukirde/Email-Spam-Detection-Using-ML.git
   cd Email-Spam-Detection-Using-ML
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   
   Navigate to `http://127.0.0.1:5000`

## Model Details

### Email Spam Detection
- **Algorithm**: Logistic Regression
- **Features**: TF-IDF Vectorization
- **Dataset**: SMS Spam Collection (~5,500 emails)

### Fake News Detection
- **Algorithm**: Logistic Regression
- **Features**: TF-IDF with text cleaning
- **Dataset**: True.csv + Fake.csv (~44,800 articles)

### Phishing URL Detection
- **Algorithm**: Random Forest (100 estimators)
- **Features**: URL structure analysis (40+ features)
- **Dataset**: PhiUSIIL Phishing URL Dataset (~100,000 URLs)


