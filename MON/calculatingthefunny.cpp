#include <bits/stdc++.h>
using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define ll long long
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short
#define pb push_back
#define mp make_pair
#define sc second
#define fr first
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 

ull modFact(ull n, ull p)
{
    if (n >= p)
        return 0;
 
    ull result = 1;
    for (ull i = 1; i <= n; i++)
        result = (result * i) % p;
 
    return result;
}


ull calc(ull n, ull m, ull facMinusTwo) {
	ull s=0;
	
	// Adding 1+2+3+...+n-20
	s = (s + (n-2)*(n-1)/2 ) % m;
	
	// adding 1+2+3+...+n-1 on all blocks
	s = (s + ((n-1)*(n)/2) * (facMinusTwo-1) ) % m;
	
	for ( int i = 2; i<n-2; i++ ) {
		
	}
	
	return s;
}

int main() {
	ull n, m;
	cin >> n >> m;
	ull facMinusTwo = modFact(n-2, m);
	cout << calc(n, m, facMinusTwo);
}



