
#include <string.h>
#include  <stdlib.h>
char * mergeAlternately(char * word1, char * word2)
{
   int m = strlen(word1);
    int n = strlen(word2);
    char * result = (char *)malloc(m+n+1);
    int i = 0, j = 0, k = 0;
    
    while (i < m || j < n)
    {
        if (i < m)
        {
            result[k] = word1[i];
            i++;
            k++;
        }
        if (j < n)
        {
            result[k] = word2[j];
            j++;
            k++;
        }
    }
    result[k] = '\0';
    
    return (result);
}