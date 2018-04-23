#include "object.h"

class Sphere : public Obj{
public:
	Sphere(float cx, float cy, float cz, float radious, float r, float b, float g, 
		float ka, float kd, float ks, float ns, float reflex, float refract, float ir);
	//checks if ray r intersects with the sphere, and if it does it returns the intersection info
	Intersect hitRay(ray r);
private:
	float x, y, z;//center coordinates
	float rad;//radious
};
