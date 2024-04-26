# title: graphs.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:44
# Description: This file contains graphing functionality for data parsed from backend

import numpy as np
import polars as pl
import plotly.graph_objects as go
from pathlib import Path

from app.backend.stats.utils import create_graph

# This is a sample function to create a scatter plot
plot_path1 = Path("partials/graphs/test_plot.html")
plot_path2 = Path("partials/graphs/test_plot2.html")


@create_graph(file_name=plot_path1)
def grade_data(data: pl.DataFrame = None) -> go.Figure:
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
    fig = go.Figure()
    for school in students["School"].unique().to_list():
        school_data = students.filter(students["School"] == school)
        fig.add_trace(
            go.Scatter(
                x=school_data["Year"],
                y=school_data["Grade"],
                mode="markers",
                name=school,
            )
        )
    fig.update_layout(
        title="Student Grades Over the Years",
        xaxis_title="Year",
        yaxis_title="Grade",
        template="ggplot2",  # Optional to change the theme
    )
    return fig


if __name__ == "__main__":
    fig = grade_data()
    print(fig)
