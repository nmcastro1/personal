#include "object.h"

class Light{
public:
	Light(float px, float py, float pz, float cr, float cb, float cg);

	float x, y, z;//position of the light source

	float r, b, g;//color of the light source

	//This function returns the ray from a point to the light source
	ray rayToLight(float ix, float iy,float iz);
	//calculates the diffuse and specular light coming from this source
	color getDiffuse(float kd, Intersect * in, ray * rr);
	color getSpecular(float ks, float ns, Intersect * in, ray* rr, ray *view);
};
