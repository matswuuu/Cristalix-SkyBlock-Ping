import io
import os
import time
import threading

import requests
import customtkinter


class Ping:
    def __init__(self, token, channel):
        def check(text, option):
            if text.find(option) != -1:
                return True

        def send_ping(message):
            headers = {
                "authorization": token
            }
            content = {
                "content": message
            }
            channel_id = channel
            requests.post(
                f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, data=content)

        for rootdir, dirs, files in os.walk("C:/"):
            for file in files:
                if ((file.split('.')[-1]) == 'launcher'):
                    if rootdir.find("cristalix") != -1:
                        while True:
                            with io.open(f"{rootdir}/updates/Minigames/logs/latest.log", "r+", encoding='utf-8') as f:
                                for line in f.readlines():
                                    if check(line, "Был активирован бустер Опыта"):
                                        send_ping("@everyone буст")
                                    if check(line, "До рестарта осталось 9 секунд"):
                                        send_ping("@everyone рестарт")

                                f.truncate(0)
                                time.sleep(120)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SKYBLOCK RESTART&BOOST PING by matswuuu")
        self.geometry("580x90")

        self.token_entry = customtkinter.CTkEntry(
            self, width=560, height=30, placeholder_text="Discord-токен")
        self.token_entry.place(x=10, y=10)

        self.channel_entry = customtkinter.CTkEntry(
            self, width=280, height=30, placeholder_text="ID канала")
        self.channel_entry.place(x=10, y=50)

        self.button = customtkinter.CTkButton(
            self, text="START", width=270, height=30, command=self.start)
        self.button.place(x=300, y=50)

    def start(self):
        self.button.configure(state=customtkinter.DISABLED)

        token = self.token_entry.get()
        channel = self.channel_entry.get()
        threading.Thread(target=Ping, args=(token, channel,)).start()


app = App()
app.mainloop()
