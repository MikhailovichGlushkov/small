import time
from moviepy.editor import *
import PyQt5.QtWidgets as qw
#st = time.time()
def explict(video_path):
    audio_path = video_path.strip(".mp4")+".wav"
    video =VideoFileClip(video_path)
    audio =video.audio
    audio.write_audiofile(audio_path)
    qw.QMessageBox.Critical(self,"错误","请检查文件格式是否为MP4！！")
def exppath(source_path): #解析路径的函数
    str=source_path.strip("file:///")
    return str
#print("消耗时间：{}".format(time.time()-st))