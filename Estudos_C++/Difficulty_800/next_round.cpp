#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, k;
    int aprovados = 0;
    int x;
    vector<int> scores;

    cin >> n >> k;
    
    for(int i = 0; i < n; i++){
        cin >> x;
        scores.push_back(x);
    }
    
    int pontuacao_min = scores[k-1];

    for(int i = 0; i < n; i++){
        if(scores[i] == 0){
            break;
        }
        else if(scores[i] >= pontuacao_min){
            aprovados++;
        }
    }

    cout << aprovados;

    return 0;
}