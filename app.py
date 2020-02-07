from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as keyboardController
mouse = Controller()
keyboard = keyboardController()

import gimp_2inkscape_exporter, inkscape_2_svg, blender_2_stl_from_svg

# ls, vars, os
import os, ls, _vars

from time import sleep





# ls one image name or the first name
oneFile = ls.ls_dir("images")["files"][0]

# open gimp with quietly 
# gimp --no-splash  --console-messages 

# remove old folders then make them
#
#   /root/bla/bla/file.png
#   split("/")[-1]
#   replace(,"")
#   + "aaaaa_scaled_images"

oneFileSplitted = oneFile.split("/")
willBeRemovedPath = oneFile.replace(oneFileSplitted[-1],"") + "aaaaa_scaled_images"

removeFoldersCmd = 'rm -rf "%s"' % (willBeRemovedPath)

os.system("""/bin/sh -c '%s' &""" % (removeFoldersCmd))

willBeCreatedPath = willBeRemovedPath = oneFile.replace(oneFileSplitted[-1],"") + "aaaaa_scaled_images/aaaaa_svg"

createFoldersCmd = 'mkdir -p "%s"' % (willBeCreatedPath)

os.system("""/bin/sh -c '%s' &""" % (createFoldersCmd))


gimpCmd = 'gimp --no-splash  --console-messages --no-data  "%s"' % oneFile 
print(gimpCmd)
os.system("""/bin/sh -c '%s' &""" % (gimpCmd))
print("""/bin/sh -c '%s'""" % (gimpCmd))

# wait then run editor
print("waiting...")
sleep(10)
print("gimp_2inkscape_exporter.doIt")
gimp_2inkscape_exporter.doIt()
print("gimp expoted")


# aaaaa_scaled_images/

oneScaledFile = ls.ls_dir("images/aaaaa_scaled_images")["files"][0]

print(oneScaledFile)

inkscapeCmd = "inkscape"
os.system("""/bin/sh -c '%s' &""" % (inkscapeCmd))
print("""/bin/sh -c '%s' &""" % (inkscapeCmd))
# wait then run...
sleep(10)
print("inkscape_2_svg.doIt")
inkscape_2_svg.doIt()
print("inkscape exported")


# svg to stl with blender

blenderCmd = "blender -noaudio"
os.system("""/bin/sh -c '%s' & """ % (blenderCmd))
print("""/bin/sh -c '%s' & """ % (blenderCmd))
# Wait then run
sleep(30)
print("blender_2_stl_from_svg.doIt")
blender_2_stl_from_svg.doIt()
print("str exported")

