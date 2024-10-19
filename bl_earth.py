#
#   Script to run bl_earth in batch mode
#
#    Example:
#      blender --background --python bl_earth.py -noaudio -E 'CYCLES' -f 1 -F 'PNG' -- data.grib
#

#
#  First set path to find bl_earth in the addon folder 
#
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__),'addons'))

print("Python:  ", sys.executable)
print("  path:  ", sys.path)

#
#  Now we can import module
#
import bl_earth

bl_earth.run(sys.argv[-1])
