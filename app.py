import dash
from dash import dcc,html


app = dash.Dash()

app.layout = html.H1("Das ist ein Text")



if __name__ == "__main__":
    app.run(debug=True)