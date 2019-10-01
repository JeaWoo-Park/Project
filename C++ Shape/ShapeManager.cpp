#include <iostream>
#include "ShapeManager.h"

using namespace std;
ShapeManager::ShapeManager(int n)
{
	nShape = 0;
	capacity = n;
	shapes = new Shape* [capacity];
}
void ShapeManager::Search(int n)
{
	for (int i = 0; i < nShape; ++i) {	//��������
		if (shapes[i]->shapenum == n) {
			Dsearch(i + 1);
			--i;
		}
	}
}
void ShapeManager::Dsearch(int n) {	//��ȣ����
	if (n <= nShape && n > 0) {
		delete shapes[n - 1];
		for (int i = n - 1; i < nShape; ++i) {
			shapes[i] = shapes[i + 1];
		}
		--nShape;
	}
	else {
		std::cout << "�߸��� �Է� �Դϴ�." << std::endl;
	}
}
ShapeManager::~ShapeManager()
{
	for (int i = 0; i < nShape; ++i)
		delete shapes[i];
}
void ShapeManager::insert(Shape* a,int n)
{
	shapes[nShape] = a;
	nShape++;
	shapes[nShape - 1]->shapenum = n;
};
void ShapeManager::draw() const
{
	cout << "------------------------------------------------" << endl;
	cout << "�����ϴ� ��� ������ �׸��ϴ�." << endl;
	cout << "�ִ� " << capacity << "���� ������ ���� �� �ֽ��ϴ�." << endl;
	cout << "��� " << nShape << "���� ������ �ֽ��ϴ�." << endl;
	cout << "------------------------------------------------" << endl;

	for (int i = 0; i < nShape; ++i) {
		cout << "[" << i + 1 << "] ";
		shapes[i]->draw();
	}
	cout << endl;

	cout << "------------------------------------------------" << endl;
	cout << "�׸��⸦ ��Ĩ�ϴ�." << endl;
	cout << "------------------------------------------------" << endl;
};
int ShapeManager::Check() {
	if (nShape == capacity) {
		return 1;
	}if (nShape != capacity) {
		return 0;
	}

}
void ShapeManager::Extra() {
	int num = capacity + 100;
	Shape** newS = new Shape*[num];
	memcpy(newS, shapes, capacity*sizeof(Shape));
	delete[] shapes;
	capacity = num;
	shapes = newS;
}