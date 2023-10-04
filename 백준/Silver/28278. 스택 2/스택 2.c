#include<stdio.h>
int main() {
	int stack[1000000] = {0,};
	int i, n,N,x;
	int top;
	top = -1;
	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%d", &n);
        if (n == 1) {

		scanf("%d", &x);
		stack[++top] = x;
	
	}
	else if (n == 2) {
		if (top != -1) {
			printf("%d\n", stack[top--]);
		}
		else {
			printf("-1\n");
		}
	}
	else if (n == 3) {
		printf("%d\n", top+1);
	}
	else if (n == 4) {
		if (top == -1) {
			printf("1\n");
		}
		else {
			printf("0\n");
		}
	}
	else if (n == 5) {
		if (top != -1) {
			printf("%d\n", stack[top]);
		}
		else {
			printf("-1\n");
		}
	 }
 }
	

}
