#include <iostream>

using namespace std;

int main () {
	int sum;
	for ( int x=999; x>0; x-- ) {
		if ( x%3 == 0 || x%5 == 0 ) {
			sum += x;
			/* test print */
			/* cout << x << endl; */
		}
	}
	cout << sum << endl;
	return 0;
}