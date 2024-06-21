https://leetcode.com/problems/trapping-rain-water/

- two pointer approach
- we need to fill water anyway if there is one bar from left smaller than any bar(not adjacant,doenot happen because we ue 2 pintern in the conditiion i< j) in right trap water. same goes with right side also. so create an left _max and right max pointers incremanet th left pinter when it is less than or equal to right max then subract the height of current iterting one(this elimnates the problem when iterating elemnt and left_max are equal)