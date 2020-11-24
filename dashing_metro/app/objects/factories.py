from dashing_metro.backend.imports import *
import dashing_metro as dm


def generate_delay_histogram(df: pd.DataFrame, transport_types=dm.backend.variables.transport_labels):
    sub_df = df.copy()
    sub_df = sub_df[sub_df['product'].isin(transport_types)]
    fig = px.histogram(sub_df, x='delay', histnorm='probability density', nbins=200)
    return fig
