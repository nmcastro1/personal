#include "Plane.h"

Plane :: Plane(float fea, float feb, float fec, float fed, float r, float b, float g, 
		float ka, float kd, float ks, float ns, float reflex, float refract, float ir)
		: Obj(r, b, g, ka, kd, ks, ns, reflex, refract, ir){
	vect vv;
	vv.x = fea;
	vv.y = feb;
	vv.z = fec;
	vv.unitarize();
	ea = vv.x;
	eb = vv.y;
	ec = vv.z;
	ed = fed;
	Obj :: type = PLANE;
}

Intersect Plane :: hitRay(ray r){
	Intersect i;
	//The basic idea is to substitute the ray equation into the plane equation
	//after simplifying terms we get this:
	float up, down, t;
	down = ea * r.ux + eb * r.uy + ec * r.uz;
	if(down >= -0.001){//ray is most likely parallel to pthe plane
		i.found = false; i.t = i.x = i.y = i.z = 0.0;
		i.u.x = i.u.y = i.u.z = 0.0;
		Obj :: temp = i;
		return i;
	}
	up = -(ea * r.px + eb * r.py + ec * r.pz + ed);
	t = up / down;

	if(t < 0.0){
		i.found = false; i.t = i.x = i.y = i.z = 0.0;
		i.u.x = i.u.y = i.u.z = 0.0;
		Obj :: temp = i;
		return i;
	}
	i.found = true;
	i.x = r.px + r.ux * t;
	i.y = r.py + r.uy * t;
	i.z = r.pz + r.uz * t;
	//Unit normal vector
	i.u.x = ea;
	i.u.y = eb;
	i.u.z = ec;
	//distance between the root of the ray and the intersection point
	i.t = t;

	Obj :: temp = i;

	return i;

}
