/**************************************
Mario Castro
**************************************/

#include "stdlib.h"
#include<GL/glut.h>

#include "sphere.h"
#include "Plane.h"
#include "light.h"
#include <vector>
#include <iostream>

#define ImageW 600
#define ImageH 600
using namespace std;

vector<Light> sources;//vector of light sources
vector<Obj *> objects;//vector containing every object in the worldspace
float eyex = 300.0, eyey = 300.0, eyez = 500.0;//eye coordinates

float framebuffer[ImageH][ImageW][3];
//Ray tracing function
color rayTracing(ray view, bool shadow, int depth, int object_id, float ldist);
ray getReflectedRay(ray view, int si);
ray getRefractedRay(ray view, Intersect imin, float c1, float c2);

// Draws the scene
void drawit(void)
{
   glDrawPixels(ImageW,ImageH,GL_RGB,GL_FLOAT,framebuffer);
   glFlush();
}

// Clears framebuffer to black
void clearFramebuffer()
{
	int i,j;

	for(i=0;i<ImageH;i++) {
		for (j=0;j<ImageW;j++) {
			framebuffer[i][j][0] = 0.0;
			framebuffer[i][j][1] = 0.0;
			framebuffer[i][j][2] = 0.0;
		}
	}
}

// Sets pixel x,y to the color RGB
void setFramebuffer(int x, int y, float R, float G, float B){
	//x and y appear to have been switched, so i fixed them back
	int tempxy = x;
	x = y;
	y = tempxy;
	if (R<=1.0)
		if (R>=0.0)
			framebuffer[x][y][0]=R;
		else
			framebuffer[x][y][0]=0.0;
	else
		framebuffer[x][y][0]=1.0;
	if (G<=1.0)
		if (G>=0.0)
			framebuffer[x][y][1]=G;
		else
			framebuffer[x][y][1]=0.0;
	else
		framebuffer[x][y][1]=1.0;
	if (B<=1.0)
		if (B>=0.0)
			framebuffer[x][y][2]=B;
		else
			framebuffer[x][y][2]=0.0;
	else
		framebuffer[x][y][2]=1.0;
}

void display(void)
{
	//The next two lines of code are for demonstration only.
	//They show how to draw a line from (0,0) to (100,100)
	//int i;
	//for(i=0;i<=100;i++) setFramebuffer(i, i, 1.0, 1.0, 1.0);

	drawit();
}

void renderImage(){
	//super duper loop
	for(int i = 0; i < ImageW; i++){
		for(int j = 0; j < ImageH; j++){
			ray jay;
			jay.px = eyex; jay.py = eyey; jay.pz = eyez;
			vect v;
			v.x = i - eyex; v.y = j - eyey; v.z = 0.0 - eyez;
			v.unitarize();
			jay.ux = v.x; jay.uy = v.y; jay.uz = v.z;
			color c = rayTracing(jay, false, 0, -1, 0.0);
			setFramebuffer(i, j, c.r, c.g, c.b);
		}
	}
	cout << "Done!" << endl;
}

void init(void){
	clearFramebuffer();
	Sphere * s1 = new Sphere(300.0, 275.0, -150.0, 100.0, 1.0, 1.0, 1.0, 0.05, 0.3, 0.2, 10.0, 0.0, 0.8, 1.1);
	Sphere * s2 = new Sphere(75.0, 250.0, -350.0, 100.0, 0.7, 0.1, 0.0, 0.5, 0.4, 0.7, 50.0, 0.0, 0.0, 0.0);
	Sphere * s3 = new Sphere(500.0, 200.0, -300.0, 100.0, 0.0, 0.6, 0.2, 0.3, 0.3, 0.3, 5.0, 0.6, 0.0, 0.0);
	Plane * s4 = new Plane(0.0, 1.0, 0.0, 300.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.6, 5.0, 0.0, 0.0, 0.0);
	s4 -> type = GRID;
	Plane * s5 = new Plane(1.0, 0.0, 1.0, 700.0, 0.0, 0.0, 0.9, 0.15, 0.2, 0.2, 5.0, 0.0, 0.0, 0.0);
	Plane * s6 = new Plane(-1.0, 0.0, 1.0, 1000.0, 0.0, 0.0, 0.9, 0.15, 0.2, 0.2, 5.0, 0.0, 0.0, 0.0);
	
	objects.push_back(s1);
	objects.push_back(s2);
	objects.push_back(s3);
	objects.push_back(s4);
	objects.push_back(s5);
	objects.push_back(s6);

	Light l1 = Light(600.0, 600.0, 800.0, 1.0, 1.0, 1.0);
	Light l2 = Light(300.0, 900.0, 100.0, 0.3, 1.0, 0.8);
	sources.push_back(l1);
	sources.push_back(l2);

	renderImage();
}

void mouse(int button, int state, int x, int y){
	switch (button){
		case GLUT_LEFT_BUTTON:
			if(state == GLUT_DOWN ){
				cout << x << ' ' << (ImageH - y) << endl;
			}
			break;
		default:
			break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowSize(ImageW,ImageH);
	glutInitWindowPosition(100,100);
	glutCreateWindow("Mario Castro - Assignment 5");
	init();	
	glutDisplayFunc(display);
	glutMouseFunc(mouse);
	glutMainLoop();
	return 0;
}

//Parameters are the incoming ray, the depth that we have traversed the tree thus far
//The index of the object that generated the reflected ray(so that we don't try and intersect it again)
//And the light info. A boolean in case the ray is a shadow ray, and the distance from the intersect to the ligh source
color rayTracing(ray view, bool shadow, int depth, int o_id, float ldist){
	color ret, reflect, refract, local;
	int si;
	if(depth > MAXDEP){
		ret.r = ret.b = ret.g = 0.0;
		return ret;
	}
	Intersect imin;//stores intersection with the shortest distance to the root of the ray
	if(shadow) imin.t = ldist;
	else imin.t = ABIGNUMBER;
	bool fmin = false;//determines if we have found a closest intersection point
	for(int i = 0; i< objects.size(); i++){
		//deals with approximation issues, if we already intersected with an object we don't wanna do it again
		if(i != o_id)objects[i]->hitRay(view);
		else continue;
		if(objects[i]->temp.found && objects[i]->temp.t <= imin.t){
			fmin = true;
			imin = objects[i]->temp;
			si = i;
		}
	}
	if(!fmin){
		if(shadow){
			ret.r = ret.b = ret.g = 1.0;//shadow ray has no obstacles; the spot has full illumination.
			return ret;
		}else{
			ret.r = ret.b = ret.g = 0.0;
			return ret;
		}
	}
	//send reflected ray
	ray rr = getReflectedRay(view, si);
	reflect = rayTracing(rr, false, depth + 1, si, 0.0);
	//send refracted ray
	//refraction didn't work out too well, so instead I used an approximation that doesn't look too bad
	if(objects[si]->ir > 0.999999){
		rr = getRefractedRay(view, imin, 1.0, objects[si]->ir);
		/*Intersect back = objects[si]->hitRay(rr);
		rr = getRefractedRay(rr, back, objects[si]->ir, 1.0);
		rr.ux = - rr.ux; rr.uy = - rr.uy; rr.uz = - rr.uz;
		objects[si]->temp = imin;*/
		refract = rayTracing(rr, false, depth + 1, si, 0.0);
	}else{
		refract.r = refract.b = refract.g = 0.0;
	}
	//calculate local illumination which is simple. the if statements are used for a grid type surface, they have a pettern like a chess board
	if(objects[si]->type == GRID){
		int cx1, cz1;
		cx1 = (imin.x < 0)? int(imin.x) % 200 + 200: int(imin.x) % 200;
		cz1 = (imin.z < 0)? int(imin.z) % 200 + 200: int(imin.z) % 200;
		if((cx1 < 100 && cz1 < 100) || (cx1 >= 100 && cz1 >= 100)){
			local.r = local.b = local.g = 1.0 * objects[si]->ka;
		}else{
			local.r = objects[si]->ka * AMB * objects[si]->r;
			local.b = objects[si]->ka * AMB * objects[si]->b;
			local.g = objects[si]->ka * AMB * objects[si]->g;
		}
	}else{
		local.r = objects[si]->ka * AMB * objects[si]->r;
		local.b = objects[si]->ka * AMB * objects[si]->b;
		local.g = objects[si]->ka * AMB * objects[si]->g;
	}
	//send shadow rays and calculate local illumination, only done once for the object
	for(int i = 0; i < sources.size(); i++){
		ray tolight = sources[i].rayToLight(imin.x, imin.y, imin.z);
		//calculate distance from intersect to light source
		vect dd; 
		dd.x = (imin.x - sources[i].x);
		dd.y = (imin.y - sources[i].y);
		dd.z = (imin.z - sources[i].z);
		//calculate the diffuse and specular light contributions
		color shad = rayTracing(tolight, true, depth + 1, si, dd.size());
		color temp1 = sources[i].getDiffuse(objects[si]->kd, &imin, &tolight);
		local.r += temp1.r * shad.r; local.b += temp1.b * shad.b; local.g += temp1.g * shad.g;
		temp1 = sources[i].getSpecular(objects[si]->ks, objects[si]->ns, &imin, &tolight, &view);
		local.r += temp1.r * shad.r; local.b += temp1.b * shad.b; local.g += temp1.g * shad.g;
	}
	//calculate global illumination
	ret.r = local.r + objects[si]->reflex * reflect.r + objects[si]->refract * refract.r;
	ret.b = local.b + objects[si]->reflex * reflect.b + objects[si]->refract * refract.b;
	ret.g = local.g + objects[si]->reflex * reflect.g + objects[si]->refract * refract.g;

	return ret;
}

ray getReflectedRay(ray view, int si){
	ray rr;
	Intersect imin = objects[si]->temp;
	rr.px = imin.x; rr.py = imin.y; rr.pz = imin.z;
	vect aux; aux.x = -view.ux; aux.y = -view.uy; aux.z = -view.uz;
	float dot = 2 * aux.dotProd(aux, imin.u);
	aux.x = dot * imin.u.x - aux.x;
	aux.y = dot * imin.u.y - aux.y;
	aux.z = dot * imin.u.z - aux.z;
	aux.unitarize();
	rr.ux = aux.x; rr.uy = aux.y; rr.uz = aux.z;

	return rr;
}

ray getRefractedRay(ray view, Intersect imin, float c1, float c2){
	ray rr;
	float vdotn;
	//initial point in the ray
	rr.px = imin.x; rr.py = imin.y; rr.pz = imin.z;
	//ray directional vector
	//right side of the equation
	vect vv;
	vv.x = -view.ux; vv.y = -view.uy; vv.z = -view.uz;
	vdotn = vv.dotProd(vv, imin.u);
	vect left, right;
	float temp1 = c2 / c1;
	right.x = temp1 * (vdotn * imin.u.x - vv.x);
	right.y = temp1 * (vdotn * imin.u.y - vv.y);
	right.z = temp1 * (vdotn * imin.u.z - vv.z);
	//left side of the equation
	temp1 = 1 - (vdotn * vdotn);
	temp1 = (c1 * c1) - (c2 * c2 * temp1);
	float temp2 = - sqrt(temp1) / c1;
	left.x = temp2 * imin.u.x;
	left.y = temp2 * imin.u.y;
	left.z = temp2 * imin.u.z;
	right.x = right.x + left.x;
	right.y = right.y + left.y;
	right.z = right.z + left.z;
	right.unitarize();
	rr.ux = right.x; rr.uy = right.y; rr.uz = right.z;

	return rr;
}
