from flask import Flask, request, jsonify
import os

app = Flask(__name__) 
@app.route('/')
def home():
    return "OK"

@app.route('/process', methods=['POST'])
def process():
    return {"result": "url"} 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)

    # 1. 영상 다운로드 (오디오만)
    subprocess.run(["yt-dlp", "-x", "--audio-format", "mp3", "-o", "audio.mp3", url])

    # 2. Whisper (음성 → 텍스트)
    with open("audio.mp3", "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_file
        )

    text = transcript["text"]

    # 3. GPT 처리
    prompt = f"""
    아래 인터뷰를 분석해서:

    1. 한국어 번역
    2. 중요 타임라인 (00:00~00:00)
    3. 유튜브용 대본 (1분)

    내용:
    {text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "result": response['choices'][0]['message']['content']
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
