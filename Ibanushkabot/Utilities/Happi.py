import requests

class HappiServices():

    def __init__(self):
        self.API_KEY='Happi-Token'
        self.headers={'x-happi-key':self.API_KEY}
        self.url_location='https://api.happi.dev/v1/geoip/'
        self.url_song='https://api.happi.dev/v1/music'

    def song(self,name):
        params={'q':name,'limit':1,'type':'track'}
        response=requests.get(self.url_song,headers=self.headers,params=params)
        if response.status_code==200:
            data=response.json()
            song_name=f"Song name: {data['result'][0]['track']}"
            artist_name=f"Artist: {data['result'][0]['artist']}"
            album_name=f"Album: {data['result'][0]['album']}"
            cover=f"[🖼️]({data['result'][0]['cover']})"
            haslyrics=data['result'][0]['haslyrics']
            if haslyrics:
                url_lyrics=data['result'][0]['api_lyrics']
                lyrics_response=requests.get(url_lyrics,headers=self.headers)
                if lyrics_response.status_code==200:
                    data_lyrics=lyrics_response.json()
                    lyrics=f"lyrics:\n\n{data_lyrics['result']['lyrics']}"
            else:
                lyrics=f"lyrics:\n\n Not found"
            return f'{song_name}\n\n{album_name}\n\n{artist_name}\n\n{lyrics}\n\n{cover}'
        return None
