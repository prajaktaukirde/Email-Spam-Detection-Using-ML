from flask import Flask, render_template, request
import pickle
import os
import re
import string
import numpy as np

app = Flask(__name__)

#======================== Loading Models ==================================================
mail_model = pickle.load(open('logistic_regression.pkl', 'rb'))
mail_feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

news_model = pickle.load(open('fake_news_model.pkl', 'rb'))
news_vectorizer = pickle.load(open('news_vectorizer.pkl', 'rb'))

# Phishing model - load when available
phishing_model = None
try:
    import joblib
    phishing_model = joblib.load('phishing_model.pkl')
except:
    print("Phishing model not found - using rule-based detection")

#======================== Helper Functions ================================================

def predict_mail(input_text):
    input_user_mail = [input_text]
    input_data_features = mail_feature_extraction.transform(input_user_mail)
    prediction = mail_model.predict(input_data_features)
    return prediction

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

def predict_news(input_text):
    cleaned_text = clean_text(input_text)
    news_vec = news_vectorizer.transform([cleaned_text])
    prediction = news_model.predict(news_vec)
    return prediction

def predict_phishing_url(url):
    """Predict if URL is phishing using the trained model or rule-based fallback"""
    try:
        # If model is available, use it (would need feature extraction matching training)
        # For now, use enhanced rule-based detection
        
        phishing_score = 0
        url_lower = url.lower()
        
        # Check for suspicious patterns
        suspicious_words = ['login', 'verify', 'account', 'secure', 'update', 'confirm', 'billing', 'auth', 'signin', 'password', 'credential']
        for word in suspicious_words:
            if word in url_lower:
                phishing_score += 1
        
        # Check for IP address
        if re.search(r'\d+\.\d+\.\d+\.\d+', url):
            phishing_score += 2
        
        # Check for HTTP (not HTTPS)
        if url.startswith('http://'):
            phishing_score += 1
        
        # Check for suspicious TLDs
        suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.top', '.xyz', '.work', '.date', '.click']
        for tld in suspicious_tlds:
            if tld in url_lower:
                phishing_score += 2
        
        # Check for character substitution (e.g., paypa1, amaz0n, faceb00k)
        if any(sub in url for sub in ['0', '1']):
            phishing_score += 2
        
        # Check URL length (phishing URLs often very long)
        if len(url) > 75:
            phishing_score += 1
        
        # Check for multiple subdomains
        if url.count('.') > 3:
            phishing_score += 1
        
        # Check for @ symbol (used to trick users)
        if '@' in url:
            phishing_score += 3
        
        confidence = round(min(phishing_score / 10 * 100, 100), 2)
        
        if phishing_score >= 4:
            return 'phishing', confidence
        else:
            return 'legitimate', round(100 - confidence, 2)
            
    except Exception as e:
        return None, str(e)

#======================== Routes ==========================================================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/email', methods=['GET', 'POST'])
def email_detection():
    if request.method == 'POST':
        mail = request.form.get('mail', '').strip()
        if not mail:
            return render_template('index.html', error="Please enter email content to analyze.")
        predicted_mail = predict_mail(input_text=mail)
        return render_template('index.html', classify=predicted_mail, mail=mail)
    return render_template('index.html')

@app.route('/news', methods=['GET', 'POST'])
def news_detection():
    if request.method == 'POST':
        news = request.form.get('news', '').strip()
        if not news:
            return render_template('news.html', error="Please enter news content to analyze.")
        prediction = predict_news(input_text=news)
        return render_template('news.html', prediction=prediction[0], news=news)
    return render_template('news.html')

@app.route('/phishing', methods=['GET', 'POST'])
def phishing_detection():
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        if not url:
            return render_template('phishing.html', error="Please enter a URL to analyze.")
        
        prediction, confidence = predict_phishing_url(url)
        
        if prediction is None:
            return render_template('phishing.html', error=confidence)
        
        return render_template('phishing.html',
                               prediction=prediction,
                               confidence=confidence,
                               url=url)
    
    return render_template('phishing.html')

if __name__ == '__main__':
    app.run(debug=True)