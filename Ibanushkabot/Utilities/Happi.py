import requests

class HappiServices():

    def __init__(self):
        self.API_KEY='API-KEY-Happi.dev'
        self.headers={'x-happi-key':self.API_KEY}
        self.url_location='https://api.happi.dev/v1/geoip/'
        self.url_song='https://api.happi.dev/v1/music'

    def my_location(self):
        response=requests.get(self.url_location,headers=self.headers)
        if response.status_code==200:
            data=response.json()
            ip=f'IP: {data["info"]["ip"]}'
            country=f'Country: {data["info"]["country"]}'
            region=f'Region: {data["info"]["region"]}'
            tiempo=f'Timezone: {data["info"]["timezone"]}'
            return f'{country}\n{region}\n{tiempo}\n{ip}'
        return None

    def location(self,ip):
        uri_location=self.url_location+ip
        response=requests.get(uri_location,headers=self.headers)
        if response.status_code==200:
            data=response.json()
            ip=f'IP: {data["info"]["ip"]}'
            country=f'Country: {data["info"]["country"]}'
            region=f'Region: {data["info"]["region"]}'
            tiempo=f'Timezone: {data["info"]["timezone"]}'
            return f'{country}\n{region}\n{tiempo}\n{ip}'
        return None

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
