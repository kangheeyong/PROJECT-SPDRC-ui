import pandas as pd
import numpy as np
import plotly.express as px


def calc(path, wave1, wave2):
    data = pd.read_csv(path)
    df = pd.DataFrame(data[['Time(sec)', wave1, wave2]])
    df = df.assign(lineRatio=df[wave1] / df[wave2], Te=- 0.13/np.log(df[wave1] / df[wave2]))
    #return df.to_html(index=False, justify='center')
    fig = px.line(y=df['Te'])
    return fig
