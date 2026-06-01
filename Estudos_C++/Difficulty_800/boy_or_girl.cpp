#include <iostream>
#include <set>
using namespace std;

int main() {
    string name;
    cin >> name;
    set<char> letras_distintas;
    for(char c : name) {
        letras_distintas.insert(c);
    }

    if(letras_distintas.size() % 2 == 0) {
        cout << "CHAT WITH HER !";
    } else {
        cout << "IGNORE HIM !";
    }

    return 0;
}