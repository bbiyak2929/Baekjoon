#include <stdio.h>
int main() {
	int N;
    scanf("%d", &N);
	int arr[1001];
	arr[0] = 1;
	arr[1] = 1;
	for (int i = 2; i <= N; i++) {
		arr[i] = arr[i - 1] + arr[i - 2];
        arr[i] = arr[i] % 10007;
		
	}
	printf("%d", arr[N]);
    return 0;
}