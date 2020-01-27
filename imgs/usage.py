import react_buttons
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    react_buttons.ReactButtons(
        id='input',
        value = 'sample value testing',
        label='my-label',
        test_text='none',
        children = 'please click a button'
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'test_text')])
def update_test(test):
    return 'month range, react_buttons: {}'.format(test)


if __name__ == '__main__':
    app.run_server(debug=True)
