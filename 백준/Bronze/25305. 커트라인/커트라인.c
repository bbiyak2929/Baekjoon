#include <stdio.h>

int arr[1000];
void sort(int* arr, int a) {
	int i, j, k;
	for (i = 0; i < a; i++) {
		k = arr[i];
		for (j = i - 1; j >= 0 && arr[j] > k; j--) {
			arr[j + 1] = arr[j];
		}
		arr[j + 1] = k;
	}

}

int main() {
	int a, b;
	int i;
	scanf("%d %d", &a, &b);
	for (i = 0; i < a; i++) {
		scanf("%d ", &arr[i]);
		
	}
	
	
	sort(arr, a); 
	printf("%d", arr[a - b]);
	return 0;
}