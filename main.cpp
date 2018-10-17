#include <iostream>
#include<stdio.h>
using namespace std;
int N;


bool isSafe(int X[], int k, int y) {
	int i = 0;
	while ((i != k) && (y != X[i]) && (abs(k - i) != abs(y - X[i]))) { // проверяем не бьется ли с предыдущими ферзями
		i++;
	}
	if (i == k)
		return true;
	else return false;
}

void rasst(int k, int &tempRef, int X[]) {  // расстановка ферзей с проверкой на "бой"
	int y;

	for (y = 0; y < N; y++) {
		if (isSafe(X, k, y)) {
			X[k] = y;
			if (k == N - 1) {
				tempRef++;
			}
			rasst(k + 1, tempRef, X);
		}
	}
}

int main() {
	int temp;
	temp = 0;
	int &tempRef = temp;
	const int S = 11;
	int X[S]{};

	cin >> N;
	rasst(0, tempRef, X);
	cout << temp;
	return 0;
}