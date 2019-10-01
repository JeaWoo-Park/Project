#include "shape.h"

class ShapeManager {
	int nShape;
	int capacity;
	Shape** shapes;
public:
	explicit ShapeManager(int n);
	
	~ShapeManager();

	ShapeManager(const ShapeManager&) = default;
	
	int Check();
	void Dsearch(int);
	void Search(int);
	void insert(Shape*,int);
	void draw() const;
	void Extra();
};