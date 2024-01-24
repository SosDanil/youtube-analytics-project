import json
import os

from googleapiclient.discovery import build

# channel_id_Pasha = 'UCWAG9jHxDDCoLjDzr7FS1iA'  # Настольный Сюрр


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализирует id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet, statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """складывает количество подписчиков с двух каналов"""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """вычитает количество подписчиков другого канала из основного"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        """сравнение меньше"""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """сравнение меньше или равно"""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        """сравнение больше"""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """сравнение больше или равно"""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __eq__(self, other):
        """сравнение на идентичность"""
        return int(self.subscriber_count) == int(other.subscriber_count)

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, name_file):
        data = {"title": self.title, "description": self.description, "url": self.url,
                "subscriber_count": self.subscriber_count, "video_count": self.video_count,
                "view_count": self.view_count}
        with open(name_file, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        api_key = os.getenv("YT_API_KEY")
        return build("youtube", 'v3', developerKey=api_key)


# if __name__ == '__main__':
#     PashaSurr = Channel(channel_id_Pasha)
#     PashaSurr.to_json("data_channel.json")
#     print(PashaSurr.channel_id)
#     print(PashaSurr.title)
#     print(PashaSurr.description)
#     print(PashaSurr.url)
#     print(PashaSurr.subscriber_count)
#     print(PashaSurr.video_count)
#     print(PashaSurr.view_count)
#     print(PashaSurr.get_service())
#     PashaSurr.print_info()


