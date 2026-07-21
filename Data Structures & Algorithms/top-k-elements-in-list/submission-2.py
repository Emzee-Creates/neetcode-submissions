class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Make our tally chart
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
                
        winners = []
        for _ in range(k):
            highest_votes = -1
            highest_voted_number = None
        
            for number, votes in counts.items():
                if votes > highest_votes:
                    highest_votes = votes
                    highest_voted_number = number
            
            winners.append(highest_voted_number)
            del counts[highest_voted_number] 
            
        return winners