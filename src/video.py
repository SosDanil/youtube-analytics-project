import json
import os

from googleapiclient.discovery import build

# Pasha_Surr_april = "L0hCB4aMjsA"
# Pasha_Surr_playlist = "PLVfgWu3FRj0urLzbVsRkazpmLmVdo0Fmw"


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.video_response = Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                id=video_id).execute()
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        self.video_url: str = f"https://youtu.be/{self.video_id}"

    def __str__(self):
        """Возвращает название видео"""
        return f"{self.video_title}"

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key = os.getenv("YT_API_KEY")
        return build("youtube", 'v3', developerKey=api_key)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


# if __name__ == '__main__':
    # test_video = Video(Pasha_Surr_antitop10)
    # test_video.printj(test_video.video_response)
    # print(test_video.video_title)
    # print(test_video.view_count)
    # print(test_video.like_count)
    # print(test_video.video_id)
    # print(test_video.video_url)
    # test_object = PLVideo(Pasha_Surr_april, Pasha_Surr_playlist)
    # print(test_object.video_title)
    # print(test_object.view_count)
    # print(test_object.like_count)
    # print(test_object.video_id)
    # print(test_object.video_url)
    # print(test_object.playlist_id)
