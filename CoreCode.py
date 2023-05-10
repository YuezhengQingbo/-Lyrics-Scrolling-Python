import tkinter as tk
from PIL import Image, ImageTk


class LyricPlayer:
    def __init__(self, master, lyrics_file, background_file):
        self.master = master
        self.master.title("Lyric Player")
        self.master.geometry("1920x1080")
        self.master.configure(background="black")

        # Add background image
        self.bg_img = Image.open(background_file)
        self.bg_photo = ImageTk.PhotoImage(self.bg_img)
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load lyrics from file
        self.lyrics = []
        with open(lyrics_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(']')
                if len(parts) == 2:
                    time_str = parts[0].replace('[', '').strip()
                    text = parts[1].strip()
                    if text:
                        self.lyrics.append((time_str, text))

        self.current_line = 0
        self.current_time = 0

        self.lyric_label = tk.Label(self.master, text="", font=("Helvetica", 30), bg="black", fg="white", anchor="s")
        self.lyric_label.place(relx=0.5, rely=0.9, anchor="center")

        # Start the lyrics
        self.master.after(1000, self.update_lyrics)

    def update_lyrics(self):
        for i in range(len(self.lyrics)):
            time_str, text = self.lyrics[i]
            if self.current_time < self.parse_time(time_str):
                break
            self.lyric_label.configure(text=text)
            self.current_line = i
        self.current_time += 1
        self.master.after(1000, self.update_lyrics)

    @staticmethod
    def parse_time(time_str):
        parts = time_str.split(':')
        if len(parts) == 2:
            minutes = int(parts[0])
            seconds = float(parts[1])
            return minutes * 60 + seconds
        return 0


if __name__ == '__main__':
    root = tk.Tk()
    player = LyricPlayer(root, './lyrics.txt', './background.jpg')
    root.mainloop()
