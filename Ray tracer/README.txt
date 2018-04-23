Mario Castro - csce 441

The raytracer - option 2
It uses a object class, from which a sphere class and a plane class derive from.
The it has a main ray tracing function that does exactly what the algorithm in class says.

Now on how to use it, the objects and lights are defined in the init() function and added
to the vector that containes them.

The constructors take the specifications for the objects in this order:
Sphere - center coordinates x,y,z and radious
Plane - normal vector components x,y,z and distance away from origin

color r,g,b
local lightning constants plus the exponent n for the specular light: ka, kd, ks, ns

ray tracing tree constants: reflexion, refraction, and index of refraction for the material

The image as it is now contains 2 light sources and 3 planes and 3 spheres.
One sphere is normal, one is refractive and one is reflective.
The two planes that serve as walls are normal as well, and the one on the botton has a grid pattern
and is reflective. If you look closely you can see the spheres reflecting on it, or you can
comment the line in the init() function that says s4->type = GRID;

the eye is defined as a global variable, right now is at 300,300,500
The projection plane or the screen starts at the origin, and it stays at z=0, with
x and y growing in the positive directions.

Btw, the light can change in color, one light source is blue-ish..the other one is white