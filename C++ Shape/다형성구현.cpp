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
	std::ofstream out1("�������� 1�� ����.txt");
	std::ofstream out2("�������� 2�� ����.txt");
	std::ofstream out3("�������� 3�� ����.txt");

	std::ifstream in1("�������� 1�� ����.txt");
	std::ifstream in2("�������� 2�� ����.txt");
	std::ifstream in3("�������� 3�� ����.txt");
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
		std::cout << "1) �����߰�" << std::endl;
		std::cout << "2) ���� ����" << std::endl;
		std::cout << "3) ��ü ���� �׸���" << std::endl;
		std::cout << "4) ����" << std::endl;
		std::cout << "5) �ҷ�����" << std::endl;
		std::cout << "6) ���α׷� ������" << std::endl;
		std::cout << "------------------------------------" << std::endl;
		std::cin >> num;
		switch (num)
		{
		case 1:
			if (sm.Check()) {
				std::cout << "���� ������ �ִ�ġ �Դϴ�." << std::endl;
				std::cout << "�ִ� ������ Ȯ��(100��) �ϰڽ��ϱ�?(y/n) ";
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
			std::cout << "1) �ﰢ��" << std::endl;
			std::cout << "2) �簢��" << std::endl;
			std::cout << "3) ��" << std::endl;
			std::cout << "4) ��" << std::endl;
			std::cout << "5) ���" << std::endl;
			std::cout << "------------------------------------" << std::endl;
			std::cin >> shape;
			switch (shape)
			{
			case 1:
			
				std::cout << "ù��° ���� ��ǥ(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "�ι�° ���� ��ǥ(x,y) : ";
				std::cin >> x2 >> y2;
				std::cout << "����° ���� ��ǥ(x,y) : ";
				std::cin >> x3 >> y3;
				if (x1 == x2 && y1 == y2) {
					std::cout << "���� ��ǥ�� �Է��� �� �����ϴ�." << std::endl;
					break;
				}if (x2 == x3 && y2 == y3) {
					std::cout << "���� ��ǥ�� �Է��� �� �����ϴ�." << std::endl;
					break;
				}if (x1 == x3 && y1 == y3) {
					std::cout << "���� ��ǥ�� �Է��� �� �����ϴ�." << std::endl;
					break;
				}
				sm.insert(new Triangle(Point(x1, y1), Point(x2, y2), Point(x3, y3)), shape);
				break;
			case 2:
				
				std::cout << "ù��° ���� ��ǥ(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "�ι�° ���� ��ǥ(x,y) : ";
				std::cin >> x2 >> y2;
				if (x1 == x2 && y1 == y2) {
					std::cout << "���� ��ǥ�� �Է��� �� �����ϴ�." << std::endl;
					break;
				}
				sm.insert(new Rectangle(Point(x1, y1), Point(x2, y2)), shape);
				
				break;
			case 3:
				std::cout << "ù��° ���� ��ǥ(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "�������� ���� : ";
				std::cin >> r;
				if (r <= 0) {
					std::cout << "�������� 0 ���ϰ� �� �� �����ϴ�." << std::endl;
					break;
				}
				sm.insert(new Circle(Point(x1, y1), r), shape);
				break;
			case 4:
				std::cout << "ù��° ���� ��ǥ(x,y) : ";
				std::cin >> x1 >> y1;
				std::cout << "�ι�° ���� ��ǥ(x,y) : ";
				std::cin >> x2 >> y2;
				if (x1 == x2 && y1 == y2) {
					std::cout << "���� ��ǥ�� �Է��� �� �����ϴ�." << std::endl;
				}
				sm.insert(new Line(Point(x1, y1), Point(x2, y2)),shape);
				break;
			case 5:
				std::cout << "����մϴ�." << std::endl;
				break;

			default:
				std::cout << "�߸��� �Է� �Դϴ�." << std::endl;
				break;
			}//�����߰� switch ��
			end:
			break;
		case 2:
			std::cout << "------------------------------------" << std::endl;
			std::cout << "1) ��ȣ�� ����" << std::endl;
			std::cout << "2) ��ü ���� ����" << std::endl;
			std::cout << "3) ���" << std::endl;
			std::cout << "------------------------------------" << std::endl;
			std::cin >> del;
			switch (del) {
			case 1:
				std::cout << "���° ������ ���� �ϳ���?" << std::endl;
				std::cin >> dsnum;
				sm.Dsearch(dsnum);
				break;
			case 2:
				std::cout << "� ������ �����ϳ���?" << std::endl;
				std::cout << "1.�ﰢ�� 2.�簢�� 3.�� 4.��" << std::endl;
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
					std::cout << "�߸��� �Է� �Դϴ�." << std::endl;
					break;
				}
				case 3:
				std::cout << "����մϴ�." << std::endl;
				break;
			}// delete switch ��
			break;
		case 3:
			sm.draw();
			break;
		case 4:
			std::cout << "��� �����մϱ�" << std::endl;
			std::cin >> save;
			switch (save)
			{
			case 1:
				out1.put(sm.draw());
				break;
			default:
				std::cout << "�߸��� �Է��Դϴ�." << std::endl;
				break;
			}
			
		case 6:
			break;
		default:
			std::cout << "�߸��� �Է� �Դϴ�." << std::endl;
			break;
		}//menu switch ��
		if (num == 6) {
			std::cout << "���α׷��� �����մϴ�." << std::endl;
			break;
		}
	
	}//while�� ��

}
	