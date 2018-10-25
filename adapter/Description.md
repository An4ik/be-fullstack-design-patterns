## Theory

### What is Adapter Design Pattern?

The **Adapter Design Pattern** helps to convert the interface of a class into another interface that the client expects. For example, an electric kettle with square-pinned plug (client) expects to have a square-pin socket. But the wall-socket (our existing class) has round pins. The pin converter (adapter) comes to the rescue.

#### Why the need for it: Problem Statement
The Adapter Pattern is needed when the interface of an existing class needs to be morphed into one that the client wants

#### Terminology
**Adaptee**: The existing class whose interface needs to be morphed.

**Adapter**: The class in charge of morphing the interface of the adaptee to cater to client's needs.

**Client**: The class who wishes that wants to change the interface of an existing class to suit its own needs.


## Explanation of Adapter Design Pattern Example

You have **MediaFile** class, that has file with its name and extension. You want to play this media file by player.
There are 2 kind of players:
+ **MediaPlayer** (Have only play() method)
+ **AdvancedMediaPlayer** (Have play_mp4() and play_vlc() methods)

Advanced Media Player can be in two forms:
+ **MP4Player** (Can play only files in .mp4 format)
+ **VLCPlayer**    (Can play only files in .vlc format)


There is also **UniversalPlayer**, which is *MediaPlayer* player type, and that now can only play files in .mp3 format.
You want to play also .mp4 and .vlc files by UniversalPlayer. To solve this problem, you decided to implement **MediaAdapter** class, which can in some way play these video files, and attach it to your UniversalPlayer.


## Instruction

1. Open **adapter.py** file.
2. You see that there are classes, that already created, but methods are not implemented.
3. Then, look at the file **tests/test_adapter.py**.
4. Run these tests:
+ Open terminal
+ Run command:
```python
python3 -m unittest tests/test_adapter.py'```
You will see that there are 19 tests, and at first you have (failures=4, errors=13)
5. To pass all tests, complete functions, which are written in **adapter.py** file.
6. You should complete one function at a time, then be sure that you have less failures
or/and erros left. Commit and push your changes.
7. Finally, you have to be sure that no test is failed and all of them are passed.
8. Compare your answers with already written answer in **answers/adapter.py**.
9. Commit and push last modified file to server.

