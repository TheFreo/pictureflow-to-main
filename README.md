# pictureflow-to-main

> This is not a patch for ready-made firmware! You will need to apply the patch and recompile the firmware for your player! How to compile, read ![here](https://www.rockbox.org/wiki/HowToCompile.html)

This patch adds a PictureFlow shortcut to the Rockbox main menu.

# Requirements

- git
- python

# Usage
1. Clone Rockbox repository
```shell
git clone git://git.rockbox.org/rockbox && cd rockbox
```

2. Clone patch repository
```shell
git clone https://github.com/TheFreo/pictureflow-to-main && cd pictureflow-to-main
```

3. apply the patch
```shell
python patch.py
```

4. Compile the firmware
