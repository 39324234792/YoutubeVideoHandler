import moviepy.editor as mp
import moviepy.video.fx.all as vfx

# Create a temp video clip for this example
# temp_clip = mp.ColorClip(size=(1920, 1080), color=(0, 0, 255), duration=1)
# temp_clip.write_videofile("blue_original_clip.mp4", fps=30)

# This is where you load in your original clip
clip_16_9 = mp.VideoFileClip("BackgroundVideos/minecraftBG2.mp4")

# Now lets crop out a 9:16 section from the original
# x1=0, y1=0 will take the section from the top left corner
x, y = clip_16_9.size
clip_9_16 = vfx.crop(clip_16_9, x1=x/2-576/2, y1=0, width=576, height=1024)
clip_9_16.write_videofile("BackgroundVideos/minecraftBG3.mp4")