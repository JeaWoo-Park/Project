#include "point.h"
#include "shape.h"

class Line : public Shape {
	Point p1, p2;
public:
	Line();
	Line(const Point&,const Point&);
	Line(const Line&);
	~Line();

	void draw() const override;

};