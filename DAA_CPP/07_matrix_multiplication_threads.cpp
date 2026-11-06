#include <iostream>
#include <vector>
#include <thread>
using namespace std;

void multiplyRow(const vector<vector<int>>& A, const vector<vector<int>>& B,
                 vector<vector<int>>& C, int row, int n) {
    for (int j = 0; j < n; j++)
        for (int k = 0; k < n; k++)
            C[row][j] += A[row][k] * B[k][j];
}

int main() {
    int n;
    cout << "Matrix size n: ";
    cin >> n;
    vector<vector<int>> A(n, vector<int>(n)), B(n, vector<int>(n));
    vector<vector<int>> C(n, vector<int>(n, 0));

    cout << "Enter matrix A:\n";
    for (auto& row : A) for (int& x : row) cin >> x;
    cout << "Enter matrix B:\n";
    for (auto& row : B) for (int& x : row) cin >> x;

    vector<thread> threads;
    for (int i = 0; i < n; i++)
        threads.emplace_back(multiplyRow, cref(A), cref(B), ref(C), i, n);
    for (auto& t : threads) t.join();

    cout << "Product:\n";
    for (auto row : C) {
        for (int x : row) cout << x << " ";
        cout << "\n";
    }
    cout << "Time complexity: O(n^3); extra space: O(n^2)\n";
    return 0;
}