※（宿題をさぼっていて時間がないため）半日で作って疲れたのと冬休み最終日テンションで、日本語がめっちゃ変です。許してください


## わっといずでぃす


これはhakko aiを使用するvscodeの拡張機能です。一応個人的には使用許可はとっていますが、まぁ自己責任でおねがいします。


仕組みとしては、vscodeの拡張機能からpyを呼んで、スクショとって、ocrして、deepseek(ローカルのプログラミング得意LLM)で抜粋&編集して、vscodeの拡張機能に投げて、ファイルに書き込んでいます。


まだ使いずらいのは分かっているので、やる気が出たら更新します。
誰かやってくれてもいいんだよ |дﾟ)ﾁﾗｯ

実際、python勉強してまだ１か月ちょいなので僕よりもうまい人が作ってください


意見・感想・質問・クレームはdiscord:r_nightcoreまで
## はうとぅーゆーず
1. リポジトリをクローンします:
    ```sh
    git clone https://github.com/rintaro-s/hakko-vscode.git
    ```

2. ディレクトリに移動します:
    ```sh
    cd hakko-vscode
    ```

3. 拡張機能をパッケージ化します:
    ```sh
    npx vsce package
    ```

4.  vscodeで拡張機能を開き、VSIXからのインストールを押し、生成されたhakko-0.0.1.vsixを選択してインストール

5. https://lmstudio.ai/ からLMstudioをインストール。

6. https://lorinta.xsrv.jp/2024/07/03/%e3%80%90lmstudio%e3%80%91local-inference-server%e6%a9%9f%e8%83%bd%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%a6%e3%80%81%e3%83%96%e3%83%a9%e3%82%a6%e3%82%b6%e3%81%a8%e3%82%b3%e3%83%b3%e3%82%bd%e3%83%bc/ などを見て、使い方をちょっと見る。

7. DeepSeekのモデルをダウンロードする。（別にLLMは何でもいい。ただDeepSeekがおすすめ。）

8. local inference serverを起動し、使える状態にする。

9. src\py\capture.pyの４８行目のapi_keyをhttps://ocr.space/ocrapi から取得して書き換える。

10. hakko aiに書いてほしいプログラムを頼む

11. 右に仮想デスクトップを作り、hakko aiのチャット画面を開いておきます。（vscodeが左になるように）

12. ライブラリをインストール
    ```sh
    pip install pyautogui time requests openai
    ```

14. VSCodeのコマンドパレット（Ctrl+Shift+P）を開き、extension.optimizeCodeコマンドを実行する。
