# PyAmbilight

##Simple ambient lighting using Philips Hue and Python
Change 1 Hue light around your TV/Monitor based on the current screenshot

*Uses [hue-python-rgb-converter] (https://github.com/benknight/hue-python-rgb-converter) from Ben Knight for converting RGB values to the XY colors needed by Hue.*

**Requires** the following libraries:
* [httplib2] (https://pypi.python.org/pypi/httplib2)
* [PIL] (https://pypi.python.org/pypi/Pillow/2.7.0)

The current implementation uses just 1 light, but this will likely change.

To use, you first need to register with the [Philips Hue API] (http://www.developers.meethue.com/) to register a new device, and need to know the following:
* Your device name
* Your bridge IP
* The ID of the light that you want to control

Change the values on lines 7-9 to your respective info:
```
setting_device = 'newdeveloper'
setting_light = '6'
setting_bridge = '192.168.1.223'
```

Run *simple_py_ambi.py* and enjoy.

Some more background info on how it works, pictures of implementation and example video available at [http://jpbrown.info/projects/view/pyambilight/] (http://jpbrown.info/projects/view/pyambilight/)
