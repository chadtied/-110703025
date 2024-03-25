#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

bool B2(int arr[], int len ,int record[]);
int main(){
        int len, arr[100]= {0}, val, record[20001]= {0}, count= 1;
        while(cin>> len){
        for(int i= 0; i< len; i++){
                cin>> val;
                arr[i]= val;
        }
        if(B2(arr, len, record))
                cout<<"Case #"<< count<< ": "<< "It is a B2-Sequence."<< endl<< endl;
        else
                cout<< "Case #"<< count<< ": "<<"It is not a B2-Sequence."<< endl<< endl;
        count++;
        }
}

bool B2(int arr[], int len, int record[]){
        bool flag= false;
        for(int i= 0; i< len; i++){
                for(int k= i; k< len; k++){
                        if(record[arr[i]+arr[k]]== 1){
                                flag= true;
                                break;
                        }
                        record[arr[i]+arr[k]]= 1;
                }
                if(flag)
                        return false;
        }
        return true;
}
