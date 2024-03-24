# title: graphs.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:44
# Description: This file contains graphing functionality for data parsed from backend

import polars as pl
import plotly.express as px
from pathlib import Path
from jinja2 import Template

from app.core.config import template_base_dir


# This is a decorator to generate a graph template given a plotly figure
def create_graph(file_name=None) -> str:
    def generate_graph(func):
        def wrapper(*args, **kwargs):
            fig = func(*args, **kwargs)
            fig.update_layout(template="plotly_dark")
            template_path = Path(template_base_dir, file_name)
            template = {
                "fig": fig.to_html(
                    full_html=False,
                )
            }
            with open(template_path, "w+", encoding="utf-8") as f:
                f.write(
                    Template(
                        """
                <div class="container">
                    {{ fig | safe }}
                </div>
                """
                    ).render(template)
                )
            return file_name

        return wrapper

    return generate_graph


# This is a sample function to create a scatter plot
plot_path = Path("partials/graphs/test_plot.html")


@create_graph(file_name=plot_path)
def create_data() -> px.line:
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")

    fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
    fig.update_traces(textposition="bottom right")
    return fig


if __name__ == "__main__":
    fig = create_data()
    print(fig)
