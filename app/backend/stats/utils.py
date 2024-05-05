# title: utils.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-30 13:55:30
# Description: This file contains utility functions for different statistical operations

from pathlib import Path
from jinja2 import Template

from app.core.config import template_base_dir


# This is a decorator to generate a graph template given a plotly figure
def create_graph(file_name=None) -> str:
    def generate_graph(func):
        def wrapper(*args, **kwargs):
            fig = func(*args, **kwargs)
            # fig.update_layout(template="plotly_light") # Optional to change the theme
            fig.update_layout(
                margin=dict(l=20, r=250, t=80, b=0),
                autosize=True,
                legend=dict(x=20, y=1),
            )
            template_path = Path(template_base_dir, file_name)
            template = {
                "fig": fig.to_html(
                    full_html=False,
                    include_plotlyjs=False,
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
