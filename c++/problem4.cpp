#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int palindromecheck(int n);

// rewritten to avoid using strings, seems to be more efficient and avoids the inelegance of string manipulation in c++ 
int palindromecheck(int n) {
    int m,sum=0,temp,check;
    temp=n;
    while(n){
        m=n%10;
        n=n/10;
        sum=sum*10+m;
    }

    if(temp==sum)
    check=1;
    else
    check=0;
    return check;
}

int main() {
    vector<int> palindromes;
    int num=0; int count=0;
    for(int i=1;i<=999;i++){
        for(int j=1;j<=999;j++){
            num=i*j;
        if(palindromecheck(num)){
            palindromes.push_back(count); 
            palindromes[count]=num;
            count+=1;
        }

        }
    }

	cout << "Number of palindromes before sort: " <<  palindromes.size() << endl; //test print
	sort(palindromes.begin(),palindromes.end()); 
	palindromes.erase(unique(palindromes.begin(),palindromes.end()),palindromes.end());
	cout << "Number of palindromes deduped and sorted: " << palindromes.size() << endl; //test print
	cout << "Greatest palindrome: " <<*( max_element( palindromes.begin(), palindromes.end() ) ) << endl;

}


