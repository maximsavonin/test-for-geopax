import requests
import json

BASE_URL = "https://nspd.gov.ru"
SEARCH_ENDPOINT = "/api/geoportal/v2/search/geoportal"

params={
    "query": "66:41:0401035",#"66:41:0505001:497",
    "thematicSearchId": 1,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
}

response = requests.get(
    url=BASE_URL + SEARCH_ENDPOINT,
    params=params,
    headers=headers,
    verify=False
)

if response.status_code == 200:
    output_file = "nspd_result.geojson"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
