#include <bits/stdc++.h>
using namespace std;

#define All(c) (c).begin(),(c).end()
#define ll long long int
#define ull unsigned long long
#define ui unsigned int
#define us unsigned short
#define pb push_back
#define mp make_pair
#define sc second
#define fr first
typedef vector<ll> vi; 
typedef vector<vi> vvi; 
typedef pair<ll,ll> ii; 


ll modInverse2;

ll modFact(ll n, ll p)
{
    if (n >= p)
        return 0;
 
    ll result = 1;
    for (ll i = 1; i <= n; i++)
        result = (result * i) % p;
 
    return result;
}

ll calcF(ll n, ll i, ll m) {
	ll _tempa = (n-i) % m;
	ll _tempb = ((n-i)+1) % m;
	ll a = (_tempa*_tempb) % m; 
	if ( a == 0 ) return 1;
	if ( m % 2 == 0 ) return a / 2;
	else return (modInverse2 * a) % m ;
}


// d - d of the subtree we're calculating 
// dB - d of the tree before this one
ll calculateNextSubtree(ll n, ll k, ll w, ll i, ll d, ll dB, ll m) {
	ll _tempC =(n-i) % m;
	ll a = (_tempC*k) % m;
	a = (a + w ) % m;
	ll _tempA = (i*d) % m;
	a = (a +  _tempA) % m;
	ll _tempB = (calcF(n, i, m)*dB) % m;
	a = ( a +  _tempB ) % m;
	return a % m;
}

ll calc2(ll n, ll m) {
	if ( n <= 2 ) return 0;
	if ( n == 3 ) return 1;
	if ( n == 4 ) return 15;
	// ll d[n];
	vector<ll> d(n,0);
	vector<ll> k(n,0);
	vector<ll> dSoFar(n,0);
	vector<ll> kSoFar(n,0);
	d[1] = 1; k[1] = 1;
	d[2] = n; k[2] = (n*(n+3))/2;
	kSoFar[1] = 1; kSoFar[2] = 1+k[2];
	dSoFar[1] = 1; dSoFar[2] = n+1;
 	for ( ll i = 3; i<n-1; i++ ) {
 		ll _tempA= (d[i-1] * (n-i+1) ) % m;
 		ll _tempB = (dSoFar[i-2] + 1) % m;
 		d[i] = ( _tempA + _tempB ) % m; 
		k[i] = calculateNextSubtree(n, k[i-1], kSoFar[i-1], i, d[i], d[i-1], m);
		kSoFar[i] = (k[i] + kSoFar[i-1]) % m;
		dSoFar[i] = ( dSoFar[i-1] + d[i] ) % m; 
	}
	return kSoFar[n-2] % m;
}


ll calcFinal(ll pattern, ll n, ll m, ll factMinusOne ) {
	ll final=0;
	for ( ll x = 1; x<n; x++ ) {
		ll a = (factMinusOne * (n-1) ) % m;
		a = ( a * x ) % m;
		final = ( final + a ) % m;
		//cout << final << "\n";
	}
	ll c = ( n * pattern ) % m;
	return ( final + c ) % m;
}
  
int gcdExtended(int a, int b, int *x, int *y) 
{ 
    if (a == 0) 
    { 
        *x = 0; 
        *y = 1; 
        return b; 
    } 
  
    int x1, y1; 
    int gcd = gcdExtended(b%a, a, &x1, &y1); 
    *x = y1 - (b/a) * x1; 
    *y = x1; 
  
    return gcd; 
} 

int modInverse(int b, int m)
{
    int x, y;
    int g = gcdExtended(b, m, &x, &y);
    if (g != 1)
        return -1;
    return (x%m + m) % m;
}

int main() {
	ios_base::sync_with_stdio(0);
   	cin.tie(0);
	ll n, m;
	cin >> n >> m;
	modInverse2 = modInverse(2, m);
	ll facMinusOne = modFact(n-1, m);
	ll pattern = calc2(n, m);
	//prllf("%llu", pattern);
	cout << calcFinal(pattern, n, m, facMinusOne);
	return 0;
}



