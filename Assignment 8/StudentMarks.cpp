#include <bits/stdc++.h>
using namespace std;

void countHighScores(int scores[] , int n){
    int count = 0;

    for(int i=0;i<n;i++){
        if(scores[i]>60){
            count++;
        }
    }
    return count;
}

void displayScores(int scores[], int n){
    for(int i=0;i<n;i++){
        if(scores[i]>60){
            cout<<scores[i]<<" ";
        }
    }
}

int main(){
    int n;
    cout<<"Enter the number: ";
    cin>>n;

    int scores[n];

        cout << "Enter marks:\n";
        for (int i = 0; i < n; i++) {
        cin >> scores[i];
    }

    int count = countHighScore(scores, n);

    cout << "\nNumber of students with marks > 60: " << count << endl;

    displayScores(scores, n);

    return 0;
}