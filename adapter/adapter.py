class MediaFile:

	def __init__(self, file):

		pass

class MediaPlayer:

    def __init__(self, mediaFile):

    	pass

    def play(self):

    	pass

class AdvancedMediaPlayer:

    def __init__(self, mediaFile):

    	pass

    def play_vlc(self):

    	pass

    def play_mp4(self):

    	pass


class MP4Player(AdvancedMediaPlayer):

	def play_mp4(self):

		pass

class VLCPlayer(AdvancedMediaPlayer):

	def play_vlc(self):

		pass


class MediaAdapter(MediaPlayer):

	def __init__(self, mediaFile):

		pass		

	def play(self):

		pass
		


class UniversalPlayer(MediaPlayer):

	def __init__(self, mediaFile):

		pass

	def play(self):

		pass
