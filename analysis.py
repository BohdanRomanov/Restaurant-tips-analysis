import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("tips.csv")

# Create new metric
df["tip_percent"] = df["tip"] / df["total_bill"] * 100

# Data overview
print(df.head())
print(df.info())

# Main metrics
print("Average bill:", round(df["total_bill"].mean(), 2))
print("Maximum bill:", round(df["total_bill"].max(), 2))

print("\nAverage bill by day:")
print(df.groupby("day")["total_bill"].mean().round(2))

print("\nAverage bill by smoker status:")
print(df.groupby("smoker")["total_bill"].mean().round(2))

print("\nAverage bill by time:")
print(df.groupby("time")["total_bill"].mean().round(2))

print("\nAverage tip percentage:")
print(round(df["tip_percent"].mean(), 2))

print("\nTip percentage by day:")
print(df.groupby("day")["tip_percent"].mean().round(2))

print("\nTip percentage by smoker status:")
print(df.groupby("smoker")["tip_percent"].mean().round(2))

print("\nAverage bill by gender:")
print(df.groupby("sex")["total_bill"].mean().round(2))

print("\nTip percentage by gender:")
print(df.groupby("sex")["tip_percent"].mean().round(2))

# Charts
plt.figure()
sns.barplot(x="day", y="total_bill", data=df)
plt.title("Average Bill by Day")
plt.savefig("chart.png")

plt.figure()
sns.barplot(x="smoker", y="total_bill", data=df)
plt.title("Average Bill: Smokers vs Non-Smokers")
plt.savefig("chart_smoker.png")

plt.figure()
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.title("Total Bill vs Tip")
plt.savefig("chart_scatter.png")

plt.figure()
sns.barplot(x="day", y="tip_percent", data=df)
plt.title("Tip Percentage by Day")
plt.savefig("chart_tip_percent.png")

plt.figure()
sns.barplot(x="sex", y="tip_percent", data=df)
plt.title("Tip Percentage by Gender")
plt.savefig("chart_gender_tip.png")

# Insights
print("\nINSIGHTS:")
print("- Average bill is higher on weekends")
print("- Smokers tend to spend slightly more")
print("- Tips increase with total bill amount")
print("- Tip percentage is lowest on Saturday")
print("- Females tip a higher percentage than males")