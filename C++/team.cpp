#include <bits/stdc++.h>
#include<iostream>
#include<cstring>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    int ans = 0;
    int ar[3];
    for (int t = 1; t <= tc; t++) {   
        int cont = 0;
        for(int i = 0; i < 3; i++){
            cin >> ar[i];
        }   

        for(int j = 0; j < 3; j++){
            if(ar[j] == 1){
                cont ++;
            }
        }
        if(cont >= 2){
            ans ++;
        }
    }
    cout << ans << endl;
}