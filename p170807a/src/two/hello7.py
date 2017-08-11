class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("Playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("Playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("Playing {} as ogg".format(self.filename))

class FlacFile:
    """
    Though FlacFile class doesn't inherit AudioFile class,
    it also has the same interface as three subclass of AudioFile.

    It is called duck typing.
    """
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename

    def play(self):
        print("Playing {} as flac".format(self.filename))

# 作者：JasonDing
# 链接：http://www.jianshu.com/p/650485b78d11
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。