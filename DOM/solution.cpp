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

ull m;

vector<ull> allFibsTo88 = { 1, 2, 3, 5, 8, 13, 
21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 
4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 
196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 
5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 
102334155, 165580141, 267914296, 433494437, 701408733, 
1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 
12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 
139583862445, 225851433717, 365435296162, 591286729879, 
956722026041, 1548008755920, 2504730781961, 4052739537881, 
6557470319842, 10610209857723, 17167680177565, 27777890035288, 
44945570212853, 72723460248141, 117669030460994, 
190392490709135, 308061521170129, 498454011879264, 
806515533049393, 1304969544928657, 2111485077978050, 
3416454622906707, 5527939700884757, 8944394323791464, 
14472334024676221, 23416728348467685, 37889062373143906, 
61305790721611591, 99194853094755497, 160500643816367088, 
259695496911122585, 420196140727489673, 679891637638612258,
1100087778366101931,  };

ull fibUpBound(ull n) {
	return *upper_bound(allFibsTo88.begin(),allFibsTo88.end(), n);
}

int fibUpBoundIDX(ull n) {
	return upper_bound(allFibsTo88.begin(),allFibsTo88.end(), n)-allFibsTo88.begin();
}

int calc(ull n, int acc, int _cache) {
	if ( n == 1 ) return acc;
	
	for ( int i = _cache; i>0; i-- ) {
		if ( n % allFibsTo88[i] == 0 ) 
			return calc(n/allFibsTo88[i], acc + (i+2), _cache);
	}
	return -1;
}


int main() {
	ios_base::sync_with_stdio(0);
   	cin.tie(0);
    cin >> m;
    for(int i = 0; i<(int)allFibsTo88.size();i++) {
    	if ( m == allFibsTo88[i] ) {
    		cout << i+1;
    		return 0;
    	}
    }
    int sol=calc(m, 0, fibUpBoundIDX(m));
    if ( sol == -1 ) cout << "NIE";
    else cout << sol-1 << "\n";
}



