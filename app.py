from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

#========================loading the save files==================================================
mail_model = pickle.load(open('logistic_regression.pkl','rb'))
mail_feature_extraction = pickle.load(open('feature_extraction.pkl','rb'))

# Note: News detection model - placeholder for now
# You can load your news detection model here when available
# news_model = pickle.load(open('news_model.pkl','rb'))
# news_vectorizer = pickle.load(open('news_vectorizer.pkl','rb'))

def predict_mail(input_text):
    input_user_mail = [input_text]
    input_data_features = mail_feature_extraction.transform(input_user_mail)
    prediction = mail_model.predict(input_data_features)
    return prediction

def predict_news(input_text):
    # Placeholder function for news detection
    # Replace this with actual model prediction when you have the news model
    # For now, it returns a simple heuristic-based prediction
    input_news = [input_text]
    # TODO: Load and use actual news detection model
    # prediction = news_model.predict(news_vectorizer.transform(input_news))
    
    # Simple placeholder logic (replace with actual model)
    # Returns 1 (Real) or 0 (Fake)
    import random
    return [random.randint(0, 1)]  # Remove this when you add real model

#======================== Routes ==========================================================

@app.route('/')
def home():
    """Home page with options for Email and News detection"""
    return render_template('home.html')

@app.route('/email', methods=['GET', 'POST'])
def email_detection():
    """Email Spam Detection page"""
    if request.method == 'POST':
        mail = request.form.get('mail', '').strip()
        if not mail:
            return render_template('index.html', error="Please enter email content to analyze.")
        predicted_mail = predict_mail(input_text=mail)
        return render_template('index.html', classify=predicted_mail, mail=mail)

    return render_template('index.html')

@app.route('/news', methods=['GET', 'POST'])
def news_detection():
    """Fake News Detection page"""
    if request.method == 'POST':
        news = request.form.get('news', '').strip()
        if not news:
            return render_template('news.html', error="Please enter news content to analyze.")
        
        # Get prediction from news model
        prediction = predict_news(input_text=news)
        return render_template('news.html', prediction=prediction[0], news=news)

    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)