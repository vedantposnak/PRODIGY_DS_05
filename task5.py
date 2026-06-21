import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\Task5\accident_prediction_india.csv")

print(df.head())
print(df.columns)

# Weather Analysis
plt.figure(figsize=(8,5))
sns.countplot(y='Weather Conditions', data=df,
              order=df['Weather Conditions'].value_counts().index)
plt.title("Accidents by Weather Condition")
plt.show()

# Road Type Analysis
plt.figure(figsize=(8,5))
sns.countplot(y='Road Type', data=df,
              order=df['Road Type'].value_counts().index)
plt.title("Accidents by Road Type")
plt.show()

# Top Accident Cities
top_cities = df['City Name'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_cities.values, y=top_cities.index)
plt.title("Top 10 Accident Hotspots")
plt.xlabel("Accident Count")
plt.show()

# Time Analysis
plt.figure(figsize=(8,5))
sns.countplot(x='Time of Day', data=df)
plt.title("Accidents by Time of Day")
plt.show()