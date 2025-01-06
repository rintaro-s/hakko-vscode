import pyautogui
import time
import requests
from openai import OpenAI

def switch_desktop_and_capture_screenshot():
    # 右の仮想デスクトップに移動
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('right')
    time.sleep(0.1)
    pyautogui.keyUp('winleft')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('right')

    # スクリーンショットを撮影（横幅は8%~50%、縦幅は下から13%~75%の範囲）
    screen_width, screen_height = pyautogui.size()
    region = (int(screen_width * 0.08), int(screen_height * 0.25), int(screen_width * 0.42), int(screen_height * 0.62))
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screenshot.png')
    print('スクリーンショットを保存しました')

    # 元の仮想デスクトップに戻る
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('left')
    time.sleep(0.1)
    pyautogui.keyUp('winleft')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('left')

def ocr_space_api(image_path, api_key):
    url = 'https://api.ocr.space/parse/image'
    with open(image_path, 'rb') as image_file:
        payload = {
            'isOverlayRequired': False,
            'apikey': api_key,
            'language': 'eng',
        }
        files = {
            'file': image_file,
        }
        response = requests.post(url, data=payload, files=files)
        return response.json()

def ocr_and_optimize_code():
    # OCR.space APIを使用してテキストを抽出
    api_key = 'your-api-key'
    image_path = 'screenshot.png'
    result = ocr_space_api(image_path, api_key)
    text = result.get('ParsedResults', [{}])[0].get('ParsedText', '')

    # LMStudio APIクライアントを設定
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # OCRしたテキスト全体をLMStudioに投げてプログラム部分を見つけ出し、成形（最適化、補完）する
    completion = client.chat.completions.create(
        model="model-identifier",
        messages=[
            {"role": "system", "content": "Find and optimize the code from the following text. Output only the program."},
            {"role": "user", "content": text}
        ],
        temperature=0.7,
    )

    optimized_code = completion.choices[0].message.content

    # 成形されたプログラムコードを表示
    print(f"Optimized Code:\n{optimized_code}")

if __name__ == "__main__":
    switch_desktop_and_capture_screenshot()
    ocr_and_optimize_code()