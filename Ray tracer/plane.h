#include "object.h"

class Plane : public Obj{
public:
	Plane(float ea, float eb, float ec, float ed, float r, float b, float g, 
		float ka, float kd, float ks, float ns, float reflex, float refract, float ir);
	//checks if ray r intersects with the plane, and if it does it returns the intersection info
	Intersect hitRay(ray r);
private:
	float ea, eb, ec, ed;//plane equation coefficients
};
