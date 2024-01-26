import json
import os
import datetime

import isodate

from googleapiclient.discovery import build

# Pasha_Surr_april = "L0hCB4aMjsA"
# Pasha_Surr_playlist = "PLVfgWu3FRj0urLzbVsRkazpmLmVdo0Fmw"


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.url = f"https://www.youtube.com/playlist?list={playlist_id}"

    @property
    def total_duration(self):
        """Возвращает суммарную длительность всех видео плейлиста в виде datetime.timedelta"""

        total_duration = datetime.timedelta()  # по умолчанию все по нулям

        video_response = self.get_video_response()

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        video_response = self.get_video_response()
        max_count_likes = 0
        id_of_best_video = ''

        for video in video_response['items']:
            if int(video["statistics"]["likeCount"]) > max_count_likes:
                max_count_likes = int(video["statistics"]["likeCount"])
                id_of_best_video = video["id"]
        return f"https://youtu.be/{id_of_best_video}"

    def get_video_response(self):
        """достает список из словарей с информацией по каждому видео из плейлиста"""
        playlist_videos = self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                                      part='contentDetails', maxResults=50, ).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                              id=','.join(video_ids)).execute()
        return video_response

    @property
    def title(self):
        playlist_info = self.get_service().playlists().list(id=self.playlist_id, part="snippet").execute()
        return playlist_info['items'][0]['snippet']['title']

    @classmethod
    def get_service(cls):
        api_key = os.getenv("YT_API_KEY")
        return build("youtube", 'v3', developerKey=api_key)

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


# if __name__ == '__main__':
#     test_playlist = PlayList(Pasha_Surr_playlist)
#     print(test_playlist.show_best_video())



