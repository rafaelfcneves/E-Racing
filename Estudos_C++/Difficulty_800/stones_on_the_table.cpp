#include <iostream>
using namespace std;

int main() {
    int n = 0, contador = 0;
    string s;
    cin >> n;
    cin >> s;

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == s[i+1]) {
            ++contador;
        }
    }
    cout << contador;
    return 0;
}