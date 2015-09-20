#include <iostream>
using namespace std;
int step = 0;
unsigned short gcd(unsigned short u, unsigned short v)
{
    std::bitset<16> ub(u);
    std::bitset<16> vb(v);
    cout << step << " u: " << u << " " << ub << " v: " << v << " " << vb <<  endl;
    ++step;
    // simple cases (termination)
    if (u == v)
        return u;

    if (u == 0)
        return v;

    if (v == 0)
        return u;

    // look for factors of 2
    if (~u & 1) // u is even
    {
        if (v & 1) // v is odd
            return gcd(u >> 1, v);
        else // both u and v are even
            return gcd(u >> 1, v >> 1) << 1;
    }

    if (~v & 1) // u is odd, v is even
        return gcd(u, v >> 1);

    // reduce larger argument
    if (u > v)
        return gcd((u - v) >> 1, v);

    return gcd((v - u) >> 1, u);
}

int main() {

    cout << gcd(40902, 24140) << endl;
    return 0;

}
