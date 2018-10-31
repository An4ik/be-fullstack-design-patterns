"""
    The Adapter pattern provides a different interface for a class. We can
    think about it as an adapter that allows you to charge a phone
    somewhere that has outlets in a different shape. Following this idea,
    the Adapter pattern is useful to integrate classes that couldn't be
    integrated due to their incompatible interfaces.
"""

class MediaFile:
    """
        Class is used to represent ordinary media file.
    """
    def __init__(self, file):
        
        """
            :param file:
            * type: str.
            * description: file path.
            * format: file_name.file_extension (example: Hello.mp3).
            
            Initialize class with 'file' argument as MediaFile("Hello.mp4").
            Split 'file' with '.' delimeter and set delimeted variables to these attributes:
            * _file_name.
            * _file_extension.
        """
        
        pass

class MediaPlayer:
    
    """
        Class is used to represent MediaPlayer interface, which must be implemented by child classes.
        Class has abstract method play(), which have to be implemented.
    """
    
    def __init__(self, mediaFile):
        
        """
            :param mediaFile:
            * type: MediaFile.
            * description: file, attached to player.
            
            Initialize class with 'mediafile' argument as MediaPlayer(mediafile).
            Set argument to '_playing_file' attribute.
        """
        
        pass
    
    def play(self):
        
        """
            Abstract method.
            Raise NotImplementedError with message.
        """
        pass

class AdvancedMediaPlayer:
    
    """
        Class is used to represent AdvancedMediaPlayer interface, which must be implemented by child classes.
        Class has abstract methods play_vlc() and play_mp4(), which have to be implemented.
    """
    
    def __init__(self, mediaFile):
        
        """
            :param mediaFile:
            * type: MediaFile.
            * description: file, attached to player.
            
            Initialize class with 'mediafile' argument as AdvancedMediaPlayer(mediafile).
            Set argument to '_playing_file' attribute.
            
        """
        
        pass
    
    def play_vlc(self):
        
        """
            Abstract method.
            Raise NotImplementedError with message.
        """
        
        pass
    
    def play_mp4(self):
        
        """
            Abstract method.
            Raise NotImplementedError with message.
        """
        
        pass


class MP4Player(AdvancedMediaPlayer):
    
    """
        Child class, which is inherited from AdvancedMediaPlayer interface, and implements play_mp4() method.
        
    """
    
    
    def play_mp4(self):
        
        """
            rtype: String.
            return: The current playing mediafile in 'mp4' format, otherwise raise ExceptionError with message.
            return format: "Playing "+file_name+"."+file_extension.
        """
        pass

class VLCPlayer(AdvancedMediaPlayer):
    
    """
        Child class, which is inherited from AdvancedMediaPlayer interface, and implements play_vlc() method.
        
    """
    
    def play_vlc(self):
        
        """
            rtype: String.
            return: The current playing mediafile in 'vlc' format, otherwise raise ExceptionError with message.
            return format: "Playing "+file_name+"."+file_extension.
        """
        pass


class MediaAdapter(MediaPlayer):
    
    """
        Class is used to represent MediaAdapter adapter, which is inherited from MediaPlayer interface, and implements play() method.
    """
    
    def __init__(self, mediaFile):
        
        """
            :param mediaFile:
            * type: MediaFile.
            * description: file, attached to player.
            
            Initialize class with 'mediafile' argument as MediaAdapter(mediafile).
            Set argument to '_playing_file' attribute.
            Initialize '_advancedMediaPlayer' attribute and set the value as a 'None'.
            
        """
        
        pass
    
    def play(self):
        
        """
            rtype: String.
            return: 'play_vlc()' or 'play_mp4()' functions of AdvancedMediaPlayer interface.
            return format: "Playing "+file_name+"."+file_extension.
            
            Set argument to '_advancedMediaPlayer' attribute as:
            * VLCPlayer("Hello.vlc"), if format of mediafile is 'vlc', or,
            * MP4Player("Hello.mp4"), if format of mediafile is 'mp4'.
        """
        
        pass


class UniversalPlayer(MediaPlayer):
    
    """
        Class is used to represent UniversalPlayer interface, which is inherited from MediaPlayer interface, and implements play() method.
        
    """
    
    def __init__(self, mediaFile):
        
        """
            :param mediaFile:
            * type: MediaFile.
            * description: file, attached to player.
            
            Initialize class with 'mediafile' argument as UniversalPlayer(mediafile).
            Set argument to '_playing_file' attribute.
            Initialize '_mediaAdapter' attribute and set the value as a 'None'.
        """
        
        pass
    
    def play(self):
        
        """
            rtype: String.
            return: current playing mediafile in format 'mp3' or using adapter in format 'vlc' or 'mp4'.
            otherwise raise NotImplementedError with message 'Unsupported format'.
            
            Set argument to '_mediaAdapter' attribute as MediaAdapter("Hello.vlc") or as MediaAdapter("Hello.mp4"),
            if format of mediafile is 'vlc' or 'mp4' respectively.
        """
        
        pass

