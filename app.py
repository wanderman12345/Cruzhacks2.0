import pandas as pd
from flask import Flask, request, render_template
app = Flask(__name__)


#loads csv file into 3 arrays
df = pd.read_csv("data/list.csv")

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form['query'].lower()
        index = -1
        for i in range(len(df)):
            if df["Product"][i] == query:
                print(i)
                index = i

        if index == -1:
            results = "Item not found"
        else:
            results = df["Impact"][index]

        return render_template("index.html", query=query, results=results)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)