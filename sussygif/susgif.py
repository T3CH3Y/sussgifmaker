#⠀⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌
#⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌
#⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⢐⠑⡌
#⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪
#⣬⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡
#⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐
#⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔
#⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘
#⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎
#⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗
#⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷
#⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟
#⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰
#⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊
#⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌
#⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁
#⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀
#⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀
#⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟
#⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾
#⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽
# Modded by Ben Zimmerman
from PIL import Image
import numpy as np
import subprocess
import os

output_width = 40  # Width of output gif, measured in sussy crewmates
twerk_frame_count = 6  # 0.png to 5.png

def get_avg_fps(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration += PIL_Image_object.info['duration']
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            return frames / duration * 1000
    return None

# Load twerk frames 🥵
twerk_frames = []
twerk_frames_data = []  # Image as numpy array, pre-calculated for performance
for i in range(6):
    try:
        img = Image.open(f"C:/Python_Projects/susifier/twerk_imgs/{i}.png").convert("RGBA")
    except Exception as e:
        print(f"Error loading twerk frames! Filename = {i}.png")
        print("Probably you renamed the twerk_imgs folder or forgot to set twerk_frame_count. baka")
        print(e)
        exit()
    twerk_frames.append(img)
    twerk_frames_data.append(np.array(img))

# Get dimensions of first twerk frame. Assume all frames have same dimensions
twerk_width, twerk_height = twerk_frames[0].size

# Get gif to sussify!
gif = Image.open("input.gif")
gifFPS = str(get_avg_fps(gif))
print(f"gif FPS: {gifFPS}")
print("Number of frames: " + str(gif.n_frames))
frame_number = 0
for i in range(gif.n_frames):
    gif.seek(i)
    gif.save(f"unprocessedframes/frame{i}.png")
    frame = Image.open(f"unprocessedframes/frame{i}.png").convert("RGB")

    input_width, input_height = frame.size

    # Height of output gif (in crewmates)
    output_height = int(output_width * (input_height / input_width) * (twerk_width / twerk_height))

    # Width, height of output in pixels
    output_px = (int(output_width * twerk_width), int(output_height * twerk_height))

    # Scale image to number of crewmates, so each crewmate gets one color
    frame_scaled = frame.resize((output_width, output_height))
    print("Sussying frame #", i)

    # Create blank canvas
    background = Image.new(mode="RGBA", size=output_px)
    for y in range(output_height):
        for x in range(output_width):
            r, g, b = frame_scaled.getpixel((x, y))

            # Grab that twerk data we calculated earlier
            # (x - y + frame_number) is the animation frame index,
            # we use the position and frame number as offsets to produce the wave-like effect
            sussified_frame_data = np.copy(twerk_frames_data[(x - y + frame_number) % len(twerk_frames)])
            red, green, blue, alpha = sussified_frame_data.T
            # Replace all pixels with colour (214,224,240) with the input image colour at that location
            color_1 = (red == 214) & (green == 224) & (blue == 240)
            sussified_frame_data[..., :-1][color_1.T] = (r, g, b)  # thx stackoverflow
            # Repeat with colour (131,148,191) but use two thirds of the input image colour to get a darker colour
            color_2 = (red == 131) & (green == 148) & (blue == 191)
            sussified_frame_data[..., :-1][color_2.T] = (int(r*2/3), int(g*2/3), int(b*2/3))

            # Convert sussy frame data back to sussy frame
            sussified_frame = Image.fromarray(sussified_frame_data)

            # Slap said frame onto the background 
            background.paste(sussified_frame, (x * twerk_width, y * twerk_height))
    background.save(f"processedframes/sussified_{i}.png")
    if (frame_number == 5):
        frame_number = 0
    else:
        frame_number += 1

print("Converting sussy frames to sussy gif")
# Convert sussied frames to gif. PIL has a built-in method to save gifs but
# it has dithering which looks sus, so we use ffmpeg with dither=none
print()
subprocess.call(f'ffmpeg -f image2 -i processedframes/sussified_%d.png -filter_complex "[0:v] scale=sws_dither=none:,split [a][b];[a] palettegen=max_colors=255:stats_mode=single [p];[b][p] paletteuse=dither=none" -r {gifFPS} -y -hide_banner -loglevel error sussified.gif')

# Remove temp files
print("Ejecting temp files from folder")
for i in range(gif.n_frames):
    os.remove(f"unprocessedframes/frame{i}.png")
    os.remove(f"processedframes/sussified_{i}.png")
