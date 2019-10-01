#include "point.h"
#include "triangle.h"
#include "circle.h"
#include "rectangle.h"
#include "ShapeManager.h"
#include "Line.h"
#include <iostream>
#include <fstream>
int main()
{
	ShapeManager sm(100);

	//for (int i = 0; i < 100; ++i) {
	//	sm.insert(new Rectangle(Point(i, i + 1), Point(i * 2, i * 3)), 2);
	//}
	//sm.insert(new Triangle());
	//sm.insert(new Triangle(Point(0, 0), Point(1, 1), Point(2, 2)));
	//sm.insert(new Circle(Point(1.23, 4.56), 7.89));

	//for (int i = 0; i < 10; ++i) {
	//	sm.insert(new Rectangle(Point(i, i + 1), Point(i * 2, i * 3)));

	//	sm.draw();
	//}
	char as = 0;
	int dsnum = 0;
	int del = 0;
	int shape = 0;
	int num = 0;
	double x1 = 0;
	double x2 = 0;
	double x3 = 0;
	double y1 = 0;
	double y2 = 0;
	double y3 = 0;
	int r = 0;
	int save;
	std::ofstream out1("도형저장 1번 파일.txt");
	std::ofstream out2("도형저장 2번 파일.txt");
	std::ofstream out3("도형저장 3번 파일.txt");

	std::ifstream in1("도형저장 1번 파일.txt");
	std::ifstream in2("도형저장 2번 파일.txt");
	std::ifstream in3("도형저장 3번 파일.txt");
	while (true) {
		save = 0;
		dsnum = 0;
		del = 0;
		shape = 0;
		num = 0;
		x1 = 0;
		x2 = 0;
		x3 = 0;
		y1 = 0;
		y2 = 0;
		y3 = 0;
		r = 0;
		std::cout << "----------------Menu----------------" << std::endl;
		std::cout << "1) 도형추가" << std::endl;
		std::cout << "2) 도형 삭제" << std::endl;
		std::cout << "3) 전체 도형 그리기" << std::endl;
		std::cout << "4) 저장" << std::endl;
		std::cout << "5) 불러오기" << std::endl;
		std::cout << "6) 프로그램 끝내기" << std::endl;
		std::cout << "------------------------------------" << std::endl;
		std::cin >> num;
		switch (num)
		{
		case 1:
			if (sm.Check()) {
				std::cout << "도형 개수가 최대치 입니다." << std::endl;
				std::cout << "최대 개수를 확장(100개) 하겠습니까?(y/n) ";
				std::cin >> as;

				switch (as)
				{
				case 'y':
					sm.Extra();
					break;
				case 'n':
					goto end;
					break;
				}
			}
			std::cout << "------------------------------------" << std::endl;
			std::cout << "1) 삼각형" << std::endl;
			std::cout << "2) 사각형" << std::endl;
			std::cout << "3) 원" << std::endl;
			std::cout << "4) 선" << std::endl;
			std::cout << "5) 취소" << std::endl;
			std::cout << "------------------------------------" << std::endl;
			std::cin >> shape;
			switch (shape)
			{
			case 1:
			
				std::cout << "첫번째 점의 좌표(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "두번째 점의 좌표(x,y) : ";
				std::cin >> x2 >> y2;
				std::cout << "세번째 점의 좌표(x,y) : ";
				std::cin >> x3 >> y3;
				if (x1 == x2 && y1 == y2) {
					std::cout << "같은 좌표를 입력할 수 없습니다." << std::endl;
					break;
				}if (x2 == x3 && y2 == y3) {
					std::cout << "같은 좌표를 입력할 수 없습니다." << std::endl;
					break;
				}if (x1 == x3 && y1 == y3) {
					std::cout << "같은 좌표를 입력할 수 없습니다." << std::endl;
					break;
				}
				sm.insert(new Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3)), shape);
				break;
			case 2:
				
				std::cout << "첫번째 점의 좌표(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "두번째 점의 좌표(x,y) : ";
				std::cin >> x2 >> y2;
				if (x1 == x2 && y1 == y2) {
					std::cout << "같은 좌표를 입력할 수 없습니다." << std::endl;
					break;
				}
				sm.insert(new Rectangle(Point(x1, y1), Point(x2, y2)), shape);
				
				break;
			case 3:
				std::cout << "첫번째 점의 좌표(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "반지름이 길이 : ";
				std::cin >> r;
				if (r <= 0) {
					std::cout << "반지름은 0 이하가 될 수 없습니다." << std::endl;
					break;
				}
				sm.insert(new Circle(Point(x1, y1), r), shape);
				break;
			case 4:
				std::cout << "첫번째 점의 좌표(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "두번째 점의 좌표(x,y) : ";
				std::cin >> x2 >> y2;
				if (x1 == x2 && y1 == y2) {
					std::cout << "같은 좌표를 입력할 수 없습니다." << std::endl;
				}
				sm.insert(new Line(Point(x1, y1), Point(x2, y2)),shape);
				break;
			case 5:
				std::cout << "취소합니다." << std::endl;
				break;

			default:
				std::cout << "잘못된 입력 입니다." << std::endl;
				break;
			}//도형추가 switch 끝
			end:
			break;
		case 2:
			std::cout << "------------------------------------" << std::endl;
			std::cout << "1) 번호로 제거" << std::endl;
			std::cout << "2) 전체 도형 제거" << std::endl;
			std::cout << "3) 취소" << std::endl;
			std::cout << "------------------------------------" << std::endl;
			std::cin >> del;
			switch (del) {
			case 1:
				std::cout << "몇번째 도형을 삭제 하나요?" << std::endl;
				std::cin >> dsnum;
				sm.Dsearch(dsnum);
				break;
			case 2:
				std::cout << "어떤 도형을 삭제하나요?" << std::endl;
				std::cout << "1.삼각형 2.사각형 3.원 4.선" << std::endl;
				std::cin >> dsnum;
				switch (dsnum)
				{
				case 1:
					sm.Search(dsnum);
					break;
				case 2:
					sm.Search(dsnum);
					break;
				case 3:
					sm.Search(dsnum);
					break;
				case 4:
					sm.Search(dsnum);
					break;
				default:
					std::cout << "잘못된 입력 입니다." << std::endl;
					break;
				}
				case 3:
				std::cout << "취소합니다." << std::endl;
				break;
			}// delete switch 끝
			break;
		case 3:
			sm.draw();
			break;
		case 4:
			std::cout << "어디에 저장합니까" << std::endl;
			std::cin >> save;
			switch (save)
			{
			case 1:
				out1.put(sm.draw());
				break;
			default:
				std::cout << "잘못된 입력입니다." << std::endl;
				break;
			}
			
		case 6:
			break;
		default:
			std::cout << "잘못된 입력 입니다." << std::endl;
			break;
		}//menu switch 끝
		if (num == 6) {
			std::cout << "프로그램을 종료합니다." << std::endl;
			break;
		}
	
	}//while문 끝

}
	