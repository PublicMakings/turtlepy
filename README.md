# turtlepy
more automated drawings using python and turtle

outputs a widescreen vector file suited for two 1920x1080 monitors

random letters in filename are the seed used to generate pattern, numbers are a unique time stamp.

various results:

https://github.com/jrparadis/turtlepy/blob/master/good-bubblesbdqjw1704210104035.svg

https://github.com/jrparadis/turtlepy/blob/master/good-lookslikebirdsxnunptgs1704211110336.svg

https://github.com/jrparadis/turtlepy/blob/master/goodbreakhejwfz1704210104745.svg

https://github.com/jrparadis/turtlepy/blob/master/goodcolorsqrsiiceaopgbqb1704210105136.svg

https://github.com/jrparadis/turtlepy/blob/master/goodiikyndkinqei1704210104858.svg

you should be able view them at full resolution (they are about 1 to 2mb each) by right clicking on the thumb nails in the above links selecting view image. works in firefox and chrome, not sure about other browsers but they should be able to view svg files at full size too.

future ideas:

more colors, put colors used in filename, make filename output better

output in png instead of svg?

manually input seed instead of randomly generating one, would allow words to be used as seed to generate pattern

various thoughts:

using moveto(each,xThis,yThis,0) on each one when it moves off screen makes more interesting patterns than the moving all 5 if one goes off screen.

picking colors is tough, palette generator websites are very useful. might want to randomize the amount of colors drawing at once.

long patterns look nice at the beginning, but quickly get too busy. short patterns are basic but build up nicely. 

lines still draw out of frame on occasion, but making it call that function every time would make this script even slower than it already is. it's better to just discard the broken ones and limit the random ranges so it happens less.
