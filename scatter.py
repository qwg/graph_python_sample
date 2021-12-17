def plot(df, ax):
    df.plot(ax=ax, kind="scatter", x='date', y='value')