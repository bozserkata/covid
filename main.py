import wbgapi as wb
import pandas as pd


pd.set_option('display.max_rows', 50)
series = wb.series.info(q='population')
series = wb.series.info()
series = wb.series.info(q='gdp')

'''
countries = wb.get_countries()
regions = wb.get_regions()
incomelevels = wb.get_incomelevels()'''

gdppercap = wb.data.DataFrame('NY.GDP.PCAP.CD',time=range(2017, 2020), labels=True)

gdppercap.to_csv('gdp_per_capita.csv', index=False)

series = wb.series.info(q='health')
print(series)

healthpercap = wb.data.DataFrame('SH.XPD.CHEX.PC.CD',time=range(2017, 2020), labels=True)

healthpercap.to_csv('health_expenditure_per_capita.csv', index=False)