import pandas as pd
import sqlite3

dbname = "main.sqlite"
conn = sqlite3.connect(dbname, isolation_level=None)

# dbをread_sqlを使用してpandasとして読み出す。
df = pd.read_sql('SELECT * FROM test', conn)
# head()はデフォルトで先頭5件取得、引数で取得する数値を入力
print(df.head())

# 作業完了したらDB接続を閉じる
conn.close()
