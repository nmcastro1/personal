#ifndef STRUCTURES_H
#define STRUCTURES_H

#include "math.h"
//Ambient light intensity
#define AMB 1.0
#define MAXDEP 5
#define ABIGNUMBER 1000000000.0
//reflected and refracted ray coeff

struct ray{
	float px, py, pz; //Initial point coordinates
	float ux, uy, uz; //Directional unitary vector coordinates
};

struct color {
	float r, g, b;		// Color (R,G,B values)
};

struct vect{
	float x, y, z;

	float dotProd(vect a, vect b){
		return (a.x * b.x) + (a.y * b.y) + (a.z * b.z);
	}
	float size(){
		return sqrt(x*x + y*y + z*z);
	}
	void unitarize(){//makes this vector a unitary vector
		float sz = 1.0 / (this->size());
		x = x*sz;
		y = y*sz;
		z = z*sz;
	}
};

enum {SPHERE, PLANE, GRID};

#endif
