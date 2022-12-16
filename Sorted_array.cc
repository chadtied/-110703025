#include<iostream>
#include<vector>
#include<ctime>
#include<cmath>

using namespace std;

//if a data is input , use the concept of insertion sort to insert it to the correct order
void insert(vector<int>& arr, int input){
        arr.push_back(input);
        for(int i= arr.size()-2; i>= 0; i--){
                if(arr[i]<= input){
                        break;
                }
                else{
                        arr[i]= arr[i]^arr[i+1];
                        arr[i+1]= arr[i]^arr[i+1];
                        arr[i]= arr[i]^arr[i+1];
                }
        }
}
//use binary_search to find the data
void search(vector<int>& arr, int head, int tail, int input){
        int mid= (head+tail)/2;
        if(arr[mid]== input){
                return;
        }
        else if(mid== head){
                return;
        }
        else if(input> arr[mid]){
                search(arr, mid+1, tail, input);
        }
        else{
                search(arr, head, mid-1, input);
        }
}
int main(){
        srand(time(NULL));
        vector<int> arr;
        double start, end;
        int num;
        cin>> num;
        num= pow(2,num);

        start= clock();
        //insert 2^n data
        for(int i= 0; i< num; i++){
                insert(arr, rand()%100000000);
        }
        end= clock();
        cout<< "insertion costs "<< (end- start)/1000<< "sec"<< endl;

        start= clock();
        //search 100000data
        for(int i= 0; i< 100000; i++){
                search(arr, 0, arr.size(), rand()%100000000);
        }

        end= clock();
        cout<< "traverse costs "<< (end- start)/1000<< "sec"<< endl;
}
