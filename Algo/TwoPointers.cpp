'''Two pointer is really an easy and effective technique which is typically used for searching pairs in a sorted arrays.'''


// Two pointer technique based solution to find 
// if there is a pair in A[0..N-1] with given sum.
bool isPairSum(A[], N, X)
{
    // represents first pointer
    int i = 0;
 
    // represents second pointer
    int j = N - 1;
 
    while (i < j) {
 
        // If we find a pair
        if (A[i] + A[j] == X)
            return true;
 
        // If sum of elements at current
        // pointers is less, we move towards
        // higher values by doing i++
        else if (A[i] + A[j] < X)
            i++;
 
        // If sum of elements at current
        // pointers is more, we move towards
        // lower values by doing i++
        else
            j--;
    }
    return false;
}
