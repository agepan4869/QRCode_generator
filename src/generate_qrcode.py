import qrcode
from tkinter import Tk, Label, Entry, Button, Frame
from PIL import Image, ImageTk

class QRCodeApp:
    def __init__(self, master):
        '''
        QRコード生成アプリの初期化。
        input:
            master(Tk): Tkinterのルートウィンドウインスタンス
        '''
        self.master = master
        self.master.title("QR Code Generator")

        # 上部フレーム（URLラベルとテキスト入力フィールド用）
        self.top_frame = Frame(master)
        self.top_frame.pack()

        # 'URL:' ラベル
        self.url_label = Label(self.top_frame, text="URL:")
        self.url_label.pack(side="left")

        # テキスト入力フィールド
        self.text_entry = Entry(self.top_frame, width=40)
        self.text_entry.pack(side="left")
        self.text_entry.bind("<Return>", self.generate_and_display_qr_code)  # Enterキーにバインド

        # 生成ボタンフレーム
        self.button_frame = Frame(master)
        self.button_frame.pack()

        # 生成ボタン
        self.generate_button = Button(self.button_frame, text="Generate", command=self.generate_and_display_qr_code)
        self.generate_button.pack()

        # QRコード表示用ラベル（初期状態では空）
        self.qr_label = Label(master)
        self.qr_label.pack()

    def generate_qr_code(self, text):
        '''
        テキストからQRコードを生成し、Pillowイメージオブジェクトを返す。
        input:
            text(str): QRコード化するテキスト

        output:
            qr_image(Image): QRコードのPillowイメージオブジェクト
        '''
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        return qr_image

    def generate_and_display_qr_code(self, event=None):
        '''
        入力されたテキストからQRコードを生成し、GUI上に表示する。
        input:
            event: イベント情報（キーバインドから呼び出される場合に使用）
        output:
            なし
        '''
        # テキストボックスからテキストを取得
        text = self.text_entry.get()
        if text:  # テキストが空でない場合に処理
            self.qr_code_image = self.generate_qr_code(text)
            qr_image_tk = ImageTk.PhotoImage(self.qr_code_image)
            self.qr_label.config(image=qr_image_tk)
            self.qr_label.image = qr_image_tk  # 参照を保持

def main():
    root = Tk()
    app = QRCodeApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()