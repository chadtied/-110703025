#include<iostream>
#include<vector>
#include<ctime>
#include<cmath>

using namespace std;

//輸入input值進入arr of sorted array
void InputArr(vector<int>& arr1, vector<int>& arr2, int input){
        int flag1= 0, flag2= 0;

        if(arr1[0]== -1){
                arr1[0]= input;
                flag1= 1;
        }
        if(flag1== 0){
                if(arr2[0]== -1){
                        arr2[0]= input;
                        flag2= 1;
                }
        }
}

//合併同樣大小的arr1 arr2，並push至下一層arr
void merge(vector<int>& target, vector<int>& arr1, vector<int>& arr2){
        int ptr1= 0, ptr2= 0, len= target.size();

        for(int i= 0; i< len; i++){
                if(ptr1== arr1.size())
                        target[i]= arr2[ptr2++];
                else if(ptr2== arr2.size())
                        target[i]= arr1[ptr1++];
                else if(arr1[ptr1]< arr2[ptr2])
                        target[i]= arr1[ptr1++];
                else
                        target[i]= arr2[ptr2++];
        }
        for(int i= 0; i< arr1.size(); i++){
                arr1[i]= -1;
                arr2[i]= -1;
        }
}

//迴圈檢查arr1和arr2是否都已滿，如果是則merge
void SortArr(vector<int> arr1[], vector<int> arr2[], int key){
        if(key== 27)
                return;
        if(arr1[key][0]!= -1&& arr2[key][0]!= -1){
                if(arr1[key+1][0]== -1)
                        merge(arr1[key+1], arr1[key], arr2[key]);
                else if(arr2[key+1][0]== -1)
                        merge(arr2[key+1], arr1[key], arr2[key]);
        }

        SortArr(arr1, arr2, key+1);
}

//利用二分搜尋，找尋陣列中符合target的值
void binary_search(vector<int>& arr, int first, int last, int target){
        int mid= (first+last)/2;
        if(arr[mid]== target){
                return;
        }
        if(mid== first)
                return;
        else if(arr[mid]< target)
                binary_search(arr, mid+ 1, last, target);
        else
                binary_search(arr, first, mid, target);
}

//搜索每層陣列，如果不為空則搜尋target值
void Search(vector<int> arr[], int key, int target){
        if(arr[key][0]== -1)
                Search(arr, key+1, target);
        else
                binary_search(arr[key], 0, arr[key].size(), target);
}




int main(){
        srand(time(NULL));
        //arr1[i] 為每層的陣列，arr2為其複製陣列
        vector<int> arr1[30], arr2[30];
        int num, input;
        double start, end;
        cin>> num;
        num= pow(2, num);
        //建立空間，將-1是為沒有值的預設
        for(int i= 0; i< 27; i++){
                for(int k= 0; k< pow(2, i); k++){
                        arr1[i].push_back(-1);
                        arr2[i].push_back(-1);
                }
        }

        start= clock();
        for(int i= 0; i< num; i++){
                input= rand()%1000000;
            
                InputArr(arr1[0], arr2[0], input);
                //每輸入完則檢查每個sorted array是否有滿
                SortArr(arr1, arr2, 0);
        }
        end= clock();
        cout<< "inverse costs "<< (end- start)/1000<< "sec"<< endl;
        /*for(int i= 0; i< 6; i++){
                for(int k= 0; k< arr1[i].size(); k++){
                        cout<< arr1[i][k]<< " ";
                }
                cout<< ",";
                for(int k= 0; k< arr1[i].size(); k++){
                        cout<< arr2[i][k]<< " ";
                }
                cout<< endl;
        }*/
        start= clock();
        for(int i= 0; i< 100000; i++){
                Search(arr1, 0, rand()%1000000);
        }
        end= clock();
        cout<< "traverse costs "<< (end- start)/1000<< "sec"<< endl;
}
