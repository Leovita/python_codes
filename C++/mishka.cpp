#include <bits/stdc++.h>
#include<iostream>
#include<cstring>

using namespace std;

string solve() {
    int n;
    cin >> n;
    int m;
    int c;
    int mishka = 0;
    int chris = 0;
    for(int i = 0; i < n; i ++){
        cin >> m >> c;

        if(m > c){
            mishka ++;
        }    
        else if(m < c){
            chris ++;
        }

    }

    if (mishka > chris){
        return "Mishka";
    }
    else if (chris > mishka){
        return "Chris";
    }
    else{
        return "Friendship is magic!^^";
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    //int tc = 1;
    // cin >> tc;
    //for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t  << ": ";
    cout << solve() << endl;
    }