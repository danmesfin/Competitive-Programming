class Solution:
	def compress(self, chars: List[str]) -> int:
		i, j = 0, 0
		ans = []
		count = 0

		while j < len(chars):
			while j < len(chars) and chars[j] == chars[i]:
				j += 1
				count += 1

			ans.append(chars[j-1])
			if count != 1 and count < 10:
				ans.append(str(count))
			if count >= 10:
				count = str(count)
				for x in count:
					ans.append(x)
			i = j
			count = 0

		chars[:] = ans
		return len(chars)
