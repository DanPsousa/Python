def quest18(x, y, z):

	nums = [x, y, z]

	nums.sort()

	return nums[2]

try:

	x, y, z = int(input("Forneça três valores inteiros: ")), int(input()), int(input())

	print("O maior dos três valores é %d." % quest18(x, y, z))

except:

	print("Não foram fornecidos valores três inteiros.")
