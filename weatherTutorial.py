import pandas
import matplotlib.pyplot as plt
from datetime import datetime

data = pandas.read_csv("weather_year.csv")

#print(data)
#print(len(data))
#print(data.columns)

#print(data.EDT.head(20))

data.columns=["EDT","maxTemp","meanTemp","minTemp","maxDew","meanDew",
              "minDew","maxHum","meanHum","minHum","maxSea","meanSea",
              "minSea","maxVisi","meanVisi","minVisi","maxWind","meanWind",
              "maxGust","precip","cloudCover","events","windDir"]


#print(data.meanTemp.head())
#print(data.meanTemp.std())
#print(data.columns)
#data.meanTemp.hist()
#plt.show()
#print(data.EDT.head())
#first_date=data.EDT.values[0]
#print(first_date)
#fD=datetime.strptime(first_date,"%Y-%m-%d")
#data.EDT=data.EDT.apply(lambda d: datetime.strptime(d,"%Y-%m-%d"))
#empty= data.apply(lambda col: pandas.isnull(col))
#data.dropna(subset=["events"])


#print(data.EDT.head())
#print(empty.events.head())

plt.xlabel("Day")
plt.ylabel("Temp in Farenheit")
plt.title("Day vs Temp")

plt.plot(data.minTemp, color="pink")
plt.plot(data.meanTemp, color="purple")
plt.plot(data.maxTemp, color="aqua")
plt.grid(True)
plt.show()
