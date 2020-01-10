import pandas as pd
import matplotlib.pyplot as plt


wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
    
    
print(wood.head())
print(steel.head())
# load rankings data here:
def plot_rank(coaster, park, df):
  rankings = df[(df["Name"] == coaster) & (df["Park"] == park)]
  
  ax = plt.subplot()
  ax.plot(rankings["Year of Rank"],rankings["Rank"])
  ax.set_xticks(rankings["Year of Rank"])
  ax.set_yticks(rankings["Rank"])
  ax.invert_yaxis()
  plt.title("Rankings of Roller Coaster by Year")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  
  plt.show()

plot_rank("El Toro", "Six Flags Great Adventure", wood)  
  


# Plot 2 Coasters at Once
def dbl_rank(coaster1, park1, df1, coaster2, park2, df2):
  rankings1 = df1[(df1["Name"] == coaster1) & (df1["Park"] == park1)]
  rankings2 = df2[(df2["Name"] == coaster2) & (df2["Park"] == park2)]
  
  ax = plt.subplot()
  ax.plot(rankings1["Year of Rank"],rankings1["Rank"])
  ax.plot(rankings2["Year of Rank"],rankings2["Rank"])
  ax.set_xticks(rankings1["Year of Rank"])
  ax.set_yticks(rankings1["Rank"])
  ax.invert_yaxis()
  plt.title("Rankings of Roller Coaster by Year")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.legend([coaster1, coaster2], loc=1)
  plt.show()

dbl_rank("El Toro", "Six Flags Great Adventure", wood, "Boulder Dash", "Lake Compounce", wood)  
  
plt.clf()

# Show the Top n Roller Coasters on the same graph

def top_n(n, df):
    ax = plt.subplot()
    ax.invert_yaxis()
    for i in range(1,n+1):
        for y in range(2013, 2018):
            ranking = df[(df["Rank"] == i) & (df["Year of Rank"] == y)]
            ax.plot(ranking["Year of Rank"], ranking["Rank"])
    
    ax.set_xticks(ranking["Year of Rank"])
    ax.set_yticks(range(1, n+1))
    
    plt.title("Top Roller Coasters over Time")
    plt.xlabel("Year")
    plt.ylabel("Rank")
    plt.legend(df["Name"])
    plt.show

top_n(5, wood)    