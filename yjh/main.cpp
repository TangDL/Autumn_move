#include <bits/stdc++.h>
using namespace std;

void op(){
    int n, m;
    cin>>n>>m;
    vector<set<int>> store(n+1);
    while(m--){
        int a,b;
        cin>>a>>b;
        store[a].insert(b);
    }
    for(int i=1;i<=n;i++){
        for(auto it = store[i].begin();it!=store[i].end();it++){
            if((*it)==i)continue;
            for(auto it2 = store[*it].begin();it2!=store[*it].end();it2++) {
                store[i].insert(*it2);
            }
        }
    }
    vector<int> nums(n+1);
    for(int i=1;i<=n;i++){
        for(auto it = store[i].begin();it!=store[i].end();it++){
            if((*it)==i)continue;
            nums[*it]++;
        }
    }
    int resbig=0,ressmall=0;
    for(int i=1;i<=n;i++) {
        if(nums[i]==n-1){
            if(resbig==0){
                resbig = i;
            }
            else{
                resbig=-1;
            }
        }
        if(nums[i]==0){
            if(ressmall==0){
                ressmall = i;
            }
            else{
                ressmall=-1;
            }
        }
    }
    if(resbig==0)resbig=-1;
    if(ressmall==0)ressmall=-1;
    cout<<resbig<<" "<<ressmall<<endl;
    return;
}

int main(){
    op();
    return 0;
}

//5 5
//2 1
//2 3
//1 3
//3 4
//4 5