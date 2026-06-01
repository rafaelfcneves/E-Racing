#include <iostream>
using namespace std;

int main() {
    int matriz[5][5];
    int linha, coluna;
    int movimentos;

    for(int i = 0; i < 5; ++i){
        for(int j = 0; j < 5; ++j){
            cin >> matriz[i][j];
            if(matriz[i][j] == 1){
                movimentos = abs(i-2) + abs(j-2);
            }
        }
    }
    cout << movimentos;
    return 0;
}