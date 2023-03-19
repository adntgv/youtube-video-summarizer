# youtube-video-summarizer
Get summary of YouTube videos using captions and ChatGPT. Get summary vie API + Chrome extension or Telegram bot.

## Run Summarizer server
Folder 'summarizer' is the main service folder that is responsible for summarization.

### Set variables
```.env
OPENAI_API_KEY=xx-.....
```

You can also set telegram bot token and chat id in .env file, if you want to use telegram bot.
```.env
TELEGRAM_TOKEN=xxxxx:.....
TELEGRAM_WEBHOOK=https://[some-url].vercel.app
```

### Run
You should run it from docker compose in root folder of the project.
```sh
docker-compose up -d
```

### Get url
Then share via ngrok
```sh
ngrok http 5000
```

### Set url in chrome extension
And finally set url in chrome extension 'script.js' file
```js

const url = 'https://<your_ngrok_url>/api/summarize';
```


### Run chrome extension
Install chome extension from local folder 'chrome-extension' and run it.


## Run Telegram bot
### Set webhook
```sh
curl -F "url=https://<your_ngrok_url>/bot/telegram" https://api.telegram.org/bot<your_bot_token>/setWebhook
```

### Run
```sh 
docker-compose up -d
```

### Run Telegram bot
You can use Telegram bot to get summary of YouTube videos. Just send link to video to bot and it will reply with summary.

```
/summary https://www.youtube.com/watch?v=QH2-TGUlwu4
```

## Customize prompt
You can customize prompt for summarization in 'summarizer' folder in 'app.py' file.
```python
prompt = f"""This video is about {video_title}.
{video_description}
"""
```