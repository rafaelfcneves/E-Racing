    #include <iostream>
    using namespace std;

    int main(){
        int n;
        int X = 0;
        string operador;
        cin >> n;
        for(int i = 0; i < n; i++) {
            cin >> operador;
            if(operador == "++X" || operador == "X++") {
                X++;
            } else if(operador == "--X" || operador == "X--") {
                X--;
            }
        }
        cout << X;
        return 0;
    }