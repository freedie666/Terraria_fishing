# Terraria fishing bot
Automated tedious fishing in terraria

## What is fishing in terraria

Fishing is an activity accomplished by using a Fishing Pole at a body of liquid (water, honey, or lava) while having bait in the player's inventory. While near the body of liquid, pressing the left mouse button at a point over the liquid will cast a line into the liquid. Pressing the button again when the bobber moves up and down will reel in the line and often an item will come up with the line.

![Terraria screenshot](https://github.com/freedie666/Terraria_fishing/blob/master/images/Screen.png?raw=true)

## How it can be automated

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


Now we can simply 
