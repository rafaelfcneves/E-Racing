#include <iostream>
using namespace std;

void transformar_em_minusculo(string& palavra){
    for(int i = 0; i < palavra.size(); ++i){
        if('A' <= palavra[i] && palavra[i] <= 'Z') {
            palavra[i] += 32;
        }
    }
}

int main(){
    string palavra1, palavra2;
    cin >> palavra1;
    cin >> palavra2;
    transformar_em_minusculo(palavra1);
    transformar_em_minusculo(palavra2);
    if(palavra1 > palavra2){
        cout << 1;
    } else if(palavra1 == palavra2){
        cout << 0;
    } else {
        cout << -1;
    }
    return 0;
}