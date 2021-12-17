import datetime
import pandas as pd
import matplotlib.pyplot as plt
import io
import openpyxl
import scatter

times = ("00:00:00", "03:00:00", "03:00:01", "09:00:15", "02:59:12", "23:59:59")

data = [[datetime.datetime.fromisoformat(f"2021-04-20 {t}.000000"), i] for i, t in enumerate(times)]

df = pd.DataFrame(data, columns=['date', 'value'])

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(9, 6))

scatter.plot(df, axes)

wb = openpyxl.Workbook()
ws = wb.active

img_data = io.BytesIO()
fig.savefig(img_data, format='png')
img = openpyxl.drawing.image.Image(img_data)
ws.add_image(img, 'A1')

#plt.show()
wb.save("out.xlsx")