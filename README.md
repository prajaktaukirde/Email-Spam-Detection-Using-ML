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
├── app.py                                    # Flask application main file
├── templates/                                # HTML templates
│   ├── home.html                            # Home page with pie chart
│   ├── index.html                           # Email spam detection UI
│   ├── news.html                            # Fake news detection UI
│   └── phishing.html                        # Phishing URL detection UI
├── static/                                   # Static assets (CSS, JS, images)
│
├── Jupyter Notebooks (Model Training)
│   ├── Email_Spam_Message_Classification_Using_Machine_Learning.ipynb
│   ├── News_Detectio.ipynb
│   └── URLdetection.ipynb
│
├── Models (Trained ML Models)
│   ├── logistic_regression.pkl              # Email spam model (58.8 KB)
│   ├── feature_extraction.pkl               # Email TF-IDF vectorizer (205 KB)
│   ├── fake_news_model.pkl                  # Fake news model (39.8 KB)
│   ├── news_vectorizer.pkl                  # News TF-IDF vectorizer (160 KB)
│   ├── phishing_model.pkl                   # Phishing URL model (7.1 MB)
│   ├── model.h5                             # LSTM plagiarism model (80 MB) ⚠️
│   └── tokenizer.pkl                        # LSTM tokenizer (2.7 MB)
│
├── Datasets
│   ├── mail_data.csv                        # Email dataset (474 KB)
│   ├── True.csv                             # Real news dataset (52 MB) ⚠️
│   ├── Fake.csv                             # Fake news dataset (61 MB) ⚠️
│   ├── PhiUSIIL_Phishing_URL_Dataset.csv    # Phishing URLs (55 MB) ⚠️
│   ├── data.csv                             # Plagiarism data (31 MB) ⚠️
│   └── train_snli.txt                       # SNLI training data (37 MB) ⚠️
│
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation

⚠️ = Large files not in GitHub (see "Large Files" section below)
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

## Large Files (Not in GitHub)

The following files are too large for GitHub (>100MB limit). Download them separately:

| File | Size | Purpose | Download Link |
|------|------|---------|---------------|
| `PhiUSIIL_Phishing_URL_Dataset.csv` | ~55 MB | Phishing training data | [Kaggle Dataset](https://www.kaggle.com/datasets) |
| `data.csv` | ~31 MB | Plagiarism dataset | Generate from notebook |
| `model.h5` | ~80 MB | LSTM plagiarism model | Train using `News_Detectio.ipynb` |
| `train_snli.txt` | ~37 MB | SNLI training data | [SNLI Corpus](https://nlp.stanford.edu/projects/snli/) |

### How to Get These Files

**Option 1: Download from Sources**
1. **Phishing Dataset**: Download from Kaggle or UCI ML Repository
2. **SNLI Data**: Download from Stanford NLP website
3. **Models**: Train using provided Jupyter notebooks

**Option 2: Train Your Own Models**
```bash
# Run the notebooks to generate models
jupyter notebook News_Detectio.ipynb
jupyter notebook URLdetection.ipynb
```

**Option 3: Contact Repository Owner**
Email: [prajaktaukirde576@gmail.com] for direct file access


