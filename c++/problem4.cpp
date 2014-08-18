#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;
using std::stringstream;
using std::string;

bool is_palindrome(string n) {
	
	int num = 0;
	for (int i = 0; i < n.length(); i++) {
		num *= 10;
		num += n[i] - '0';
	}

	int num2 = 0;
	for (int i = n.length() - 1; i >= 0; i--) {
		num2 *= 10;
		num2 += n[i] - '0';
	}
	return (num == num2) ? true : false;
}

int find_palindromes(int rangemin, int rangemax) {
	int palindromes[10000];
	for (const auto &x : )
}

int main (void) {
	if (is_palindrome("1011")) {
		cout << "True!" << endl;
	} else {
		cout << "False." << endl;
	}
}