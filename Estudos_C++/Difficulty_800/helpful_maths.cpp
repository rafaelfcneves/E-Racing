#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s, nova_soma;
    cin >> s;
    vector<int> numeros;
    for(char algarismo : s) {
        if(algarismo != '+') {
            numeros.push_back(algarismo);
        }
    }
    sort(numeros.begin(), numeros.end());
    nova_soma = numeros[0];

    for(int i = 1; i < numeros.size(); ++i) {
        nova_soma += '+';
        nova_soma += numeros[i];
    }
    cout << nova_soma;
    return 0;
}