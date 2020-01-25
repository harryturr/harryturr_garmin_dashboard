import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from worker_functions import num_to_month
import pandas as pd
import numpy as np
import react_buttons

#from textwrap import dedent as d
#import json
#import gpxpy

# from react_buttons import react_buttons
# import react_buttons as rb
# import temp_react_package


#df = pd.read_csv(
#    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
#)

df2 = pd.read_csv("activities_5_correct.csv")
df2 = df2.reindex(
    columns=[
        "Activity_Type",
        "Date",
        "Title",
        "Distance",
        "Calories",
        "Time",
        "Avg_HR",
        "Max_HR",
        "Avg_Pace",
        "Elev_Gain",
    ]
)

df_overviewdata = df2

df2.Time = [
    int(i.split(":")[0]) * 60 + int(i.split(":")[1]) * 1 + int(i.split(":")[2]) / 60
    for i in df2.Time
]


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
external_stylesheets = ["./assets/style.css"]

styles = {"pre": {"border": "thin lightgrey solid", "overflowX": "scroll"}}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

test_dict = []
for i in df2.Activity_Type.unique():
    test_dict.append(dict(label=i, value=i))
header_dict = []
for i in list(df2):
    header_dict.append(dict(label=i, value=i))

counter = len(df2)
app.layout = html.Div(
    children=[
        
        html.H1(children="H A R R Y T U R R"),
        html.H4(children="plotting garmin .gpx data in a 'dash'"),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H1(
                            id="no-act-text",
                            children=str(counter),
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                                "font-size": "750%",
                            },
                        ),
                        html.H6(
                            children="total activities",
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    style={
                        "width": "28%",
                        "display": "inline-block",
                        "align-items": "center",
                        "justify-content": "center",
                    },
                    className="mini_container",
                ),
                html.Div(
                    children=[
                        html.H1(
                            id="distance-text",
                            children=str(counter),
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                                "font-size": "750%",
                            },
                        ),
                        html.H6(
                            children="total kilometers",
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    style={
                        "width": "28%",
                        "display": "inline-block",
                        "align-items": "center",
                        "justify-content": "center",
                    },
                    className="mini_container",
                ),


html.Div(
                    children=[
                        html.H1(
                            id="time-text",
                            children=str(counter),
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                                "font-size": "750%",
                            },
                        ),
                        html.H6(
                            children="total hours",
                            style={
                                # "width": "45%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    style={
                        "width": "28%",
                        "display": "inline-block",
                        "align-items": "center",
                        "justify-content": "center",
                    },
                    className="mini_container",
                ),

            ],
            style={
                "width": "100%",
                "display": "inline-block",
                "align-items": "center",
                "justify-content": "space-between",
                # "marginBottom": "-10em",
            },
        ),
        html.Br(),
        
        html.Div(
            children=[
                dcc.Graph(
                    id="graph-with-slider",
                    style={
                        "width": "100%",
                        "display": "inline-block",
                        "align-items": "center",
                        "justify-content": "center",
                    },
                )
            ],
            className="mini_container",
            style={
                "width": "65%",
                "display": "inline-block",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        
                        html.Div(
                            id="month-to-month",
                            children=[html.P(children="select your month range:")],
                            style={
                                "width": "100%",
                                "display": "inline-block",
                                "align-items": "center",
                                "justify-content": "center",
                                "padding-left": "5%",
                                # "padding-right": "50%",
                            },
                        ),
                        dcc.RangeSlider(
                            id="month-slider",
                            min=pd.to_numeric(df2["Date"].str[5:7].min()),
                            max=pd.to_numeric(df2["Date"].str[5:7].max()),
                            value=[
                                pd.to_numeric(df2["Date"].str[5:7].min()),
                                pd.to_numeric(df2["Date"].str[5:7].max()),
                            ],
                            marks={
                                str(month): str(month)
                                for month in pd.to_numeric(
                                    df2["Date"].str[5:7].unique()
                                )
                            },
                            step=None,
                        ),
                        html.Br(),
                        html.Div([
    react_buttons.ReactButtons(
        id='input',
        value = 'sample value testing',
        label='my-label',
        test_text='none',
        children = 'please click a button'
    ),
    html.Div(id='output')
]),
                    ],
                    className="mini_container",
                ),
                
                html.Div(
                    children = [
                        html.P("pick your y-axis", style = {"font-weight": "bold"}),

                dcc.RadioItems(
                    id="yaxis-radio",
                    options=[
                        header_dict[3],
                        header_dict[4],
                        header_dict[5],
                        header_dict[6],
                        header_dict[7],
                        header_dict[8],
                        header_dict[9],
                    ],
                    value=header_dict[3]["value"],
                    style={"marginBottom": "0em"},
                ),
                    ],                    className="mini_container"

                ),
                


                html.Div(
                    children = [
                        html.P("choose activity types", style = {"font-weight": "bold"}),
                    
                dcc.Checklist(
                    id="activity-checklist",
                    options=[test_dict[0], test_dict[1], test_dict[2], test_dict[3]],
                    value=[
                        test_dict[0]["value"],
                        test_dict[1]["value"],
                        test_dict[2]["value"],
                        test_dict[3]["value"],
                    ],
                    style={"marginBottom": "0em"},
                ),

                    ],                    className="mini_container",

                )
                
            ],
            style={
                "width": "25%",
                "display": "inline-block",
                "align-items": "center",
                "justify-content": "center",
            },
        ),
        # generalize this instead of hardcoding
        html.Div(
            children=[
                html.Div(id="my-div"),
                # interactive selecting point
                # https://dash.plot.ly/interactive-graphing
                html.H6(
                    id="activity-pick-a-point",
                    children="select a point to see more details below",
                    className="mini_container",
                    style={
                        "width": "90%",
                        "display": "inline-block",
                        "align-items": "center",
                        "justify-content": "center",
                        #"background-color": "yellow"
                    },
                ),
                # put plots here
                html.Div(
                    [
                        html.Div(
                            children=[dcc.Graph(id="elevation-graph")],
                            className="mini_container",
                            style={"width": "31%", 
                            "display": "inline-block",
                            "align-items": "center",
                            "justify-content": "center"},
                        ),
                        html.Div(
                            children=[dcc.Graph(id="lat-lon-graph")],
                            className="mini_container",
                            style={"width": "31%", 
                            "display": "inline-block",
                            "align-items": "center",
                            "justify-content": "center"},
                        ),
                        html.Div(
                            children = [
                                #left side of stat box
                            html.Div(
                                children = [
                                    html.H5("activity stats"),
                                                                
                                html.P("date:", style = {"font-weight": "bold"}),
                                html.P("activity type:", style = {"font-weight": "bold"}),
                                html.P("distance (km):", style = {"font-weight": "bold"}),
                                html.P("calories (kCal):", style = {"font-weight": "bold"}),
                                html.P("time (hrs):", style = {"font-weight": "bold"}),
                                html.P("avg HR (bpm):", style = {"font-weight": "bold"}),
                                html.P("max HR (bpm):", style = {"font-weight": "bold"}),
                                html.P("avg pace (kph):", style = {"font-weight": "bold"}),
                                html.P("elev gain (m):", style = {"font-weight": "bold"})
                                ],style={"width": "45%", 
                            "display": "inline-block",
                            "align-items": "center",
                            "justify-content": "center"}
                            ),
                            # right side of stat box
                            html.Div(
                                children = [
                                    html.H5(""),
                                    html.P(children = "...", id = 'date_text'),
                                    html.P(children = "...", id = 'type_text'),
                                    html.P(children = "...", id = 'distance_text'),
                                    html.P(children = "...", id = 'calories_text'),
                                    html.P(children = "...", id = 'time_text'),
                                    html.P(children = "...", id = 'avg_hr_text'),    
                                    html.P(children = "...", id = 'max_hr_text'), 
                                    html.P(children = "...", id = 'avg_pace_text'), 
                                    html.P(children = "...", id = 'elev_gain_text'),                             
                            
                                ],style={"width": "50%", 
                            "display": "inline-block",
                            "align-items": "center",
                            "justify-content": "center"}
                            ),
                            html.Br(), html.Br(), html.Br(), html.Br(),
                            html.H5("powered by Plot.ly Dash")
                            
                                ],
                            className = "mini_container",
                            style={"width": "21%", 
                            "display": "inline-block",
                            "align-items": "center",
                            "justify-content": "center"},

                        ),

                        
                    ],
                    style={"width": "100%", "display": "inline-block","align-items": "center","justify-content": "center"},
                ),
                
               
            ],
            style={
                "width": "100%",
                "display": "inline-block",
                "align-items": "center",
                "justify-content": "center"
                
            },
        ),
        html.Div(
            [html.H6(id="gasText"), html.P("harrisonn griffin, github.com/harryturr")], id="gas", className="mini_container",
            style = {"width" : "90%"}
        ),
    ]
)


""" 
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input('month-slider', 'value'),
    Input('activity-checklist','value')]
)
def update_output_div(value, activity_name):
    filtered_df2 = df2[(pd.to_numeric(df2['Date'].str[5:7])< value[1]+1) & (pd.to_numeric(df2['Date'].str[5:7])>value[0]-1)]
    for i in activity_name: #filtered_df2.Activity_Type.unique()
        df2_by_activity = filtered_df2[filtered_df2['Activity_Type'] == i]
    return 'You\'ve entered "{}"'.format(len(df2_by_activity['Date']))
 """


@app.callback([Output('output', 'children'),Output('month-slider', 'value')], [Input('input', 'test_text')])
def update_test(test):
    return ([test],
    [int(test[:2]),int(test[3:5])])




@app.callback(
    [
        Output("activity-pick-a-point", "children"),
        #Output("activity-type-text", "children"),
        #Output("activity-y-text", "children"),
        #Output("selected-data", "children"),
        Output("elevation-graph", "figure"),
        Output("lat-lon-graph", "figure"),
        Output("date_text", "children"),
        Output("type_text", "children"),
        Output("distance_text", "children"),
        Output("calories_text", "children"),
        Output("time_text", "children"),
        Output("avg_hr_text", "children"),
        Output("max_hr_text", "children"),
        Output("avg_pace_text", "children"),
        Output("elev_gain_text", "children")

    ],
    [Input("graph-with-slider", "selectedData")],
)
def display_selected_data(selectedData):
    # selectedData = dict(selectedData)
    # activity_date = selectedData['points'][0]['x']
    # return json.dumps(selectedData, indent=2)
    # return str(selectedData['points'][0]['x']),str(selectedData['points'][0]['y'],str(selectedData['points'][0]['text']))

    data_date = selectedData["points"][0]["x"]

    df2 = pd.read_csv("./data_rename_csv/" + str(data_date) + ".csv")

    # file_path = "./data_rename/" + str(data_date) + ".gpx"
    # print(file_path)
    # gpx_file = open(file_path, 'r')
    # gpx = gpxpy.parse(gpx_file)
    print("success")
    #print(data_date)
    #print(df22.loc[df22['Date'] == data_date]['Calories'])
    # data_gpx = gpx.tracks[0].segments[0].points
    # df_gpx = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
    # for point in data_gpx:
    #    df_gpx = df_gpx.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)

    print("complete")
    print(df2.lon[0])
    # print(str(df['lon'][0]))

    elev_traces = []
    elev_traces.append(
        dict(
            x=df2["time"],
            y=df2["alt"],
            colorscale="YIOrRd",
            text=df2["alt"],
            mode="lines",
            opacity=0.7,
            marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
            name=i,
        )
    )
    lat_lon_traces = []

    lat_lon_traces.append(
        dict(
            x=df2["lat"],
            y=df2["lon"],
            colorscale="YIOrRd",
            text=df2["lat"],
            mode="lines",
            opacity=0.7,
            marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
            name=i,
        )
    )
    print('what i look for')
    print(df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Time'])
    return (
    html.Div(children = [
        html.H6('You\'ve selected data from {}'.format(selectedData["points"][0]["x"])) ]),
                            #
        #selectedData["points"][0]["y"],
        #selectedData["points"][0]["text"],
        # selectedData["points"][0]["x"] df2.lon[0]
        #df2.lon[0],
        {
            "data": elev_traces,
            "layout": dict(
                xaxis={"title": "time"},
                yaxis={"title": "elevation"},
                margin={"l": 40, "b": 40, "t": 10, "r": 10},
                legend={"x": 0, "y": 1},
                hovermode="closest",
                transition={"duration": 500},
                # clickmode="event+select",
            ),
        },
        {
            "data": lat_lon_traces,
            "layout": dict(
                xaxis={"title": "lattitude"},
                yaxis={"title": "longitude"},
                margin={"l": 40, "b": 40, "t": 10, "r": 10},
                legend={"x": 0, "y": 1},
                hovermode="closest",
                transition={"duration": 500},
                # clickmode="event+select",
            ),
        },
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Date'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Activity_Type'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Distance'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Calories'],
                html.P(["%.1f" % np.float(df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Time'])]),
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Avg_HR'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Max_HR'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Avg_Pace'],
                df_overviewdata.loc[df_overviewdata['Date'] == data_date]['Elev_Gain']

    )

@app.callback(
    [
        Output("graph-with-slider", "figure"),
        Output(component_id="no-act-text", component_property="children"),
        Output(component_id="month-to-month", component_property="children"),
        Output("distance-text", "children"),
        Output("time-text", "children"),
    ],
    [
        Input("month-slider", "value"),
        Input("activity-checklist", "value"),
        Input("yaxis-radio", "value"),
    ],
)
def update_figure(value, activity_name, yaxis):
    print(value)
    counter = 0
    count_sum = 0
    distance_sum = 0
    time_sum = 0
    month_str = num_to_month(value)
    filtered_df2 = df2[
        (pd.to_numeric(df2["Date"].str[5:7]) < value[1] + 1)
        & (pd.to_numeric(df2["Date"].str[5:7]) > value[0] - 1)
    ]
    traces = []
    for i in activity_name:  # filtered_df2.Activity_Type.unique()
        df2_by_activity = filtered_df2[filtered_df2["Activity_Type"] == i]
        traces.append(
            dict(
                x=df2_by_activity["Date"],
                y=df2_by_activity[yaxis],
                text=df2_by_activity["Activity_Type"],
                mode="markers",
                opacity=0.7,
                marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                name=i,
            )
        )
        count_sum = count_sum + np.sum(df2_by_activity[yaxis])
        distance_sum = distance_sum + np.sum(df2_by_activity["Distance"])
        time_sum = time_sum + np.sum(df2_by_activity["Time"])

        counter = counter + len(df2_by_activity["Date"])
    # print(traces)
    return (
        {
            "data": traces,
            "layout": dict(
                xaxis={"title": "Date of Activity"},
                yaxis={"title": yaxis},
                margin={"l": 40, "b": 40, "t": 10, "r": 10},
                legend={"x": 0, "y": 1},
                hovermode="closest",
                transition={"duration": 500},
                clickmode="event+select",
            ),
        },
        # "number of activities : " + str(counter),
        html.P([str(counter)]),
        html.P(month_str[0] + " to " + month_str[1]),
        # "total " + yaxis + ":  \n" + str(count_sum),
        # "total " + yaxis + ":  \n" + str(distance_sum),
        html.P(["%.0f" % distance_sum]),
        html.P(["%.0f" % time_sum]),
    )


# "%.1f" % (21.3331,)
# "%.1f" % distance_sum

if __name__ == "__main__":
    app.run_server(debug=False, port=6970)
