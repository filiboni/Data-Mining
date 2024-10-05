# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import seaborn as sns

# Load the CSV file using pandas
class DataMiner:
    def __init__(self, csv1, csv2):
        tmp1 = pd.read_csv(csv1)
        tmp2 = pd.read_csv(csv2)
        self.df = pd.merge(tmp1, tmp2, left_on='cyclist', right_on='_url', how='inner')

    def columns_names(self):
        return self.df.columns

    def delete_column(self, col):
        self.df.drop(columns=[col], inplace=True)

    def replace_NaN(self, column, value):
        self.df[column].fillna(value, inplace=True)
    # Loop through each column to get counts
    def inspect(self):
        print(f"{'Column':<30} | {'Non-null count':<15} | {'Total count':<15} | {'Missing':<15}")
        tmp = []
        for column in self.columns_names():
            non_null_count = self.df[column].count()  # Count of non-null values
            total_count = len(self.df[column])        # Total number of values
            print(f"{column:<30} | {non_null_count:<15} | {total_count:<15} | {total_count == non_null_count}")

            if total_count != non_null_count:
                tmp.append(column)

        return tmp

    def find_rows_with_alternatives(self, col1, col2):
        tmp = []
        for _, row in self.df.iterrows():
            if (row[col1] is None) ^ (row[col2] is None):
                tmp.append(row['name'])
        return tmp

    def check_are_alternatives(self, col1, col2):
        alternatives_rows = len(dm.find_rows_with_alternatives(col1, col2))
        print(f"{"YES. Columns are alternatives" if alternatives_rows == self.rows() else "NO. Columns are not alternatives"}. It's true for {alternatives_rows}/{dm.rows()} rows")

    def get_categoricals(self):
        return self.df.select_dtypes(include=['object', 'category']).columns.tolist()

    def get_numericals(self):
        return self.df.select_dtypes(include=['number']).columns.tolist()

    def plot_by_name(self):
        pass

    def rows(self):
        return len(self.df)

dm = DataMiner(r"./dataset/races.csv", r"./dataset/cyclists.csv")

categoricals_cols = dm.get_categoricals()
numericals_cols = dm.get_numericals()
print(f"Categoricals columns: {categoricals_cols}")
print(f"Numerical columns: {numericals_cols}")

missing_cols = dm.inspect()
print(f"Missing values columns: {missing_cols}")

dm.check_are_alternatives("points", "uci_points")

dm.delete_column('average_temperature')


print("END")