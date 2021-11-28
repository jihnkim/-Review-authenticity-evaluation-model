import pandas as pd
import numpy

# 식신 csv merge
# df_lst = []
# for i in range(1, 3):
#     df = pd.read_csv(f'siksin_info{i}.csv', sep=',', encoding='utf-8')
#     df_lst.append(df)
#
# result = pd.concat(
#     [df_lst[0], df_lst[1]])
#
# result.to_csv('siksin_info.csv', index=False)

# info merge
main_df = pd.read_csv(f'dining_info.csv', sep=',', encoding='utf-8')
main_df = main_df[['store_id',
                  'region',
                  'store_name',
                  'store_x',
                  'store_y',
                  'store_addr',
                  'store_addr_new',
                  'store_tel',
                  'open_hours',
                  'website',
                  'd_link']]

# print(main_df['website'])

def info_merge():
    naver_df = pd.read_csv(f'naver_info.csv', sep=',', encoding='utf-8')
    google_df = pd.read_csv(f'google_info.csv', sep=',', encoding='utf-8')
    siksin_df = pd.read_csv(f'siksin_info.csv', sep=',', encoding='utf-8')

    # naver df 전처리 필요
    naver_df = naver_df.dropna(subset=['store_id'])
    naver_df.reset_index(drop=True, inplace=True)

    lst = naver_df['store_id'].tolist()
    naver_lst = []
    for i in range(len(naver_df)):
        naver_lst.append(int(lst[i]))

    naver_df['store_id'] = naver_lst

    df_lst = [naver_df, google_df, siksin_df]

    n_link_lst = []
    g_link_lst = []
    s_link_lst = []
    for i in range(len(df_lst)):
        for column in df_lst[i]:
            if column == 'n_link':
                for idx, store_id in enumerate(main_df['store_id']):
                    if store_id in naver_lst:
                        n_link_lst.append(naver_df['n_link'][naver_lst.index(store_id)])
                    else:
                        n_link_lst.append('')

            elif column == 'g_link':
                for idx, store_id in enumerate(main_df['store_id']):
                    if main_df['store_id'][idx] == google_df['store_id'][idx]:
                        g_link_lst.append(google_df['g_link'][idx])

            elif column == 's_link':
                for idx, store_id in enumerate(main_df['store_id']):
                    if main_df['store_id'][idx] == siksin_df['store_id'][idx]:
                        s_link_lst.append(siksin_df['s_link'][idx])

            elif i > 1:
                continue

            # elif column == 'website':
            #     for idx, store_id in enumerate(main_df['store_id']):
            #         main_df.loc[main_df['website'] == None, 'website'] = siksin_df['website'][idx]

            elif column == 'open_hours':
                for idx, store_id in enumerate(main_df['store_id']):
                    main_df.loc[main_df['open_hours'] == '', 'open_hours'] = siksin_df['open_hours'][idx]

            elif column == 'store_tel':
                for idx, store_id in enumerate(main_df['store_id']):
                    main_df.loc[main_df['store_tel'] == '', 'store_tel'] = siksin_df['store_tel'][idx]

    main_df['website'] = siksin_df['website']
    main_df['n_link'] = n_link_lst
    main_df['g_link'] = g_link_lst
    main_df['s_link'] = s_link_lst

    return main_df



result = info_merge()
print(result)

result.to_csv('storeInfo.csv', encoding='utf-8', index=False)