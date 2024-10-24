import pandas as pd

# Survey data (rows: participants, columns: questions)
data = {
    'Q1': [5, 3, 4, None, 5],
    'Q2': [None, 4, 3, 2, None],
    'Q3': [2, 3, None, 4, 4],
    'Q4': [5, None, 3, 4, None]
}

df = pd.DataFrame(data)

average_score = df.mean(axis=0)

# print(average_score)


