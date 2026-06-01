#include <iostream>
#include <vector>
using namespace std;

bool too_long_or_not(string word){
    return (word.size() <= 10);
}

string abbreviate(string word){
    int num_char;
    string abbreviation;
    num_char = word.size() - 2;
    string num = to_string(num_char);
    word = word[0] + num + word[num_char + 1];
    
    return word;
}

int main(){
    int n;
    cin >> n;
    vector<string> palavras;

    for(int i = 0; i < n; i++){
        string word;
        cin >> word;
        
        if(too_long_or_not(word)){
            palavras.push_back(word);
        }else{
            word = abbreviate(word);
            palavras.push_back(word);
        }
    }

    for(int i = 0; i < n; i++){
        cout << palavras[i] << endl;
    }

    return 0;
}