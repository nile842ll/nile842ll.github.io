import pandas as pd
import matplotlib.pyplot as plt
import mpld3



df = pd.read_csv("UNdata_Export_20250403_011008399.csv")


df.columns = ["field0", "Country", "field1", "Year", "field2", "Sex", 
              "field3", "Age group", "field4", "Unit", "field5", "Value"]

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

pivotitaly = df.pivot(index="Year", columns="Sex", values="Value").sort_index()
#Thailand plot
dfthai = pd.read_csv("thailand_enrollment.csv")



dfthai.columns = ["field0", "Country", "field1", "Year", "field2", "Sex", 
              "field3", "Age group", "field4", "Unit", "field5", "Value"]

dfthai["Year"] = pd.to_numeric(dfthai["Year"], errors="coerce")
dfthai["Value"] = pd.to_numeric(dfthai["Value"], errors="coerce")

pivotthai = dfthai.pivot(index="Year", columns="Sex", values="Value").sort_index()

#creating interactive plot for extra credit
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(pivotitaly.index, pivotitaly["All genders"], label="All Genders (Italy)", color="blue")
ax.plot(pivotitaly.index, pivotitaly["Female"], label="Women (Italy)", color="pink")
ax.plot(pivotthai.index, pivotthai["All genders"], label="All Genders (Thailand)", color="teal")
ax.plot(pivotthai.index, pivotthai["Female"], label="Women (Thailand)", color="red")
ax.set_title("Enrollment in Grade 5 in Italy and Thailand by Gender (UN Data)")
ax.set_xlabel("Year")
ax.set_ylabel("Population Count")
ax.legend(title="Gender & Country")
ax.grid(True)
plt.tight_layout()
plt.savefig("italythaiplot.png")
print("SUCCESS Saved plot as italythaiplot.png")
html_str = mpld3.fig_to_html(fig)
with open("italythaiplot_interactive.html", "w") as f:
    f.write(html_str)
print("SUCCESS Saved interactive plot as italythaiplot_interactive.html")



