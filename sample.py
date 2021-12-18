import datetime
import pandas as pd
import matplotlib.pyplot as plt
import io
import openpyxl
import scatter

import matplotlib
 
fonts = set([f.name for f in matplotlib.font_manager.fontManager.ttflist])
print(fonts)

times = ("00:00:00", "03:00:00", "03:00:01", "09:00:15", "02:59:12", "23:59:59")
data1 = [[datetime.datetime.fromisoformat(f"2021-04-20 {t}.000000"), i] for i, t in enumerate(times)]
df1 = pd.DataFrame(data1, columns=['date', 'value'])

times = ("09:12:03", "02:14:50", "20:00:01", "22:33:15")
data2 = [[datetime.datetime.fromisoformat(f"2021-04-20 {t}.000000"), i+3] for i, t in enumerate(times)]
df2 = pd.DataFrame(data2, columns=['date', 'value'])

#fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(9, 6))

fig = plt.figure()
ax = fig.add_subplot(111, xlabel='時刻', ylabel='値')

scatter.init(ax)

scatter.ax_scatter(ax, df1['date'].to_list(), df1['value'].to_list(), "a")
scatter.ax_scatter(ax, df2['date'].to_list(), df2['value'].to_list(), "b")

#scatter.df_scatter(df1, ax, 'date', 'value', "a")
#scatter.df_scatter(df2, ax, 'date', 'value', "b")

wb = openpyxl.Workbook()
ws = wb.active

img_data = io.BytesIO()
fig.savefig(img_data, format='png')
img = openpyxl.drawing.image.Image(img_data)
ws.add_image(img, 'A1')

#plt.show()
wb.save("out.xlsx")