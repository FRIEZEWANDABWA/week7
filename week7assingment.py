import pandas as pd

# Load dataset
file_path = 'path_to_your_dataset.csv'  # Replace with your actual file path
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully")
except FileNotFoundError:
    print("File not found, please check the file path")

# Display the first few rows
df.head()


# Check data types and missing values
df.info()

# Check for missing values
missing_values = df.isnull().sum()
print(missing_values)


# Compute basic statistics
df.describe()


# Example: Grouping by species and calculating the mean of numerical columns
grouped_data = df.groupby('species').mean()
print(grouped_data)


# Example: Line chart showing sales trend over time
# Assuming the dataset has 'Date' and 'Sales' columns
df['Date'] = pd.to_datetime(df['Date'])  # Ensure the 'Date' column is in datetime format
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='o', color='b', label='Sales Trend')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()


# Example: Bar chart for average petal length by species
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()


# Example: Scatter plot of sepal length vs petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species', palette='Set1')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()
