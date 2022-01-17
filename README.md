Color Transfer between Images
======
> This code was based on [*Ching-Yu Chia*]('https://github.com/chia56028/Color-Transfer-between-Images), who implemented of the paper [*Color Transfer between Images*](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf) by Erik Reinhard, Michael Ashikhmin, Bruce Gooch and Peter Shirley.

### Example
<p float="left">
    <img src="https://github.com/alissonpina/color_transfer/blob/main/_source/eternal_sunshine_of_spotless_mind.png?raw=true" width="250" height="170" alt="Source">
    <img src="https://github.com/alissonpina/color_transfer/blob/main/_target/minari.png?raw=true" width="250" height="170" alt="Target">
    <img src="https://github.com/alissonpina/color_transfer/blob/main/_output/eternal_sunshine_of_spotless_mind.png" width="250" height="170" alt="Output">
</p>

### Install Packages
```bash
$ pip install requirements.txt
```

### Steps
1. Save some image(s) into '_source' folder (.png, .bmp, .jpg);
2. On terminal: ```python color_transfer.py```;
3. Pick a target image on Dialog Window (there are several templates in the '_target' folder);
4. Get your image(s) into '_output' folder;

### EXE File
```bash
$ pip install pyinstaller
$ pyinstaller -F color_transfer.py
```
