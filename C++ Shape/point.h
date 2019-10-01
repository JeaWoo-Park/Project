#ifndef _Point
#define _Point

class Point
{
public:
	double x, y;

	Point();
	Point(double, double);
	Point(const Point&) = default;

};
#endif //  _Point
