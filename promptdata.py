import pandas as pd
pf_score_path = 'personal_finance/personal_transactions.csv'
df = pd.read_csv(pf_score_path)

grouped_df = df.groupby('Category')

for name, _ in grouped_df:
    print(name,end=",")

# Print up to 5 rows of each group
for name, group in grouped_df:
    print(f"Group: {name}")
    unique_rows = group.drop_duplicates('Description').head(5)
    for index, row in unique_rows.iterrows():
        print(f"Description: {row['Description']}, Amount: {row['Amount']}")
    #print(f"unique_rows.head(5)")
    print("\n")