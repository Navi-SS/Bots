from urllib import parse,request
import re

class YoutubeService():

    def video(self,search):
        query_string=parse.urlencode({'search_query':search})
        html_content=request.urlopen('http://www.youtube.com/results?'+query_string)
        search_results=re.findall(r"watch\?v=(\S{11})",html_content.read().decode())
        return f'[📹](https://www.youtube.com/watch?v={search_results[0]})'
