from math import remainder
from click import command
from speech_recognition_engine import SpeechTextEngine
import config
from notion import NotionClient
from datetime import datetime
import time

notion_integration_token = config.NOTION_INTEGRATION_TOKEN
notion_database_id = config.NOTION_DATABASE_ID

sr = SpeechTextEngine()
notionClient = NotionClient(token=notion_integration_token,
                            database_id=notion_database_id)

if __name__ == "__main__":

    remainder = 5
    count = 0
    while True:
        count = 0
        if sr.wakeup():
            sr.speak("listening sir....")
            time.sleep(0.5)
            while True:
                if count == remainder:
                    sr.speak("you didn't said anything for a while sir")
                    time.sleep(0.5)

                command = sr.speech_recognition()
                if "deactivate" in command:
                    print("Deactivate!")
                    sr.speak("Deactivating")
                    break

                if "note" in command or "todo" in command:
                    sr.speak("Tell me sir")
                    note = sr.speech_recognition()

                    if note == "":
                        sr.speak("you didn't said anything")
                        continue
                    else:
                        sr.speak('your todo is ' + note)
                        sr.speak(" should i store?")

                        command = sr.speech_recognition()
                        if "no" in command:
                            sr.speak("Ok sir")

                    time_now = datetime.now().astimezone().isoformat()
                    status = "Active"

                    res = notionClient.create_page(desc=note,
                                                   date=time_now,
                                                   status=status)
                    if res.status_code == 200:
                        print("created successfully....!!!")
                        sr.speak("new note created")
                    else:
                        print(f"error :-> status code = {res.status_code}")
                        sr.speak("can't store the note")

                if "exit" in command:
                    sr.speak("program terminating")
                    exit()