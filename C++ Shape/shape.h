#ifndef _Shape
#define _Shape

class Shape {
public:
	
	Shape() {};
	virtual ~Shape() { };
	int shapenum;
	virtual void draw() const = 0;
};

#endif // _Shape
