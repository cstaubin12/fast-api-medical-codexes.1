from flask import Flask
import pandas as pd


df = pd.read_csv('./data/diagnoses2019.csv')

app = Flask(__name__)


@app.route('/', methods=['get'])
def home():
    return 'this is an api service for MN ICD code details'


@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/icd/<value>', methods=["GET"])
def icd(value):
    filtered = df[df['principal_diagnosis_code'] == value]
    return filtered.to_json(orient="records")


if __name__ == '__main__':
    app.run(debug=True)
