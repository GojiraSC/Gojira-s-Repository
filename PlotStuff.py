import pandas as pd

column = ["Mariya", "Batman", "Spongebob"]
titled_columns = {"name": column,
                 "height": [1.67, 1.9, 0.25],
                 "weight": [54, 100, 1]}
data = pd.DataFrame(titled_columns)
select_column = data["weight"]
print(select_column)
