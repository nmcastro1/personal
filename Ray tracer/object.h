#ifndef OBJECT_H
#define OBJECT_H

#include <vector>
#include "structures.h"

struct Intersect{
	bool found;
	float x,y,z; //Intersection point coordinates
	vect u; //Normal vector components
	float t;//distance calculated from the ray parameters
};

//I don't think you can name a class 'Object'
class Obj{
	public:
		Obj(float cr, float cb, float cg, float kka, float kkd, float kks, float nns, float refl, float fract, float iir){
			r = cr; g = cg; b = cb;
			ka = kka; kd = kkd; ks = kks; ns = nns;
			reflex = refl;
			refract = fract;
			ir = iir;
		}
		//float x, y, z;
		float r, b, g;//colors for the object
		float ka, kd, ks, ns;//ambient, diffuse and specular light coefficients
		float reflex, refract, ir;//ir = index of refraction

		int type;

		Intersect temp;
		//Virtual functions for support for the different shapes such as planes and spheres
		//hitray calculates the intersection point between the ray r and the object
		Intersect virtual hitRay(ray r) = 0;

	protected:
		//none
};

#endif
