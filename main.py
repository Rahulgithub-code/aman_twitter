
def getLargestString(s, k):


	frequency_array = [0] * 26


	for i in range(len(s)):

		frequency_array[ord(s[i]) -
						ord('a')] += 1


	ans = ""


	i = 25
	while i >= 0:


		if (frequency_array[i] > k):


			temp = k
			st = chr( i + ord('a'))
			
			while (temp > 0):


				ans += st
				temp -= 1
		
			frequency_array[i] -= k


			j = i - 1
			
			while (frequency_array[j] <= 0 and
				j >= 0):
				j -= 1
		

			if (frequency_array[j] > 0 and
				j >= 0):
				str1 = chr(j + ord( 'a'))
				ans += str1
				frequency_array[j] -= 1
			
			else:


				break
			

		elif (frequency_array[i] > 0):


			temp = frequency_array[i]
			frequency_array[i] -= temp
			st = chr(i + ord('a'))
			while (temp > 0):
				ans += st
				temp -= 1
			

		else:
			i -= 1
			
	return ans		


if __name__ == "__main__":

	S = input()
	k = 2
	print (getLargestString(S, k))


