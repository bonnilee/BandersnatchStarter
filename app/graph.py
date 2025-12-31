from altair import Chart, Tooltip
from pandas import DataFrame

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    """Create an interactive scatter plot visualization.

    Args:
        df: DataFrame containing monster data
        x: Column name for x-axis
        y: Column name for y-axis
        target: Column name for color encoding

    Returns:
        Altair Chart object
    """

    # Chart properties for dark theme
    properties = {
        "width": 700,
        "height": 500,
        "background": "#1e1e2f",
        "padding": 10
    }

    graph = (
        Chart(df, title=f"{y} by {x} for {target}")
        .mark_circle(size=100)
        .encode(
            x=x,
            y=y,
            color=target,
            tooltip=Tooltip(df.columns.to_list())
        )
        .properties(**properties)
        .configure_axis(
            labelColor="white",
            titleColor="white"
        )
        .configure_title(
            color="white",
            fontSize=18,
            font="Verdana"
        )
        .configure_legend(
            labelColor="white",
            titleColor="white"
        )
    )

    return graph

