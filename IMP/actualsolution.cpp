#include <bits/stdc++.h>
using namespace std;

#define All(c) (c).begin(),(c).end()
#define ll long long int
#define ull unsigned long int
#define ui unsigned int
#define us unsigned short
#define pb push_back
#define mp make_pair
#define sc second
#define fr first
typedef vector<ll> vi; 
typedef vector<vi> vvi; 
typedef pair<ll,ll> ii; 

constexpr long m = 1e9+7;
constexpr long MAX_IN = 1e6+7;

long long weirdIter(long long z, long long k) {
	if ( k == 0 ) return 1;
	long long ctr=1;
	for ( long long i = z; i>(z-k); i--) {
		ctr = ( ctr * i ) % m;
	}
	return ctr % m;
}

long long modFact(long long w)
{
	if ( w == 0 ) return 1;
    if (w >= m)
        return 0;
 
    long long result = 1;
    for (long i = 1; i <= w; i++)
        result = (result * i) % m;
 
    return result;
}

// typy:
// A - pusty
// B - 1 możliwy
// C - 2 możliwe
// D - pewniak

struct Option {
	char type;
	long a=0;
	long b=0;
};

long getBVal(Option opt) {
	return opt.a == -1 ? opt.b : opt.a;
}

long long moduloMultiplication(long long a, long long  b)
{
    long long res = 0; 
    a %= m;
    while (b)
    {
        if (b & 1)
            res = (res + a) % m;
        a = (2 * a) % m;
        b >>= 1; 
    }
 
    return res;
}


long n=0;
long unknownLength=0;
bool taken[MAX_IN] = {false};
long instructions[MAX_IN] = {0};
Option prePattern[MAX_IN];
long encounters[MAX_IN]={0};
long inCounter[MAX_IN+1]={0};
long positions[MAX_IN+1][2];


bool __counter_temp[MAX_IN]={false};

bool verifyInput() {
	
	for ( long i = 0; i<n; i++ ) {
		inCounter[ instructions[i] ]++;
		if ( inCounter[instructions[i]] > 2 ) return false;
		positions[instructions[i]][ inCounter[instructions[i]]-1 ] = i;
		if ( inCounter[instructions[i]] == 2 ) {
			if ( abs(positions[instructions[i]][0] - positions[instructions[i]][1]) != 2 )
				return false;
		}
	}

	
	return true;
}

long long calculateSolution() {
	// find k, z, w, h=(z-k)
	// cout << "UnknwonLength (z): " <<  unknownLength << "\n";
	long z = unknownLength;
	long k = 0;
	for ( long i = 0; i<n; i++ ) {
		if ( prePattern[i].type == 'A' ) k++;
	}
	// cout << "'A' counter (k): " << k << "\n";

	vector<long> segments;

	// Iterate over even segments and count them
	long __cache=0;
	bool goingOverSegment=false;
	for ( long p = 0; p<2; p++ ) {
		for ( long i = p; i<n; i+=2 ) {
			if ( i >= n ) break;
			if ( goingOverSegment ) {
				if ( prePattern[i].type=='C' ) __cache+=1;
				else if ( prePattern[i].type=='B' ) {
					__cache+=1;
					segments.pb(__cache);
					__cache = 0;
					goingOverSegment=false;
				}
			} else {
				if (prePattern[i].type=='B') {
					goingOverSegment=true;
					__cache+=1;
				}
			}
		}
	}

	// multiply everything up
	long long solution=1;
	for ( long long i = 0; i<segments.size(); i++) {
		solution = moduloMultiplication(solution, segments[i]);
	}

	// cout << "Solution: " << solution << "\n";
	// cout << "segments that are faulty: \n";
	// for ( auto v : segments ) {
	// 	if ( v <= 0 )
	// 		cout << v << ", ";
	// }
	// cout << "\n";

	// mulitply by factorial of amount of the segments
	long long factSegSize = modFact((long long)segments.size()) % m;

	// cout << "factSegSize: " << factSegSize << "\n";

	solution = (solution * factSegSize) % m;
	return  (solution * weirdIter(z, k)) % m;
}

int main() {
	ios_base::sync_with_stdio(0);
   	cin.tie(0);
	cin >> n;
	
	for ( long i = 0; i<n; i++ ) {
		cin >> instructions[i];
		__counter_temp[ instructions[i] ] = true;
	}
	
	if ( !verifyInput() ) {
		cout << 0 << "\n";
		return 0;
	}
	
	for ( long i = 1; i<n+1; i++ ) 
		if ( !__counter_temp[i] )
			unknownLength++;
	
	
	if ( unknownLength == 0 ) {
		if ( n % 2 == 1 ) cout << 0 << "\n";
		else cout << 1 << "\n";
		return 0;
	}
	

	
	// pre initiate data
	prePattern[0].type = 'B'; prePattern[n-1].type = 'B';
	prePattern[0].a = instructions[1]; prePattern[0].b = -1;
	prePattern[n-1].a = instructions[n-2]; prePattern[n-1].b = -1;
	
	prePattern[1].type = 'D'; prePattern[n-2].type = 'D';
	prePattern[1].a = instructions[0]; prePattern[1].b = instructions[0];
	prePattern[n-2].a = instructions[n-1]; prePattern[n-2].b = instructions[n-1];
	taken[ instructions[n-1] ] = true;
	taken[ instructions[0] ] = true;
	
	// Populate according to pairs 
	for ( long i = 2; i<n-2; i++ ) { 
		prePattern[i].a = instructions[i-1];
		prePattern[i].b = instructions[i+1];
		prePattern[i].type = 'C';
		if ( prePattern[i].a == prePattern[i].b ) { 
			prePattern[i].type = 'D';
			taken[ prePattern[i].a ] = true;
		}
	}
	
	
	// Populate with the rule of standing next to a already known
	for ( long i = 2; i<n-2; i++ ) {
		if ( prePattern[i-2].type == 'D' ) {
			if ( prePattern[i-2].a != instructions[i-1] ) {
				prePattern[i].type = 'D';
				prePattern[i].a = instructions[i-1];
				prePattern[i].b = instructions[i-1];
				taken[ prePattern[i].a ] = true;
			}
		}
		if ( prePattern[i+2].type == 'D' ) {
			if ( prePattern[i+2].a != instructions[i+1] ) {
				prePattern[i].type = 'D';
				prePattern[i].a = instructions[i+1];
				prePattern[i].b = instructions[i+1];
				taken[ prePattern[i].a ] = true;
			}
		}
	}
	
	// prune taken
	for ( long i = 0; i<n; i++ ) {
		switch ( prePattern[i].type ) {
			case 'C':
				if ( taken[prePattern[i].a]&&taken[prePattern[i].b] )
					prePattern[i].type='A';
				if ( taken[prePattern[i].b] ) {
					prePattern[i].type='B';
					prePattern[i].b=-1; 
				}
				if ( taken[prePattern[i].a] ) {
					prePattern[i].type='B';
					prePattern[i].a=-1; 
				}
				
				
				break;
			case 'B':
				if ( taken[getBVal( prePattern[i] )] )
					prePattern[i].type='A';
				break;
			default:
				break;
		}
	}
	
	// count encounters
	for ( long i = 0; i<n; i++ ) {
		if ( prePattern[i].type == 'D' ) 
			encounters[ prePattern[i].a ]++;
		else if ( prePattern[i].type == 'B' ) 
			encounters[(prePattern[i].a==-1?prePattern[i].b:prePattern[i].a)]++;
		else if ( prePattern[i].type == 'C' ) {
			encounters[ prePattern[i].a ]++;
			encounters[ prePattern[i].b ]++;
		}	
	}
	
	

	// final iteration process
	for ( long i = 0; i<n; i++) {
		bool hasChanged=false;
		Option patt = prePattern[i];
		if ( patt.type == 'D' ) continue;
		if ( patt.type == 'A' ) continue;
		if ( patt.b != -1 && encounters[patt.b] == 1 ) {
			encounters[patt.a]--;
			prePattern[i].type = 'D'; 
			prePattern[i].a = patt.b; 
			hasChanged=true;
			if ( taken[patt.b] ) {
				prePattern[i].type = 'A';
			}
			taken[ patt.b ] = true;
		
		} else if ( patt.a != -1 && encounters[patt.a] == 1 ) {
			encounters[patt.b]--;
			prePattern[i].type = 'D'; 
			prePattern[i].b = patt.a; 
			hasChanged=true;
			if ( taken[patt.a] ) {
				prePattern[i].type = 'A';
			}
			taken[ patt.a ] = true;
		}
		
		if ( hasChanged && i >= 2 ) i-=3;
	}
	
	for ( long i = 0; i<n; i++ ) {
		if ( prePattern[i].type != 'D' ) {
			if ( prePattern[i].a == -1 && prePattern[i].b == -1 ) prePattern[i].type = 'A';
		}
	}

	cout << calculateSolution() << "\n";
	
	return 0;
}



