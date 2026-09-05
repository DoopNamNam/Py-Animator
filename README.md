Python class for turning sprite sheets into working animations in python, using pygame.
You initialise an animations class, and each parameter is fairly self-explanatory, but I will go through each one.

framenum - The number of frames are in the animation.
framerate - The amount of time you want each frame to last, in seconds.
sheet - For the sprite sheet itself, in the form of a pygame sprite. This currently only works for horizontal strips.
height - The height of the animation.
width - The width of the animation, not the sprite sheet but the final animation that you want.

After this, you can use either the "animate" method to create an animation which loops indefinitely or "animateonce" to play the animation once.
If you place either of those two methods within a game loop, they will return the surface at the frame it should be at.
