#include <iostream>
#include <vector>
using namespace std;

bool contar_zero(vector<int> lista){
    int num_zero = 0;
    for (int num : lista){
        if(num == 0){
            num_zero++;
        }
    }
    return (num_zero < 2);
}

int main(){
    int n;
    int solucoes = 0;
    
    cin >> n;
    
    for(int i = 0; i < n; i++){
        int p, v, t;

        cin >> p >> v >> t;
        vector<int> lista = {p, v, t};

        if(contar_zero(lista)){
            solucoes++;
        }
        lista.clear();
    }
    cout << solucoes;
    return 0;
}