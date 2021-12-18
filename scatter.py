import matplotlib.dates as mdates

def ax_scatter(ax, x, y, label):
    ax.scatter(x, y, label=label)

def df_scatter(df, ax, x, y, label):
    df.plot(ax=ax, kind="scatter", x=x, y=y, label=label)

def init(ax):
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    #ax.tick_params(axis='x', rotation=270) x軸のラベルを縦書きする場合