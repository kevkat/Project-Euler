#include <iostream>

using namespace std;

int main () {
	long top=600851475143;
	long x=2;
	while (x<top) {
		if (top%x==0) {
			top = top/x;
			cout << top << endl;
		}
		else {
			x += 1;
		}
	}
	cout << top << endl;
}