import json
import os

from googleapiclient.discovery import build

channel_id_Pasha = 'UCWAG9jHxDDCoLjDzr7FS1iA'  # Настольный Сюрр


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv("YT_API_KEY")
    youtube = build("youtube", 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = self.channel["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]
        self.data = {"title": self.title, "description": self.description, "url": self.url,
                     "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                     "view_count": self.view_count}

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, name_file):
        json_data = json.dumps(self.data, ensure_ascii=False)
        with open(name_file, "w", encoding="UTF-8") as file:
            file.write(json_data)

    @classmethod
    def get_service(cls):
        return cls.youtube


if __name__ == '__main__':
    PashaSurr = Channel(channel_id_Pasha)
    PashaSurr.to_json("data_channel.json")
    print(PashaSurr.channel_id)
    print(PashaSurr.title)
    print(PashaSurr.description)
    print(PashaSurr.url)
    print(PashaSurr.subscriber_count)
    print(PashaSurr.video_count)
    print(PashaSurr.view_count)
    print(PashaSurr.youtube)
    PashaSurr.print_info()


