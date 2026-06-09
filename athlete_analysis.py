import pandas as pd
import matplotlib.pyplot as plt

# Load data
athletes = pd.read_csv("data/athlete_events.csv")

# Top 10 sports by participation
top_sports = athletes['Sport'].value_counts().head(10)

# Plot
plt.figure(figsize=(10,5))
top_sports.plot(kind='bar')

plt.title("Top 10 Most Popular Sports")
plt.xlabel("Sport")
plt.ylabel("Number of Athlete Entries")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("graph5_popular_sports.png")

plt.show()
