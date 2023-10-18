import base64
import os

import requests
from dotenv import load_dotenv

load_dotenv()  # これが .env ファイルから環境変数を読み込む役割を果たします。


def text_to_speech(text, output_filename, api_key):
    url = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + api_key

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": "en-US",
            "ssmlGender": "NEUTRAL"
        },
        "audioConfig": {
            "audioEncoding": "MP3"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    audio_content = response.json().get("audioContent")
    audio_data = base64.b64decode(audio_content)
    with open(output_filename, "wb") as out:
        out.write(audio_data)
        print(f"Audio content written to file {output_filename}")


if __name__ == "__main__":
    API_KEY = os.environ.get('GOOGLE_TEXT_TO_SPEECH_API_KEY')
    sample_text = "Hello, this is a Text-to-Speech API test."
    text_to_speech(sample_text, "sample_output.mp3", API_KEY)

    # output_filename = 'sample_output.mp3'
    # with open(output_filename, "rb") as f:
    #     print(f.read(10))  # 最初の10バイトを表示
