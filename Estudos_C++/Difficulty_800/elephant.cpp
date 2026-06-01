#include <iostream>
using namespace std;

int main() {
    int x;
    int passos;
    cin >> x;

    passos = x/5;
    if (x%5 != 0) {
        ++passos;
    }
    cout << passos;
    return 0;
}