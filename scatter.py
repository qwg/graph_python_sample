import matplotlib.dates as mdates

def ax_plot(ax, x, y, label):
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.plot(x, y, label=label)

def df_plot(df, ax, x, y, label):
    df.plot(ax=ax, kind="scatter", x=x, y=y, label=label)