#include<bits/stdc++.h>
using namespace std;

// Code in leetcode editor
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> sol;
        map<int, int> mp;
        int diff, len = nums.size();
        for (int i = 0; i < len; i++)
        {
            diff = target - nums[i];
            if (mp.count(diff))
            {
                sol.push_back(i);
                sol.push_back(mp[diff]);
                break;
            }
            mp[nums[i]] = i;
        }

        return sol;
    }
};

/* Another implementation
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int> > vi;
        int c = 0;
        for(auto i: nums){
            vi.push_back({i, c++});
        }
        sort(vi.begin(), vi.end());
        int i = 0, j = nums.size() - 1;
        while( i < j){
            int res = vi[i].first + vi[j].first;
            if (res == target){
                i = vi[i].second, j = vi[j].second;
                break;
            } else if(res < target){
                i++;
            } else {
                j--;
            }
        }
        return {i,j};
    }
};
*/