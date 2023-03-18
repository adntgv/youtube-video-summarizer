from youtube_transcript_api import YouTubeTranscriptApi


class Transcriber():
    async def youtube_transcribe(self, id):
        srt = [] 
        srt = YouTubeTranscriptApi.get_transcript(
            id, languages=['en', 'ru']) 
        
        res = ""
        for item in srt:
            res += f"{item['text']} "
        return res


class MockTranscriber():
    async def youtube_transcribe(self, id):
        return "Hello world"
