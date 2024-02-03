import tempfile
from gtts import gTTS
from moviepy.editor import *
import math

def words_to_subclip(string):
    #Text to Speech input string
    speech = gTTS(string)
    temp_file = tempfile.NamedTemporaryFile()
    #speech.save(tempFilePath)
    speech.save(temp_file.name)
    audio_clip = AudioFileClip(temp_file.name)
    txt_clip = TextClip(string, color='white', method='caption', align='center')
    txt_clip = txt_clip.set_duration(audio_clip.duration)
    txt_clip = txt_clip.set_audio(audio_clip)
    return txt_clip

def script_to_subclips(video_filename, bg_video_path, script_filename, words_per_screen):
    with open(script_filename, 'r') as f:
        script = f.read()
    words = script.split()
    chunks = [' '.join(words[chunk_index*words_per_screen:chunk_index*words_per_screen+words_per_screen])
              for chunk_index in
                range(math.ceil(len(words)/float(words_per_screen)))]
    video = concatenate_videoclips([words_to_subclip(chunk) for chunk in
                                   chunks], method='compose')
    bg_video = VideoFileClip(bg_video_path).subclip(0, video.duration)
    video = CompositeVideoClip([bg_video, video])
    video.write_videofile(video_filename, fps=24)

