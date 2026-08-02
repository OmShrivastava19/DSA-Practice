class Solution {
  public:
    vector<int> getMinMax(vector<int> &arr) {
        int n = arr.size();
        int min;
        int max;
        for (int i=0; i<n;i++){
            if (arr[i]>max){
                max = arr[i];
            }
            if (arr[i]<min){
                min = arr[i];
            }
        }
        return {min, max};
    }
};
