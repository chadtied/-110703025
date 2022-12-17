//採用c++函式庫內unordered_map實作hash_table

#include<iostream>
#include<unordered_map>
#include<cmath>
#include<ctime>

using namespace std;

int main(){
        srand(time(NULL));

        int num;
        double start, end;
        unordered_map<long long, int> table;
        pair<unordered_map<long long, int>::iterator, bool> ptr;

        cin>> num;
        num= pow(2,num);

        start= clock();
        for(int i= 0; i<num; i++){
                do{
                        ptr= table.insert(pair<long long, int>(rand()%(num*10), rand()%100000000));
                }while(!ptr.second);
        }
        end= clock();
        cout<< "inverse costs "<< (end- start)/1000<< "sec"<< endl;


        start= clock();
        for(int i= 0; i< 100000; i++){
                int val= rand()%100000000;
                for(auto it= table.begin(); it!= table.end(); it++){
                        if(it->first== val)
                                break;
                }
        }
        end= clock();
        cout<< "traverse costs "<< (end- start)/1000<< "sec"<< endl;


        cout<< endl;
}
