from datetime import datetime
from email import header
from http import client
import json
import requests
import config


class NotionClient:

    def __init__(self, token, database_id) -> None:
        self.token = token
        self.database_id = database_id
        self.headers = {
            'Authorization': 'Bearer ' + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def create_page(self, desc, date, status):
        url = "https://api.notion.com/v1/pages"

        data = {
            "parent": {
                "database_id": self.database_id
            },
            "properties": {
                "Description": {
                    "title": [{
                        "text": {
                            "content": desc
                        }
                    }]
                },
                "Date": {
                    "date": {
                        "start": date,
                        "end": None
                    }
                },
                "Status": {
                    "rich_text": [{
                        "text": {
                            "content": "Active"
                        }
                    }]
                }
            }
        }

        data = json.dumps(data)
        res = requests.post(url=url, data=data, headers=self.headers)
        return res


if __name__ == "__main__":
    notion_integration_token = config.NOTION_INTEGRATION_TOKEN
    notion_database_id = config.NOTION_DATABASE_ID

    client = NotionClient(token=notion_integration_token,
                          database_id=notion_database_id)
    time_now = datetime.now().astimezone().isoformat()
    status = "Active"
    res = client.create_page(desc="testing", date=time_now, status=status)
    if res.status_code == 200:
        print("created successfully....!!!")
    else:
        print(f"error :-> status code = {res.status_code}")