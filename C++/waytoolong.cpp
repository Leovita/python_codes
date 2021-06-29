#include <bits/stdc++.h>
#include<iostream>
#include<cstring>

using namespace std;

#define ar array
#define ll long long

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;



string solve() {
    cout << "porcodio";
    int count = 0;
    string s;
    string ans;
    cin >> s;
    cout << s.size();
    if (s.size() > 10){ 
        for(int i = 1; i < s.size() - 1; i++){
            count ++;
        }
        ans = s[0] + to_string(count) + s[s.size()];
        cout << ans;
    }
    else{
        cout << s << endl;
    }

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    //cout << solve() << endl;
    } 

}