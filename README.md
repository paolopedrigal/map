# [San Jose District 4 Map](https://www.electdavidcohen.com/neighborhoods)

![License Static Badge](https://img.shields.io/badge/license-MIT-orange)

## Description

Small project to help me tune the coordinates of neighborhoods in District 4 of San Jose, California, United States.

## Technology used

- JavaScript
- HTML
- CSS
- Python

## Motivation

This project was used ultimately for San Jose City Councilmember David Cohen in his election website. You can check out the map live [here!](https://www.electdavidcohen.com/neighborhoods) (Full URL: https://www.electdavidcohen.com/neighborhoods)

## In the works

The bottleneck in this project was converting the geographical coordinates to pixel coordinates for the SVG polygons. The project used Python to manipulate the coordinates, but was used for one neighborhood region at a time, and _not_ all of them together.

## How the map was coded

The coordinates of each neighborhood were given to me by my client and are in the `coordinates/` folder as a text file under the naming convention `<neighborhood-name>.txt` (e.g. `alviso.txt`)

- My client used _Google My Maps_ to draw out the neighborhood areas and then the coordinates were extracted from an exported KML file.

After receiving each set of coordinates of their respective neighborhood region, I converted the set of coordinates from geographical longitude/latitude coordinates to pixel coordinates.

In order to do this, a Python script called `coordinates.py` was used for conversion. In a nut shell, this script receives 5 inputs: (1) name of the the text file containing the raw coordinates, (2) minimum pixel on the horizontal axis, (3) maximum pixel on the horizontal axis, (4) minimum pxiel on the vertical axis, (5) maximum pixel on the vertical axis. The output of the script is the rescaled set of coordinates.

For example, to rescale the coordinates of Alviso with 135 and 418 being the respective minimum and maximum pixel coordinates on the horizontal axis and with 40 and 340 being the respective minimum and maximum pixel coordinates on the vertical axis, you may the run the script below as follows:

```
$ python3 coordinates/alviso.txt 135 418 40 340
```

Finally, after converting the coordinates, HTML SVG polygon tag elements were used as the `points` attribute contained the set of coordinates.

## License

MIT License.
