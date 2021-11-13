import pandas as pd

# for prepared data
def merge_files(review):
    if review == True:
        df_lst = []
        for i in range(1, 11):
            df = pd.read_csv(f'google_review_{i}_10.csv', sep=',', encoding='utf-8')
            df = df.drop(columns=['Unnamed: 0'], axis=1)
            df_lst.append(df)

        result = pd.concat(
            [df_lst[0], df_lst[1], df_lst[2], df_lst[3], df_lst[4], df_lst[5], df_lst[6], df_lst[7], df_lst[8],
             df_lst[9]])

        return result

    elif review == False:
        pass

result_df = merge_files(True)
result_df.to_csv('google_review.csv', index=False)