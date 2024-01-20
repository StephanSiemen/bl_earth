#
#   Script to run bl_earth in batch mode
#
#    Example:
#      blender --background --python bl_earth.py -noaudio -E 'CYCLES' -f 1 -F 'PNG'
#

#
#  First set path to find bl_earth in the addon folder 
#
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__),'addons'))

#
#  Now we can import module
#
import bl_earth

bl_earth.run()
