class validateSubsequence:
    # O(n) time | O(1) space
    @staticmethod
    def validateSubsequence(array, sequence):
        """
        This method is used to check the subsequence 
        Definition of subsequence: 
            In mathematics, a subsequence is a sequence that can be derived from another 
            sequence by deleting some or no elements without changing the order of the remaining elements.
            For example, the sequence {A,B,D} is a subsequence of {A,B,C,D,E,F}  obtained after removal of elements.
        """
        #Initalize the array indexes
        arrayIdx = 0 
        seqIdx = 0
        # While loop to check the indexes within the bound 
        while arrayIdx < len(array) and seqIdx < len(sequence): 
            #If the value is same then increment the sequence index
            if array[arrayIdx] == sequence[seqIdx]: 
                seqIdx = seqIdx + 1     
            arrayIdx = arrayIdx + 1
            # return whether the sequence is covered
            return seqIdx == len(sequence)



if __name__ == '__main__': 

    print(validateSubsequence.validateSubsequence([1, 1, 6, 1],[1, 1, 1, 6]))