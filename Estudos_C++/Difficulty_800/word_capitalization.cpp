#include <iostream>
using namespace std;

int main() {
    string palavra, resto_palavra;
    char primeiro_char;
    cin >> palavra;
    if(palavra[0] > 'Z') {
        primeiro_char = palavra[0] - 32;
        for(int i = 1; i < palavra.size(); ++i) {
            resto_palavra += palavra[i];
        }
        palavra = primeiro_char + resto_palavra;
    }
    cout << palavra;
    return 0;
}