#include <iostream>
#include "triangle.h"

Triangle::Triangle() :p1(), p2(), p3() { std::cout << "Triangle defualt" << std::endl; }

Triangle::Triangle(const Point& a, const Point& b, const Point& c)
	: p1(a), p2(b), p3(c) {
	std::cout << "Triangle 积己" << std::endl;
}

Triangle::Triangle(const Triangle& other) : p1(other.p1), p2(other.p2), p3(other.p3) { std::cout << "Triangle 汗荤积己" << std::endl; }
Triangle::~Triangle() { std::cout << "Triangle 家戈" << std::endl; }

void Triangle::draw() const
{

	std::cout << "伙阿屈 - (" << p1.x << ',' << p1.y << "), (" << p2.x << ',' << p2.y << "), (" << p3.x << ',' << p3.y << ')' << std::endl;
}
