# title: graphs.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:44
# Description: This file contains graphing functionality for data parsed from backend

import polars as pl
import plotly.express as px
from pathlib import Path

from app.backend.stats.utils import create_graph

# This is a sample function to create a scatter plot
plot_path1 = Path("partials/graphs/test_plot.html")
plot_path2 = Path("partials/graphs/test_plot2.html")


@create_graph(file_name=plot_path1)
def gdp_data(data=None) -> px.line:
    # This is a sample function to create a scatter plot
    df = px.data.gapminder().query(
        "country in ['United Kingdom', 'India', 'China', 'Canada']"
    )

    fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
    # fig.update_traces(textposition="bottom right", textfont_size=8)
    fig.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        title="Life Expectancy vs GDP per Capita",
        template="ggplot2",
        margin=dict(l=20, r=150, t=80, b=50),
    )
    return fig


if __name__ == "__main__":
    fig = gdp_data()
    print(fig)
