import pandas as pd

# 讀取 pd.read_json()
# json_reader = pd.read_json("./taipei_cafes.json")
# print(json_reader)

# 利用pandas將dataframe寫入JSON
# my_coffee = {
#     "name":["cafeA","cafeB","cafeC"],
#     "address":["AddressA","AddressB","AddressC"],
#     "wifi":[4,5,6],
#     "seats":[10,34,30]
# }
# df = pd.DataFrame(my_coffee)

# df.to_json( "my_coffee.json", orient="records", force_ascii=False, indent=4)
# print("資料成功儲存")

# 利用pandas將兩個JSON的資料做合併
# mycoffee_df = pd.read_json("my_coffee.json")
# taipeicoffee_df = pd.read_json("taipei_cafes.json")

# concate_df = pd.concat([taipeicoffee_df,mycoffee_df], ignore_index=True)
# concate_df.to_json("combined_cofes.json", orient="records", force_ascii=False, indent=4)
# print("資料成功儲存")

# 利用pandas對json資料做挑選，並將挑選到的資料做刪除
combine_df = pd.read_json("./combined_cofes.json")
combine_df = combine_df[combine_df["name"]!="cafeA"]
combine_df.loc[combine_df["name"]=="cafeB","address"]="BBB"
combine_df.to_json("combined_cafes.json", orient="records",force_ascii=False,indent=4)
print("修改完成")