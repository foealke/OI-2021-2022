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

constexpr int MAX_MN = 1e3+7;

int n, m;
char tab[MAX_MN][MAX_MN];

constexpr int p = 1e9+7;

bool checkR(int& x, int& y, int& len, char * pattern, bool (*taken)[MAX_MN]) {
	if ( x+len > m ) return false;
	bool failed=false;
	for ( int i = 0; i<len; i++ ) {
		if ( (tab[y][x+i] != pattern[i]) || taken[y][x+i] ) failed=true;
	}
	if ( !failed ) {
		for ( int i = 0; i<len; i++ ) taken[y][x+i]=true;
	}
	return !failed;
}
bool checkD(int& x, int& y, int& len, char * pattern, bool (*taken)[MAX_MN]) {
	if ( y+len > n ) return false;
	bool failed=false;
	for ( int i = 0; i<len; i++ ) {
		if ( (tab[y+i][x] != pattern[i]) || taken[y+i][x] ) failed=true;
	}
	if ( !failed ) {
		for ( int i = 0; i<len; i++ ) taken[y+i][x]=true;
	}
	return !failed;
}

bool check(int len, char * pattern) {
	if ( pattern[len-1] != tab[n-1][m-1] ) return false;
	bool taken[MAX_MN][MAX_MN] = {0};
	
	// Od góry do dołu, od lewej do prawej i sprawdzamy najpiew czy pasuje w dół
	for ( int x = 0; x<m; x++) {
		for ( int y = 0; y<n; y++) {
			if ( taken[y][x] ) continue;
			if ( !checkD(x,y,len,pattern,taken) ) {
				if ( !(checkR(x,y,len,pattern,taken))) {
					return false;
				}
			}
		}
	}
	return true;
}


int main() {
	ios_base::sync_with_stdio(0);
   	cin.tie(0);
    cin >> n >> m;
	unordered_map<char, int> char_occ;
	string alf = "qwertyuiopasdfghjklzxcvbnm";
	for ( int i = 0; i<n; i++ ) {
		for ( int x = 0; x<m; x++ ) {
			char _temp; cin >> _temp;
			if (char_occ.find(_temp) != char_occ.end() )
				char_occ[_temp]++;
			else
				char_occ[_temp]=1;
			tab[i][x] = _temp;
		}
	}
	// find first and last character of each segment
    char fC = tab[0][0]; char lC = tab[n-1][m-1];
    // find all possible lengths 
    // ( all divisors of m*n that are 
    // less or equal to max(m,n))
    vector<int> lengths;
    for ( int i = max(m,n); i>0; i--) {
    	if ( (m*n) % i == 0 ) lengths.pb(i);
    }
    
    // eliminate all divisors which are not possible
    // ( d - divisor, o - letter occurance )
    // divisor is ok if (for each letter)
    // o % ((m*n)/d) == 0 
    vector<int> posLengths;
    for ( int i = 0; i<lengths.size();i++ ) {
    	bool _check=true;
    	for ( auto d : char_occ ) {
    		if ( d.sc % ((m*n)/ lengths[i] ) != 0 ) _check=false; 
    	}
    	if ( _check ) posLengths.pb( lengths[i] ); 
    }
    
    vector<int> solution;
    
    if ( char_occ.size() == 1 ) {
    	for ( int i = 1; i<max(m,n)+1; i++ ) {
			if ( m % i == 0 || n % i == 0 ) solution.pb(i);
    	}
    } else {
    	for ( auto v : posLengths ) {
	    	char patternR[v]; char patternD[v];
	    	for ( int i = 0; i<v; i++ ) {
	    		patternR[i] = tab[0][i];
	    		patternD[i] = tab[i][0];
	    	}
	    	if ( (m >= v && check(v, patternR)) || (n >= v && check(v, patternD)) ) 
	    		solution.pb(v);
	    }
	    sort(solution.begin(), solution.end());
    }
    
    
    cout << (int)solution.size() << "\n";
    for ( auto v : solution ) cout << v << " "; 
}



