import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_neural_model():
    df = pd.read_csv("app/data/sample_scores.csv")
    df['weak_area'] = df[['html_score', 'css_score', 'js_score']].idxmin(axis=1)
    X = df[['html_score', 'css_score', 'js_score']]
    y = df['weak_area']

    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def predict_weak_area(model, html, css, js):
    input_data = [[html, css, js]]
    prediction = model.predict(input_data)[0]
    return prediction
