#include <iostream>
using namespace std;

bool end_in_zero_or_not(int n)
{
    return (n % 10 == 0);
}

int subtraction(int n)
{
    if(end_in_zero_or_not(n)){
        n = n / 10;
    }else{
        n = n - 1;
    }
    return n;
}

int main(){
    int n, k;
    cin >> n >> k;
    
    for (int i = 0; i < k; i++){
        n = subtraction(n);
    }
    cout << n;
    return 0;
}