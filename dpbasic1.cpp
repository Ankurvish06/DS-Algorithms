
https://www.spoj.com/problems/CODEIT02/


const int nax = 25;
int n, k;
vector<int> a(nax);

int solve(int pos, int rem, int prevXor)
{
	if (pos == n) // Exhausted the element choice
	{
		if (rem == 0) // You have chosen k elements somehow, so this is valid
			return prevXor;
		else
			return 0; // Something went wrong returning the least possible value 
	}
	if (rem == 0) // Whoa! You have to finish the taking process
		return prevXor;
	// Now me have a choice
	int ret = max(solve(pos + 1, rem, prevXor), solve(pos + 1, rem - 1, prevXor ^ a[pos]));
	// Take the element or not -- Choose the best
	return ret;
}

void solve()
{
	cin >> n >> k;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	cout << solve(0, k, 0) << '\n';
}
