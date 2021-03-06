import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
# load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# write function to plot rankings over time for 1 roller coaster here:
#print(wood.head())
#print(steel.head())
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

plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def plot_rank_two(coaster1, park1, coaster2, park2, df):
  ranking1 = df[(df["Name"] == coaster1) & (df["Park"] == park1)]
  ranking2 = df[(df["Name"] == coaster2) & (df["Park"] == park2)]
  
  ax = plt.subplot()
  ax.plot(ranking1["Year of Rank"],ranking1["Rank"])
  ax.plot(ranking2["Year of Rank"],ranking2["Rank"])
  ax.set_xticks(ranking1["Year of Rank"])
  ax.set_yticks(range(1,5))
  ax.invert_yaxis()
  plt.title("Rankings of Roller Coaster by Year")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  
  plt.show()


plot_rank_two("El Toro", "Six Flags Great Adventure", "Boulder Dash", "Lake Compounce", wood)

plt.clf()

# write function to plot top n rankings over time here:
def top_n_rankings(n, rankings_df):
  top_n_rankings = rankings_df[rankings_df['Rank'] <= n]
  
  ax = plt.subplot()
  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)   
  ax.set_xticks(rankings_df["Year of Rank"])
  ax.invert_yaxis()
  plt.title("Top N Roller Coasters")
  plt.xlabel("Year")
  plt.ylabel("Rank")
  plt.legend()
  plt.show()

top_n_rankings(5, steel)
plt.clf()


# load roller coaster data here:
coaster_df = pd.read_csv("roller_coasters.csv")
print(coaster_df.head())

# write function to plot histogram of column values here:
def coastergram(df, column):
  dfm = (coaster_df[column]).dropna()
  plt.hist(dfm, bins=20)
  plt.ylabel("Frequency")
  plt.xlabel(str(column))
  plt.title("Coaster "+ str(column) + " Distribution")
  plt.show()
  
coastergram(coaster_df, "speed")

plt.clf()

# write function to plot inversions by coaster at a park here:
def inverts(coaster_df, park_name):
  park_coasters = coaster_df[coaster_df['park'] == park_name]
  park_coasters.sort_values('num_inversions', ascending = False)
  coaster_names = park_coasters['name']
  number_inversions = park_coasters['num_inversions']
  coaster_nums = [i for i, _ in enumerate(coaster_names)] 
  
  plt.bar(coaster_nums, number_inversions)
  plt.title("Coasters and Inversions at "+ str(park_name))
  plt.xlabel("Coaster Name")
  plt.ylabel("Number of Inversions")
  plt.xticks(coaster_nums, coaster_names, rotation = 85)
  plt.show()

inverts(coaster_df, 'Six Flags Great America')
plt.clf()
    
# write function to plot pie chart of operating status here:
def status(coaster_df):
  operating = coaster_df[coaster_df['status'] == 'status.operating']
  broken = coaster_df[coaster_df['status'] == 'status.closed.definitely']
  num_op = len(operating)
  num_broken = len(broken)
  total = num_op + num_broken
  per_op = num_op/total * 100
  per_broken = num_broken/total * 100

  labels = "Operational", "Non-Operational"
  sizes = [per_op, per_broken]

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels,   autopct='%1.1f%%', shadow = True)
  ax1.axis("equal")
  plt.title("Chart of Operational Status of Coasters")
  plt.show()

status(coaster_df)
plt.clf()
  
# write function to create scatter plot of any two numeric columns here:
def scatter_coaster(coaster_df, col1, col2):
  coaster_df = coaster_df[coaster_df['height'] <= 140]
  coaster_df = coaster_df.dropna()
  coaster_df[str(col1)]
  plt.scatter(coaster_df[str(col1)], coaster_df[str(col2)])
  plt.title(str(col2) + " versus " + str(col1) + " of Roller Coasters")
  plt.xlabel(str(col1))
  plt.ylabel(str(col2))
  plt.show()

scatter_coaster(coaster_df, "speed", "length")

plt.clf()