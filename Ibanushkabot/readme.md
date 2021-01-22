# Welcome to ibanushkabot documentation

## Introduction

Ibanushkabot is a chat-bot located in Telegram, it's help users to find songs data, youtube videos, find any IP address location and translate phrases with audio message to hear it. No more time lost changing amongst apps when you are chatting with someone.

Test it [here!][1]

## Bot commands

### /help
Returns a menu with all available commands
#### input: 
```
/help
```
#### output:
...
* /youtube <"video name">
* /song <"song name">
* /translate <"source_language destination_language phrase">
* /help
* /example
* For more help contact the admin
...

### /example
Returns a menu with all available commands with examples
#### input: 
...
/example
...
#### output:
...
* /youtube life on mars David Bowie
* /song walk away Franz Ferdinand
* /translate english spanish Hello World
* /help
* /example
* if you need more help contact the admin
...

### /youtube <"video name">
Returns the first match on youtube search
#### input: 
/youtube Ode to the mets The Strokes
#### output:
video url [here!][3]

### /mylocation
Returns my IP address location data
#### input:
/mylocation
#### output:
* Country: US
* Region: 
* Timezone: America/Chicago
* IP: 142.250.69.46

### /location <"IP">
Returns my IP address location data
#### input:
/location 172.217.15.14
#### output:
* Country: US
* Region: 
* Timezone: America/Chicago
* IP: 172.217.15.14

### /song <"song name">
Returns song data with lyrics if it has
#### input:
/song Take me out Franz Ferdinand
#### output:
Song name: Take Me Out

Album: Franz Ferdinand

Artist: Franz Ferdinand

lyrics:

So if you're lonely
You know I'm here
Waiting for you
I'm just a crosshair
I'm just a shot away from you
And if you leave here
You leave me broken
Shattered I lie
I'm just a crosshair
I'm just a shot then we can die

I know I won't be leaving here
With you

I say don't you know
You say you don't know
I say... take me out

I say you don't show
Don't move time is slow
I say... take me out

I say you don't know
You say you don't go
I say... take me out

If I move this could die
If eyes move this could die
I want you... to take me out

I know I won't be leaving here (with you)
I know I won't be leaving here
I know I won't be leaving here (with you)
I know I won't be leaving here with you

I say don't you know?
You say you don't know
I say...take me out

If I wane, this can die
If I wane, this can die
I want you to take me out

If I move, this could die
If eyes move, this could die
Come on, take me out

I know I won't be leaving here (with you)
I know I won't be leaving here
I know I won't be leaving here (with you)
I know I won't be leaving here with you

Cover [here!][4]

### /translate <"source_language destination_language phrase">
Returns the translate phrase with an audio message to hear it
#### input:
/translate spanish english Estos es una prueba, Hola Mundo.
#### output:
This is a test, Hello World.
Audio message [here!][5]

## API-Keys

#### Happi
If you need to create your own Happi.dev API-Key just click [here!][2]

## Issues with Ibanushkabot

If you discover any issue with Ibanushkabot, please contact me. I'll help you soon!

[1]: https://t.me/Ibanushkabot
[2]: https://happi.dev
[3]: https://www.youtube.com/watch?v=BjC0KUxiMhc
[4]: https://ia800706.us.archive.org/29/items/mbid-462210cb-c90c-38f9-8fcf-1a04d7c86729/mbid-462210cb-c90c-38f9-8fcf-1a04d7c86729-4776442757_thumb500.jpg
[5]: https://translate.google.com/translate_tts?ie=UTF-8&q=This%20is%20a%20test%2C%20Hello%20World.%20&tl=en-us&client=tw-ob&idx=0
