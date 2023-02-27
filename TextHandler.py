import moviepy.editor as mp


def video(audio=None):
    clip = mp.VideoFileClip("BackgroundVideos/scaryBGTrim.mp4")
    txt_clip = mp.TextClip("GeeksforGeeks", fontsize=75, color='white')
    txt = mp.TextClip("GoodGeeks ", fontsize=75, color='white')
    txt_clip = txt_clip.set_pos('center').set_duration(0, 10)
    txt_clip2 = txt.set_pos('left').set_duration(10, 30)
    final_clip = mp.CompositeVideoClip([clip, txt_clip])
    final_clip.write_videofile("NewVideos/my_new_video.mp4")
    final_clip.close()