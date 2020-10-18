#include <iostream>
#include <string>
#include <queue>
#include <stack>
using namespace std;


int main(){
    int T;
    cin>>T;
    while(T--){
        int N, M;
        string table,people;
        cin>>N>>table>>M>>people;
        priority_queue<int, vector<int>, greater<int> > pq1;
        stack<int> stk0;
        for(int i=0;i<N;i++){
            if(table[i]=='1'){
                pq1.push(i+1);
            }
            if(table[N-i-1]=='0'){
                stk0.push(N-i-1+1);
            }
        }
        for(int i=0;i<M;i++){
            if(people[i] == 'M'){
                if(pq1.empty()){
                    pq1.push(stk0.top());
                    stk0.pop();
                    cout<<pq1.top()<<endl;
                }
                else{
                    cout<<pq1.top()<<endl;
                    pq1.pop();
                }
            }
            else{
                if(!stk0.empty()) {
                    cout << stk0.top() << endl;
                    pq1.push(stk0.top());
                    stk0.pop();
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
