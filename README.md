Version: 1.0.1

============
Description
============
Welcome to Legacy of a Thousand Suns Time to Next Level
(lots-ttnl-calc). The goal of the script is to help players decide how
long it will take to level up again based upon their recharge rates
and current experience. It uses a bit of statistics to be able to
guess how long it'll take to level up.

=================
Table of Contents
=================
- [Installation][install]
- [Details][details]
- [Usage][usage]
- [Caveats and Future Development][todo] 
- [Bug Reports and Suggestions][bugs] 
- [Thanks][thanks]

[install]: ./loats-ttnl-calculator#installation "Installation"
[details]: ./loats-ttnl-calculator#details "Details"
[usage]: ./loats-ttnl-calculator#usage "Usage"
[todo]: ./loats-ttnl-calculator#caveats--future-development 
        "Caveats and Future Development"
[bugs]: ./loats-ttnl-calculator#bug-reports-and-suggestions 
        "Bug Reports and Suggestions"
[thanks]: ./loats-ttnl-calculator#thanks "Thanks"

============
Installation
============
To install this program, just download the zip archive or the source,
and place in a directory of your choosing.

Please note that you must have [Python](http://www.python.org)
installed on your system to use this script.

============
Details
============
The following are some values critical to understanding how this
script works:

Experience points given per point of staming used: 1-5xp  
Experience points given per point of energy or hoonor used: 1-2xp  

Assuming that the experience given is normally distributed, this
gives:

Expected experience per stamina point used: 3xp  
Expected expereince per energy or honor point used: 1.5xp  

From there, it is just a matter of normalizing the recharge rates and
expected experiences values to experience per second, summing that all
up, and dividing the current experience needed to next level to arrive
at three predictions.

Worst case assumes that the least experience is always gained per
hit. The average case assumes the expected value, and the best case
assumes that the most experience is always given.

============
Usage
============
Either double-click the lots_tnl.py file or run it from a terminal:

$> ./lots_tnl.py

Enter minutes to recharge 1 energy point: 1  
Enter seconds to recharge 1 energy point: 30  
Enter minutes to recharge 1 stamina point: 1  
Enter seconds to recharge 1 stamina point: 50  
Enter minutes to recharge 1 honor point: 2  
Enter seconds to recharge 1 honor point: 0  
Enter remaining experience until next level: 1000  

...

Press enter to continue...

<img src="https://github.com/queertypes/loats-ttnl-calculator/raw/master/docs/ttnl-calc.png"
     width="684"
     height="321"
     alt="ttnl-calc in action!"/>

============
Caveats & Future Development
============
This script does not take into account:

1. How much stamina, energy, or honor you have remaining.
2. How much HP you have at the moment.
3. The energy predicted XP is calculated based upon being able to hit
   an energy raid, which is either Vince Vortex or a World Raid.
4. The presence of experience boosting tactics, like Take a Chance or
   PoE, including factors that might affect that like one's LSI.

The script assumes that the distribution of experience values is a normal distribution.

Future development may attempt to consider these factors and refine
this assumption with gathered data.

===========================
Bug Reports and Suggestions
===========================

If you find any cases that crash the program, don't display corectly,
or if you find that the predictions are off (especially the worst and
best cases!), please send an email to:

allele.dev@gmail.com

To make the fixing process faster, please use the following template:

Operating system: (Linux, Mac OS, Windows)  
Python version:  
Expected:  

Actual:  

Problem:  


============
Thanks
============

* Thanks to ClownLily for reviewing this program.
* Thanks to the author of colorama, Jonathan Hartley.
* Thanks to the creators of Legacy of a Thousand Suns for making a very
  entertaining game.
