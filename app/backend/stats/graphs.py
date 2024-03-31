# title: graphs.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:44
# Description: This file contains graphing functionality for data parsed from backend

import numpy as np
import polars as pl
import plotly.express as px
from pathlib import Path

from app.backend.stats.utils import create_graph

# This is a sample function to create a scatter plot
plot_path1 = Path("partials/graphs/test_plot.html")
plot_path2 = Path("partials/graphs/test_plot2.html")


@create_graph(file_name=plot_path1)
def grade_data(data=None) -> px.scatter:
    # This is a sample function to create a scatter plot
    num_rows = 200
    rng = np.random.default_rng(seed=7)
    students_data = {
        "Grade": rng.exponential(scale=10, size=num_rows),
        "Year": rng.integers(low=1995, high=2023, size=num_rows),
        "School": rng.choice(
            ["Engineering", "Social Science", "English"], size=num_rows
        ),
    }
    students = pl.DataFrame(students_data)
    fig = px.scatter(
        students,
        x="Grade",
        y="Year",
        color="School",
        title="Grade vs Year",
    )
    fig.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        template="ggplot2",
        margin=dict(l=20, r=150, t=80, b=50),
    )
    return fig


if __name__ == "__main__":
    fig = gdp_data()
    print(fig)
