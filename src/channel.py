import json
import os

from googleapiclient.discovery import build

import isodate

api_key = os.getenv("YT_API_KEY")

youtube = build("youtube", 'v3', developerKey=api_key)

# channel_id = 'UCWAG9jHxDDCoLjDzr7FS1iA'  #Настольный Сюрр
# channel = youtube.channels().list(id=channel_id, part='snippet, statistics').execute()
# print(channel)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
