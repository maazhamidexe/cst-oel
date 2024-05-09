from flask import Flask, request, redirect, url_for, render_template
from textblob import TextBlob

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']
        if action == 'Analyze Sentiment':
            sentiment = TextBlob(text).sentiment.polarity
            sentiment_classification = classify_sentiment(sentiment)
            return redirect(url_for('display_result', result=f"Sentiment: {sentiment_classification}"))
        elif action == 'Correct Spelling':
            corrected = TextBlob(text).correct().string
            return redirect(url_for('display_result', result=f"Corrected Text: {corrected}"))
    return render_template('index.html')

@app.route('/result')
def display_result():
    result = request.args.get('result', '')
    return render_template('result.html', result=result)

def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    app.run(debug=True)