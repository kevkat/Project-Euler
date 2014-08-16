#include <iostream>

using namespace std;

int main () {
	int lim=4000000;
	int current=1;
	int last=2;
	int total_evens;
	for (  ; current<lim ; last=current+last, current=last-current ) {
		cout << current << endl;
		if (current%2==0) {
			total_evens = total_evens + current;
		}
	}
	cout << "Sum: " << total_evens << endl;
}