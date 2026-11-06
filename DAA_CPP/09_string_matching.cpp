#include <iostream>
#include <string>
using namespace std;

int main() {
    string text, pattern;
    cout << "Enter text: ";
    cin >> text;
    cout << "Enter pattern: ";
    cin >> pattern;

    cout << "Naive matches at index: ";
    bool found = false;
    for (int i = 0; i + (int)pattern.size() <= (int)text.size(); i++) {
        int j = 0;
        while (j < (int)pattern.size() && text[i + j] == pattern[j]) j++;
        if (j == (int)pattern.size()) { cout << i << " "; found = true; }
    }
    if (!found) cout << "none";

    const int d = 256, q = 101;
    int m = pattern.size(), n = text.size(), p = 0, t = 0, h = 1;
    for (int i = 0; i < m - 1; i++) h = (h * d) % q;
    for (int i = 0; i < m && i < n; i++) {
        p = (d * p + pattern[i]) % q;
        t = (d * t + text[i]) % q;
    }
    cout << "\nRabin-Karp matches at index: ";
    found = false;
    for (int i = 0; i <= n - m; i++) {
        if (p == t && text.substr(i, m) == pattern) {
            cout << i << " "; found = true;
        }
        if (i < n - m) {
            t = (d * (t - text[i] * h) + text[i + m]) % q;
            if (t < 0) t += q;
        }
    }
    if (!found) cout << "none";
    cout << "\nNaive worst-case: O(nm); Rabin-Karp average: O(n+m), worst: O(nm)\n";
}