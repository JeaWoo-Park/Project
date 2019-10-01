#include <iostream>
#include "circle.h"

Circle::Circle() : center(), rad(0) { std::cout << "CIrcle default" << std::endl; }

Circle::Circle(const Point& c, int r) : center(c), rad(r) { std::cout << "Circle 생성" << std::endl; }

Circle::Circle(const Circle& other) : center(other.center), rad(other.rad) { std::cout << "Circle 복사생성" << std::endl; }
Circle::~Circle() { std::cout << "Circle 소멸" << std::endl; }

void Circle::draw() const
{
	std::cout << "원 - 중심점(" << center.x << "," << center.y << ") 반지름 " << rad << std::endl;
}