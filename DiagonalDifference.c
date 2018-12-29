#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int a[100][100];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            scanf("%d ", &a[i][j]);
        }
        scanf("\n");
    }

    int d1 = 0;
    int d2 = 0;

    for (int i = 0; i < n; i++)
    {
        d1 += a[i][i];
        d2 += a[i][n - i - 1];
    }

    int fin = fabs(d1 - d2);

    printf("%d", fin);
    return 0;
}
