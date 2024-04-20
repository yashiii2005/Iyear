import matplotlib.pyplot as plt
import seaborn as sns

# Load iris dataset from Seaborn
iris = sns.load_dataset('iris')

# A. Scatter plot of petal length vs petal width
plt.figure(figsize=(8, 6))
sns.scatterplot(x='petal_length', y='petal_width', data=iris, hue='species')
plt.title('Petal Length vs Petal Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(title='Species')
plt.show()

# B. Histograms of all four attributes
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
sns.histplot(iris['sepal_length'], bins=20, kde=True, color='skyblue')
plt.title('Sepal Length Distribution')

plt.subplot(2, 2, 2)
sns.histplot(iris['sepal_width'], bins=20, kde=True, color='salmon')
plt.title('Sepal Width Distribution')

plt.subplot(2, 2, 3)
sns.histplot(iris['petal_length'], bins=20, kde=True, color='green')
plt.title('Petal Length Distribution')

plt.subplot(2, 2, 4)
sns.histplot(iris['petal_width'], bins=20, kde=True, color='purple')
plt.title('Petal Width Distribution')

plt.tight_layout()
plt.show()

# C. Pie chart of flower type frequency
plt.figure(figsize=(6, 6))
iris['species'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'salmon', 'lightgreen'])
plt.title('Flower Type Frequency')
plt.ylabel('')
plt.show()

# D. Pair plot
sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
plt.show()