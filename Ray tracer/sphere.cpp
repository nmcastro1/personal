#include "sphere.h"

Sphere :: Sphere(float cx, float cy, float cz, float radious, float r, float b, float g, 
		float ka, float kd, float ks, float ns, float reflex, float refract, float ir)
		: Obj(r, b, g, ka, kd, ks, ns, reflex, refract, ir){
	x = cx;
	y = cy;
	z = cz;
	rad = radious;
	Obj :: type = SPHERE;
}

Intersect Sphere :: hitRay(ray r){
	Intersect i;
	//The basic idea is to substitute the ray equation into the sphere equation
	//after simplifying terms we get this:
	float qb = 1.0, qc = 1.0;
	//coefficients for the quadratic equation (A = 1)
	qb = 2 * (r.ux * (r.px - x) + r.uy * (r.py - y) +  r.uz * (r.pz - z));
	qc = (r.px - x) * (r.px - x) + (r.py - y) * (r.py - y) + (r.pz - z) * (r.pz - z) - (rad * rad);
	//calculate the discriminant and the solutions
	float discr = qb * qb - 4 * qc;
	if(discr < 0.0){//no solution. We still initialize the data inside the struct
		i.found = false; i.t = i.x = i.y = i.z = 0.0;
		i.u.x = i.u.y = i.u.z = 0.0;
		Obj :: temp = i;
		return i;
	}
	//calculate solutions
	float t;
	t = 0.5 * (- qb - sqrt(discr));
	if(t <= 0.0){//not a valid solution
		t = 0.5 * (- qb + sqrt(discr));
		if(t <= 0.0){
			i.found = false; i.t = i.x = i.y = i.z = 0.0;
			i.u.x = i.u.y = i.u.z = 0.0;
			Obj :: temp = i;
			return i;
		}
	}
	i.found = true;
	i.x = r.px + r.ux * t;
	i.y = r.py + r.uy * t;
	i.z = r.pz + r.uz * t;
	//Unit normal vector
	float sr = 1 / rad;
	i.u.x = (i.x - x) * sr;
	i.u.y = (i.y - y) * sr;
	i.u.z = (i.z - z) * sr;
	//distance between the root of the ray and the intersection point
	//i.t = sqrt((i.x - r.px) * (i.x - r.px) + (i.y - r.py) * (i.z - r.pz) + (i.z - r.pz) * (i.z - r.pz));
	i.t = t;

	Obj :: temp = i;

	return i;
}
