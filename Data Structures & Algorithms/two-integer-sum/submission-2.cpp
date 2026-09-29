#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int numberNeeded;

        for(int i =0; i<nums.size();i++){
            map[nums[i]] = i;
        }

        for(int i = 0; i<nums.size(); i++){
            numberNeeded = target - nums[i];
            if(map.count(numberNeeded)>0 && map.at(numberNeeded)!=i){
                return {i, map[numberNeeded]};
            }
        }
    }
};
