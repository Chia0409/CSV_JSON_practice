import requests

# API URL
url = "https://cafenomad.tw/api/v1.2/cafes/taipei"

# 發送 GET 請求下載資料
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()  # 解析 JSON 格式的回應
    # 將資料儲存成 JSON 檔案
    with open("taipei_cafes.json", "w", encoding="utf-8") as f:
        import json
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("資料已成功下載並儲存為 taipei_cafes.json")
else:
    print(f"無法下載資料，錯誤代碼：{response.status_code}")
