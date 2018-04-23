#include "light.h"

Light :: Light(float px, float py, float pz, float cr, float cb, float cg){
	x = px; y = py; z = pz;
	r = cr; b = cb; g = cg;
}

//This function returns the ray from a point to the light source
ray Light :: rayToLight(float ix, float iy,float iz){
	ray ret;
	vect direct;
	ret.px = ix;
	ret.py = iy;
	ret.pz = iz;
	direct.x = (x - ix);
	direct.y = (y - iy);
	direct.z = (z - iz);
	direct.unitarize();
	ret.ux = direct.x;
	ret.uy = direct.y;
	ret.uz = direct.z;
	
	return ret;
}
//Diffuse light equals kd*Intensity*(L.N)
//calculates the diffuse light coming from this light source. If the light source is ocluded, then the dot prod is negative and the contribution is zero
color Light :: getDiffuse(float kd, Intersect * in, ray * rr){
	color cc;
	vect uu;
	uu.x = rr->ux;
	uu.y = rr->uy;
	uu.z = rr->uz;
	float dot = uu.dotProd(uu, in->u);//N.L
	if(dot < 0.0)	dot = 0.0;

	cc.r = r * kd * dot;
	cc.b = b * kd * dot;
	cc.g = g * kd * dot;

	return cc;
}
//Specular light equals ks*Intensity*(R.E)^n where R = (2N.L)N-L
color Light :: getSpecular(float ks, float ns, Intersect * in, ray * rr, ray * view){
	color cc;
	vect uu, ee, res;
	uu.x = rr->ux;//Light vector
	uu.y = rr->uy;
	uu.z = rr->uz;
	float dot = 2 * uu.dotProd(uu, in->u);
	if(dot < 0.0)	{
		cc.r = cc.b = cc.g = 0.0;
		return cc;
	}
	//resulting vector(R) in the equation
	res.x = (dot * in->u.x) - uu.x;
	res.y = (dot * in->u.y) - uu.y;
	res.z = (dot * in->u.z) - uu.z;
	//view vector
	ee.x = view->ux;
	ee.y = view->uy;
	ee.z = view->uz;
	
	dot = - res.dotProd(res, ee);
	if(dot < 0.0) dot = 0.0;
	dot = pow(dot, ns);

	cc.r = r * ks * dot;
	cc.b = b * ks * dot;
	cc.g = g * ks * dot;

	return cc;
}
