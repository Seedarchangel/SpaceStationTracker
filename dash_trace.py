import datetime
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json
import plotly.plotly as py
from plotly import tools
from pyorbital.orbital import Orbital
import plotly.graph_objs as go 

def initname():
    return [
    {'label': 'ISS (ZARYA)', 'value': 'ISS (ZARYA)'},
    {'label': 'TIANGONG 1', 'value': 'TIANGONG 1'},
    {'label': "FLOCK 2E'-1", 'value': "FLOCK 2E'-1"},
    {'label': "FLOCK 2E'-3", 'value': "FLOCK 2E'-3"},
    {'label': 'FLOCK 2E-1', 'value': 'FLOCK 2E-1'},
    {'label': 'FLOCK 2E-3', 'value': 'FLOCK 2E-3'},
    {'label': 'FLOCK 2E-5', 'value': 'FLOCK 2E-5'},
    {'label': 'FLOCK 2E-7', 'value': 'FLOCK 2E-7'},
    {'label': "FLOCK 2E'-5", 'value': "FLOCK 2E'-5"},
    {'label': "FLOCK 2E'-6", 'value': "FLOCK 2E'-6"},
    {'label': "FLOCK 2E'-8", 'value': "FLOCK 2E'-8"},
    {'label': "FLOCK 2E'-9", 'value': "FLOCK 2E'-9"},
    {'label': "FLOCK 2E'-11", 'value': "FLOCK 2E'-11"},
    {'label': "FLOCK 2E'-12", 'value': "FLOCK 2E'-12"},
    {'label': "FLOCK 2E'-13", 'value': "FLOCK 2E'-13"},
    {'label': "FLOCK 2E'-14", 'value': "FLOCK 2E'-14"},
    {'label': "FLOCK 2E'-16", 'value': "FLOCK 2E'-16"},
    {'label': "FLOCK 2E'-15", 'value': "FLOCK 2E'-15"},
    {'label': 'TIANGONG-2', 'value': 'TIANGONG-2'},
    {'label': "FLOCK 2E'-18", 'value': "FLOCK 2E'-18"},
    {'label': "FLOCK 2E'-17", 'value': "FLOCK 2E'-17"},
    {'label': "FLOCK 2E'-19", 'value': "FLOCK 2E'-19"},
    {'label': "FLOCK 2E'-20", 'value': "FLOCK 2E'-20"},
    {'label': 'BANXING-2', 'value': 'BANXING-2'},
    {'label': 'STARS-C', 'value': 'STARS-C'},
    {'label': 'ITF-2', 'value': 'ITF-2'},
    {'label': 'WASEDA-SAT3', 'value': 'WASEDA-SAT3'},
    {'label': 'AOBA-VELOX 3', 'value': 'AOBA-VELOX 3'},
    {'label': 'LEMUR-2-REDFERN-GOES', 'value': 'LEMUR-2-REDFERN-GOES'},
    {'label': 'LEMUR-2-TRUTNA', 'value': 'LEMUR-2-TRUTNA'},
    {'label': 'LEMUR-2-AUSTINTACIOUS', 'value': 'LEMUR-2-AUSTINTACIOUS'},
    {'label': 'LEMUR-2-TRUTNAHD', 'value': 'LEMUR-2-TRUTNAHD'},
    {'label': 'HAVELSAT', 'value': 'HAVELSAT'},
    {'label': 'SOMP 2', 'value': 'SOMP 2'},
    {'label': 'COLUMBIA', 'value': 'COLUMBIA'},
    {'label': 'SGSAT', 'value': 'SGSAT'},
    {'label': 'CXBN-2', 'value': 'CXBN-2'},
    {'label': 'ICECUBE', 'value': 'ICECUBE'},
    {'label': 'PHOENIX', 'value': 'PHOENIX'},
    {'label': 'X-CUBESAT', 'value': 'X-CUBESAT'},
    {'label': 'QBEE50-LTU-OC', 'value': 'QBEE50-LTU-OC'},
    {'label': 'ALTAIR PATHFINDER', 'value': 'ALTAIR PATHFINDER'},
    {'label': 'SHARC', 'value': 'SHARC'},
    {'label': 'ZA-AEROSAT', 'value': 'ZA-AEROSAT'},
    {'label': 'LINK', 'value': 'LINK'},
    {'label': 'CSUNSAT 1', 'value': 'CSUNSAT 1'},
    {'label': 'UPSAT', 'value': 'UPSAT'},
    {'label': 'SPACECUBE', 'value': 'SPACECUBE'},
    {'label': 'HOOPOE', 'value': 'HOOPOE'},
    {'label': 'CHALLENGER', 'value': 'CHALLENGER'},
    {'label': 'NJUST-1', 'value': 'NJUST-1'},
    {'label': 'UNSW-ECO', 'value': 'UNSW-ECO'},
    {'label': 'DUTHSAT', 'value': 'DUTHSAT'},
    {'label': 'LILACSAT-1', 'value': 'LILACSAT-1'},
    {'label': 'NSIGHT-1', 'value': 'NSIGHT-1'},
    {'label': 'SNUSAT-1', 'value': 'SNUSAT-1'},
    {'label': 'QBITO', 'value': 'QBITO'},
    {'label': 'AALTO-2', 'value': 'AALTO-2'},
    {'label': 'SUSAT', 'value': 'SUSAT'},
    {'label': 'I-INSPIRE II', 'value': 'I-INSPIRE II'},
    {'label': 'POLYITAN-2-SAU', 'value': 'POLYITAN-2-SAU'},
    {'label': 'SNUSAT-1B', 'value': 'SNUSAT-1B'},
    {'label': 'EXALTA-1', 'value': 'EXALTA-1'},
    {'label': 'AOXIANG-1', 'value': 'AOXIANG-1'},
    {'label': 'BEEAGLESAT', 'value': 'BEEAGLESAT'},
    {'label': 'ATLANTIS', 'value': 'ATLANTIS'},
    {'label': 'SOYUZ-MS 06', 'value': 'SOYUZ-MS 06'},
    {'label': 'PROGRESS-MS 07', 'value': 'PROGRESS-MS 07'},
    {'label': 'SIMPL', 'value': 'SIMPL'},
    {'label': 'ECAMSAT', 'value': 'ECAMSAT'},
    {'label': 'ASTERIA', 'value': 'ASTERIA'},
    {'label': 'DELLINGR (RBLE)', 'value': 'DELLINGR (RBLE)'},
    {'label': 'TECHEDSAT 6', 'value': 'TECHEDSAT 6'},
    {'label': 'OSIRIS-3U', 'value': 'OSIRIS-3U'},
    {'label': 'SOYUZ-MS 07', 'value': 'SOYUZ-MS 07'},
    {'label': 'PROGRESS-MS 08', 'value': 'PROGRESS-MS 08'}]



app = dash.Dash(__name__)
app.css.append_css({"external_url": "https://cdnjs.cloudflare.com/ajax/libs/spectre.css/0.5.0/spectre.min.css"})
app.layout = html.Div([
   html.H4('Visualization of Space Station Positions for the Current Day'),
   html.Div([
   html.Label("Space Station Name"),
   dcc.Dropdown(
    options=initname(),
    value='ISS (ZARYA)',
    multi=True,
    id='SSDropdown'
)
],
  style={  'width': '50%',
           'display': 'inline-block'}

),
    dcc.Graph(
    style={'height': "100%",
           'width': "100%"
    },
    id='datagraph'
    ),
    html.Label("Hour(in UTC)"),
    html.Div(
    
    dcc.Slider(
        id='hour',
        min=0,
        max=24,
        marks={i: '{}:00'.format(i) for i in range(24)},
        value=datetime.datetime.utcnow().hour,),
    style = {"height": "50"}
    ),
    html.Label("Minute(in UTC)"),
    html.Div(
    dcc.Slider(
        id="minute",
        min=0,
        max=60,
        marks={i: '{}'.format(i) for i in range(60)},
        value=datetime.datetime.utcnow().minute)
    )

])

#@app.callback(
#    Output('datagraph','figure'),
#    [Input('SSDropdown','value')
#    ]
#)
#def returnplot(spaceStation):
#    orb = Orbital(spaceStation,tle_file='stations.txt')
#    now = datetime.datetime.utcnow()
#    location = orb.get_lonlatalt(now)
#    print location


@app.callback(
    Output('datagraph','figure'),
    [Input('SSDropdown','value'),
     Input('hour', 'value'),
     Input('minute','value')
    ]
)
def initMap(input,hourval,minuteval):
    #orb = Orbital(input,tle_file='stations.txt')
    print hourval
    print minuteval
    latlist = []
    longlist = []
    textlist = []
    now = datetime.datetime.utcnow()
    newdate = now.replace(hour=hourval, minute=minuteval)
    if type(input) is list:
        textlist = input
        for a in input:
            orb = Orbital(a,tle_file='stations.txt')
            locationset = orb.get_lonlatalt(newdate)
            latlist.append(locationset[0])
            longlist.append(locationset[1])
    else:
        textlist = [input]
        print textlist
        orb = Orbital(input, tle_file='stations.txt')
        locationset = orb.get_lonlatalt(newdate)
        latlist = [locationset[0]]
        longlist = [locationset[1]]
        print latlist
        print longlist
    data = [ dict(
            text = textlist,
            lat = latlist,
            mode = "markers+text",
            lon = longlist,
            type = "scattergeo",
            showlegend = True,
            textposition = "bottom center"
        )
        ]
    layout = dict(
            width = 1000,
            height = 700,
        geo = dict(

            scope = 'world',
            showland = True,
            showframe = False,
            #landcolor = "rgb(212, 212, 212)",
            #subunitcolor = "rgb(255, 255, 255)",
            countrycolor = "rgb(255, 255, 255)",
            #showlakes = True,
            #showsubunits = True,
            showcountries = True,
            projection = dict(type = "orthographic"),
           # lonaxis = dict(
           #     showgrid = False,
           #     gridwidth = 0.5,
           #     range= [ -1080, 1080.0 ],
           #     dtick = 5
           # ),
           # lataxis = dict (
           #     showgrid = False,
           #     gridwidth = 0.5,
           #     range= [ -1080, 1080 ],
           #     dtick = 5
           # )
        )
    )
    fig = {'data': data, 'layout': layout}
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
