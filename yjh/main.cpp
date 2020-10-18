#include <bits/stdc++.h>
using namespace std;


void helper(int N, string& table, int& table_st, priority_queue<int, vector<int>, greater<int>>& pq1, stack<int>& stk0){
//        for(int i=N-1;i>=0;i--){
    while(table_st!=N && (pq1.empty() || stk0.empty())){
        if(table[table_st]=='1'){
            pq1.push(table_st+1);
        }
        else if(table[table_st]=='0'){
            stk0.push(table_st+1);
        }
        table_st++;
    }
}
int main(){
    int T;
    cin>>T;
    while(T--){
        int N, M;
        string table,people;
        cin>>N>>table>>M>>people;
        priority_queue<int, vector<int>, greater<int> > pq1;
        stack<int> stk0;
        int table_st = 0;
        helper(N, table, table_st, pq1, stk0);
        for(int i=0;i<M;i++){
            if(people[i] == 'M'){
                helper(N, table, table_st, pq1, stk0);
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
                helper(N, table, table_st, pq1, stk0);
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
