import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s

df=pd.read_csv("Iris.csv")
print(df)

#box plot
s.boxplot(df['SepalLengthCm'],color='black')
plt.title("Boxplot of species")
plt.xlabel("sepallength in cm")
plt.legend()
plt.show()

#bargraph
species_counts=df['species'].value_counts()
plt.bar(species_counts.index,species_counts.values)
plt.title("species vs count")
plt.xlabel("species")
plt.ylabel("Counts")
plt.show()

#scatter plot

species=df['species'].unique()
for sp in species:
    subset= df[df['species']==sp]
    plt.scatter(subset['SepalLengthCm'],subset['SepalWidthCm'])
plt.title('SepalLength vs SepalWidth')
plt.xlabel('SepalLength')
plt.ylabel('SepalWidth')
plt.legend()
plt.show()

#piechart
species_counts=df['species'].value_counts()
plt.pie(species_counts.values, labels=species_counts.index)
plt.title("Piechart for species_count")
plt.legend()
plt.show()