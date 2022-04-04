from PIL import Image

gif = Image.open("input.gif")
print("Number of frames: " + str(gif.n_frames))
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"frames/frame{i}.png")