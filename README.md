# Manupulating

[pynput](https://pypi.org/project/pynput/) is used for GUI.

`pynput Easy` function comes from [pynput-Easy-Key-and-Mouse-Usage-Function](https://github.com/inceabdullah/pynput-Easy-Key-and-Mouse-Usage-Function).

[ls](ls.py) function is given from [Ati_News_Algo_on_Docker_Quart_Flask_Controled](https://github.com/inceabdullah/Haber-Tellali-3th-Wave-News-Service/blob/master/aws-fargate-docker-container/flask%2B/Ati_News_Algo_on_Docker_Quart_Flask_Controled/quart_flask/app.py) but slightly changed added `path`

`vars` file has `sh` variables like $DISPLAY 

# Packages

nedded to use, `python-xlib` for `python3`, so: `apt-get install python3-xlib`

# What to do

This py file opens `Gimp` GUI app on the `DESKTOP` (`X Window`)

also opens `inkscape` then, `blender`.

**in Gimp** converts image to grey scaled then, scales and saves. 

**in inkscape** `png image` converted by `gimp` is traced then saved as `svg file`.

**in blender** `svg file` is imported to `blender` then, exluded and exported as `.stl file`.




# in Docker


`debian_9_desktop_inkscape_gimp_blender` is used to convert from any picture file to `svg` file.

Docker repository name is `/hacikoder` on `Docker Hub`.