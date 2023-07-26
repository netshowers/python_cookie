from pathlib import Path

import pandas as pd


def main():
    files = Path('D:/Document/python/case 1').glob('*.xlsx')

    dfs = [
        pd.read_excel(f, engine="openpyxl")
        for f in files
    ]
    B = 'DEN'
    print({A: B for A in range(5)})

    df = pd.concat(dfs)
    # writer = pd.ExcelWriter('D:/Document/python/case 1/new_jd_goods.xlsx')
    # df.to_excel(writer)
    # writer.close()
    df.to_csv('D:/Document/python/case 1/new_jd_goods.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    main()
