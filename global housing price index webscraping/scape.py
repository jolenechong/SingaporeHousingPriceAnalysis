from bs4 import BeautifulSoup
import requests
import pandas as pd

for i in range(2009,2022):
    url = f'https://www.numbeo.com/property-investment/rankings.jsp?title={i}'
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")
    table = doc.find("table",{"id":"t2"})
    print("\n TABLE", i)

    df_table = pd.read_html(str(table),encoding="UTF-8")[0]

    df_table = df_table.drop(["Rank"], axis=1)

    # print(df_table)
    print(df_table.info())
    # df_table.to_csv(f"PropertyPriceIndexByCity_{i}.csv")
    print(i,'done')