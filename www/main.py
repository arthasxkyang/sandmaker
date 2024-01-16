from flask import *
from .db import *
import pygame

bp=Blueprint('main',__name__,url_prefix='/main')

@bp.route('/media/play/<filename>')
def media_play(filename):
    # 系统开始播放音乐，文件位置在media文件夹下
    # 判断结尾是否是MP3
    if filename.endswith(".mp3"):
        pygame.mixer.init()
        pygame.mixer.music.load(f"/media/{filename}")
        pygame.mixer.music.play()
        return f"正在播放{filename}"
    else:
        return "不支持的文件格式"