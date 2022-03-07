# Terraria fishing bot
Automated tedious fishing in terraria with Python using PIL

## What is fishing in terraria

Fishing is an activity accomplished by using a Fishing Pole at a body of liquid (water, honey, or lava) while having bait in the player's inventory. While near the body of liquid, pressing the left mouse button at a point over the liquid will cast a line into the liquid. Pressing the button again when the bobber moves up and down will reel in the line and often an item will come up with the line.

![Terraria screenshot](https://github.com/freedie666/Terraria_fishing/blob/master/images/Screen.png?raw=true)

## How it can be automated

### Detection of fishing line 

We need to take screenshots of gameplay and detect movement of the fishing line. Also there is no need for whole screenshot, so big chunk can be cropped.


<p align="center">
  <img src="https://github.com/freedie666/Terraria_fishing/blob/master/images/Screen_cropped.jpg" />
</p>

Next step is to extract fishing line from the image. We have to know RGB value of the fishing line, in this case values are int the table below.

<div align="center">
<table>
<thead>
<tr>
<th>Color</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Red</td>
<td align="right">249</td>
</tr>
<tr>
<td>Green</td>
<td align="right">86</td>
</tr>
<tr>
<td>Blue</td>
<td align="right">56</td>
</tr>
</tbody>
</table>
</div>


Now we can simply separate pixels with this value from pixels with other RGB values. There is also some buffer in RGB range providing room for color differences. (For example buffer with size of 10 will include pixels that have Green value of 86 +- 10. Same goes for Red and Blue)

Pixels that are in desired range are set to white (255,255,255) others are set to black (0,0,0).

<p align="center">
  <img src="https://github.com/freedie666/Terraria_fishing/blob/master/images/Screen_black_n_white.jpg" />
</p>

### Catching fish

Catching fish means detecting fishing line movement and pressing LMB. It can be done by repeatedly taking screenshots and comparing subsequent frames. Comparing means taking absolute value of the pixel-by-pixel difference between the two images and then looking at average value of all pixels in image that is result of this process.

| ![detection-false](https://github.com/freedie666/Terraria_fishing/blob/master/images/detection-false.jpg?raw=true)  | ![detection-true](https://github.com/freedie666/Terraria_fishing/blob/master/images/detection-true.jpg?raw=true) | 
|:---:|:---:|
|Fishing line did not move|Fishing line moved|

Now we can take look at average pixel value in each image.

<div align="center">
  
| Left image    | Right image   | 
| :-----------: | :-------------:| 
| 0.0121        | 0.4445 | 
  
</div>

In order to detect movement of fishing line we can take number that is somewhere in this interval and gives room for some errors. In this case was chosen 0.3. When its detected program presses LMB -> catches fish -> throws line again with LMB and whole process can repeat itself. Happy fishing!!!

