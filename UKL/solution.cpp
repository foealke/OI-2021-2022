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

ull n,m;

ull stageA() {
	ull s=1;
	ull a=1;
	ull i=n-1;
	ull diff=1;
	while(i>=1) {
		a=(a*i);
		s=(s+a);
		i--;
		if ( i == 2 ) diff = a;
	}

	return s+((n-2)*a - diff);
}


int main() {
	ios_base::sync_with_stdio(0);
   	cin.tie(0);
    cin >> n >> m;
    if ( n == 2 ) cout << "1\n";
	else cout << stageA() << "\n";
}



