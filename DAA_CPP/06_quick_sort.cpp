#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std;

int partitionArray(vector<int>& a, int low, int high) {
    int pivot = a[high], i = low - 1;
    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[high]);
    return i + 1;
}

void quickSort(vector<int>& a, int low, int high, bool randomized) {
    if (low >= high) return;
    if (randomized) {
        int r = low + rand() % (high - low + 1);
        swap(a[r], a[high]);
    }
    int p = partitionArray(a, low, high);
    quickSort(a, low, p - 1, randomized);
    quickSort(a, p + 1, high, randomized);
}

int main() {
    srand((unsigned)time(nullptr));
    int n;
    cout << "Number of elements: ";
    cin >> n;
    vector<int> a(n), b;
    for (int i = 0; i < n; i++) cin >> a[i];
    b = a;

    quickSort(a, 0, n - 1, false);
    quickSort(b, 0, n - 1, true);

    cout << "Deterministic: ";
    for (int x : a) cout << x << " ";
    cout << "\nRandomized: ";
    for (int x : b) cout << x << " ";
    cout << "\nAverage/expected time: O(n log n), worst: O(n^2)\n";
    return 0;
}