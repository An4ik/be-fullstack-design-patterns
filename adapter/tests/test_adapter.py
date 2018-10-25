from unittest import TestCase

from adapter import *

class AdapterTest(TestCase):

	"""
		Testing MediaFile class
	"""
	def test_MediaFile_file_name(self):
		file = MediaFile("Cкриптонит - Мультибрендовый.wav")
		self.assertEqual(file._file_name, "Cкриптонит - Мультибрендовый")

	def test_MediaFile_file_extension(self):
		file = MediaFile("Cкриптонит - Мультибрендовый.wav")
		self.assertEqual(file._file_extension, "wav")

	"""
		Testing MediaPlayer class
	"""

	def test_MP_file_attached(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp4")
		player = MediaPlayer(file)
		self.assertEqual(player._playing_file,file)

	def test_MP_play_func_is_not_implemented(self):
		file = MediaFile("Cкриптонит - Мультибрендовый.wav")
		player = MediaPlayer(file)
		self.assertRaises(NotImplementedError, player.play)

	"""
		Testing AdvancedMediaPlayer class
	"""

	def test_AMP_file_attached(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp4")
		player = MP4Player(file)
		self.assertEqual(player._playing_file,file)

	def test_AMP_play_vlc_func_is_not_implemented(self):
		file = MediaFile("Cкриптонит - Мультибрендовый.wav")
		player = AdvancedMediaPlayer(file)
		self.assertRaises(NotImplementedError, player.play_vlc)

	def test_AMP_play_mp4_func_is_not_implemented(self):
		file = MediaFile("Cкриптонит - Мультибрендовый.wav")
		player = AdvancedMediaPlayer(file)
		self.assertRaises(NotImplementedError, player.play_mp4)

	"""
		Testing MP4Player class
	"""

	def test_MP4P_play_mp4_convenient_extension(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp4")		
		player= MP4Player(file)
		self.assertEqual("Playing "+player._playing_file._file_name+"."
			+player._playing_file._file_extension, player.play_mp4())

	def test_MP4P_play_mp4_other_extensions(self):
		file = MediaFile("Bruno Mars - Uptown Funk.avi")		
		player = MP4Player(file)
		self.assertRaises(Exception, player.play_mp4())

	"""
		Testing VLCPlayer class
	"""

	def test_VLCP_play_vlc_convenient_extension(self):
		file = MediaFile("Bruno Mars - Uptown Funk.vlc")		
		player= VLCPlayer(file)
		self.assertEqual("Playing "+player._playing_file._file_name+"."
			+player._playing_file._file_extension, player.play_vlc())

	def test_VLCP_play_vlc_other_extensions(self):
		file = MediaFile("Bruno Mars - Uptown Funk.avi")		
		player= VLCPlayer(file)
		self.assertRaises(Exception, player.play_vlc())

	"""
		Testing MediaAdapter class
	"""

	def test_MediaAdapter_has_AMP(self):
		file = MediaFile("Bruno Mars - Uptown Funk.vlc")		
		adapter = MediaAdapter(file)
		self.assertEqual(adapter._advancedMediaPlayer, None)

	def test_MediaAdapter_play_vlc_file(self):
		file = MediaFile("Bruno Mars - Uptown Funk.vlc")		
		adapter = MediaAdapter(file)
		self.assertEqual("Playing "+adapter._playing_file._file_name+"."
			+adapter._playing_file._file_extension, adapter.play())

	def test_MediaAdapter_play_mp4_file(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp4")		
		adapter = MediaAdapter(file)
		self.assertEqual("Playing "+adapter._playing_file._file_name+"."
			+adapter._playing_file._file_extension, adapter.play())

	"""
		Testing UniversalPlayer class
	"""

	def test_UP_has_MediaAdapter(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp3")		
		player = UniversalPlayer(file)
		self.assertEqual(player._mediaAdapter, None)

	def test_UP_play_mp3_file(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp3")		
		player = UniversalPlayer(file)
		self.assertEqual("Playing "+player._playing_file._file_name+"."
			+player._playing_file._file_extension, player.play())

	def test_UP_play_mp4_file(self):
		file = MediaFile("Bruno Mars - Uptown Funk.mp4")		
		player = UniversalPlayer(file)
		self.assertEqual("Playing "+player._playing_file._file_name+"."
			+player._playing_file._file_extension, player.play())

	def test_UP_play_vlc_file(self):
		file = MediaFile("Bruno Mars - Uptown Funk.vlc")		
		player = UniversalPlayer(file)
		self.assertEqual("Playing "+player._playing_file._file_name+"."
			+player._playing_file._file_extension, player.play())

	def test_UP_play_other_extension(self):
		file = MediaFile("Bruno Mars - Uptown Funk.wav")		
		player = UniversalPlayer(file)
		self.assertRaises(NotImplementedError, player.play)