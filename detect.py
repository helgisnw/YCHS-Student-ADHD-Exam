import requests

def get_spreadsheet_updates():
    # 구글 API를 사용해서 구글 스프레드시트의 이벤트를 구독합니다.
    url = "https://sheets.googleapis.com/v4/spreadsheets/1Ec9jRzYUGrMQifrFWNxIRvB2xACrO8E0i9pdzC3Ik20/events"
    headers = {
        "Authorization": "Bearer ",
    }
    while True:
        response = requests.get(url, headers=headers)

        # 이벤트가 발생하면 이벤트 정보를 내 서버로 전송합니다.
        if response.status_code == 200:
            events = response.json()["events"]
            for event in events:
                print(events)
                if event["type"] == "UPDATE":
                    print("UPDATED!")

if __name__ == "__main__":
    get_spreadsheet_updates()
