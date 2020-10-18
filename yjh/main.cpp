#include <bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
        int N, M;
        string table,people;
        cin>>N>>table>>M>>people;
        priority_queue<int, vector<int>, greater<int> > pq0,pq1;
        for(int i=N-1;i>=0;i--){
            if(table[i]=='1'){
                pq1.push(i+1);
            }
            else if(table[i]=='0'){
                pq0.push(i+1);
            }
        }
        cout<<endl;
        for(int i=0;i<M;i++){
            if(people[i] == 'M'){
                if(pq1.empty()){
                    pq1.push(pq0.top());
                    pq0.pop();
                    cout<<pq1.top()<<endl;
                }
                else{
                    cout<<pq1.top()<<endl;
                    pq1.pop();
                }
            }
            else{
                if(!pq0.empty()) {
                    cout << pq0.top() << endl;
                    pq1.push(pq0.top());
                    pq0.pop();
                }
                else{
                    cout<<pq1.top()<<endl;
                    pq1.pop();
                }
            }
        }
    }
    return 0;
}

//2
//5
//01102
//6
//MFMMFF
//5
//01102
//6
//MFMMFF
